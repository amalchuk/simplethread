.PHONY: all install install-development build upload clean

all: install clean

install:
	@echo "Installing the package"
	@python setup.py install --quiet

install-development:
	@echo "Installing the package in the development mode"
	@python -m pip install pip setuptools wheel --upgrade --quiet --no-cache-dir
	@python setup.py develop --quiet
	@pip install --requirement requirements-dev.txt --upgrade --quiet --no-cache-dir

build:
	@echo "Building the package"
	@python setup.py sdist

upload:
	@echo "Upload to the package registry"
	@find dist -type f | xargs twine upload --disable-progress-bar

clean:
	@echo "Delete all temporary files"
	@find . -type f -name '*.py[cod]' | xargs rm --force
	@find . -type d -name '__pycache__' | xargs rm --force --recursive