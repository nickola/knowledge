# Settings
MANAGE = ./manage.py

# Not to print any recipes before executing them
.SILENT:

# Targets are not files / directories ("all" - default target, invoked by simply executing "make")
.PHONY: all $(MAKECMDGOALS)

# Using "documentation" as default target
all: documentation

documentation:
	${MANAGE} documentation
