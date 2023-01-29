#!/usr/bin/env python
import os
import re
import argparse
from fnmatch import fnmatch

# Settings
COMPONENTS = [
    {'path': './kubernetes'},
    {'path': './linux'}
]

OUTPUT = {
    'documentation': './README.md'
}

IGNORE_FILES = ['.*', '_*']

REGEX_MARKDOWN_HEADER = re.compile(r'^(?P<pounds>#+)\s+(?P<text>.*)$')
REGEX_MARKDOWN_HEADER_LINK = re.compile(r'[\s\'\"\.\,\-_()]+')


# Functions
def get_files(path, pattern=None, ignore=None):
    result = []

    if ignore is None:
        ignore = IGNORE_FILES

    for root, _, files in os.walk(path):
        for file in files:
            is_matched = fnmatch(file, pattern) if pattern else True

            for ignore_pattern in ignore or ():
                if fnmatch(file, ignore_pattern):
                    is_matched = False
                    break

            if is_matched:
                result.append(os.path.join(root, file))

        break

    result.sort()

    return result


def process_component_files(processor, components=None, pattern=None, snippets=False):
    for component in (components or COMPONENTS):
        data = {
            'component': component,
            'files': get_files(component['path'], pattern=pattern)
        }

        if snippets:
            snippets_path = os.path.join(component['path'], 'snippets')

            if os.path.exists(snippets_path):
                data['snippets'] = get_files(snippets_path)

        processor(data)


def add_table_of_content(markdown):
    items = []

    for line in (markdown or '').splitlines():
        match = REGEX_MARKDOWN_HEADER.match(line)

        if match:
            level = len(match.group('pounds'))
            text = match.group('text').strip()
            items.append((level, text))

    rendered_items = []

    for level, text in items:
        spaces = '  ' * ((level - 1) if level > 0 else 0)
        link = REGEX_MARKDOWN_HEADER_LINK.sub('-', text.lower()).strip('-')

        rendered_items.append('{spaces}- [{text}](#{link})'.format(spaces=spaces, text=text, link=link))

    table_of_content = "\n".join(rendered_items)

    if table_of_content:
        markdown = "# Contents\n\n{}\n\n{}".format(table_of_content, markdown)

    return markdown


# Actions
def action_documentation():
    parts = []

    def processor(section):
        files, snippets = section.get('files'), section.get('snippets')

        for file in files or ():
            content = open(file).read().strip()

            if content:
                parts.append(content)

        # Add snippets only if documentation exists
        if parts:
            snippets_parts = []

            for file in snippets or ():
                content = open(file).read().strip()
                comment = []

                for line in content.splitlines():
                    line = line.strip()

                    if not line or line.startswith('#'):
                        comment.append(line.lstrip('#').lstrip())

                    else:
                        while comment and comment[-1] != '':
                            del comment[-1]

                        break

                if len(comment) >= 2:
                    header = comment[0]
                    del comment[0]

                    comment = "\n".join(comment).strip()

                    if comment:
                        snippets_parts.append("### {}\n\n{}\n\nSee file: `{}`.".format(header, comment, file))

            if snippets_parts:
                parts.append("## Snippets")
                parts.extend(snippets_parts)

    process_component_files(processor, pattern='*.md', snippets=True)

    if parts:
        output = OUTPUT['documentation']
        text = add_table_of_content("\n\n".join(parts)) + "\n"

        open(output, 'w').write(text)

        print("Generated: {}".format(output))


# Main
def main():
    parser = argparse.ArgumentParser(description="Knowledge Base management")
    action_parsers = parser.add_subparsers(help="Actions")

    # Documentation
    documentation_parser = action_parsers.add_parser('documentation', help="Generate documentation")
    documentation_parser.set_defaults(action='documentation')

    # Start
    arguments = vars(parser.parse_args())
    action = arguments.pop('action', None)

    if action:
        method_name = 'action_{}'.format(action)
        handler = globals().get(method_name)

        if not handler:
            raise Exception("Unknown method: {}".format(method_name))

        handler()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
