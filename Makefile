# Makefile used to manage the git repository, not for the tutorial

all:
	python ipynbhelper.py --check
	python ipynbhelper.py --render
	python ipynbhelper.py --clean
