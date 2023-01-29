#!/usr/bin/env python
import os
import re
from fnmatch import fnmatch

# Settings
COMPONENTS = [
  {'path': './kubernetes'}
]

OUTPUT = {
    'documentation': './README.md'
}

REGEX_MARKDOWN_HEADER = re.compile(r'^(?P<pounds>#+)\s+(?P<text>.*)$')
REGEX_MARKDOWN_HEADER_LINK = re.compile(r'[\s\(\)\.,_]+')


def get_files(path, pattern=None):
    result = []

    for root, _, files in os.walk(path):
        for file in files:
            is_matched = fnmatch(file, pattern) if pattern else True

            if is_matched:
                result.append(os.path.join(root, file))

        break

    return result


def process_component_files(processor, components=None, pattern=None):
    for component in (components or COMPONENTS):
        files = get_files(component['path'], pattern=pattern)
        processor(component, files)


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
        link = REGEX_MARKDOWN_HEADER_LINK.sub('-', text.lower())

        rendered_items.append('{spaces}- [{text}](#{link})'.format(spaces=spaces, text=text, link=link))

    table_of_content = "\n".join(rendered_items)

    if table_of_content:
        markdown = "# Contents\n\n{}\n\n{}".format(table_of_content, markdown)

    return markdown


def generate_documentation():
    parts = []

    def processor(_, files):
        for file in files:
            file_name = os.path.basename(file)

            if not file_name.startswith('_'):
                content = open(file).read().strip()

                if content:
                    parts.append(content)

    process_component_files(processor, pattern='*.md')

    if parts:
        output = OUTPUT['documentation']
        text = add_table_of_content("\n\n".join(parts)) + "\n"

        open(output, 'w').write(text)

        print("Generated: {}".format(output))


# Main
def main():
    generate_documentation()


if __name__ == '__main__':
    main()
