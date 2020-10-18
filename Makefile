.PHONY: all install install-development build upload test coverage clean

all: install clean

install:
	@echo "Installing the package"
	@python setup.py install

install-development:
	@echo "Installing the package in the development mode"
	@python -m pip install pip setuptools wheel --upgrade --force-reinstall --quiet --no-cache-dir
	@pip install --editable .[development] --upgrade --force-reinstall --quiet --no-cache-dir

build:
	@echo "Building the package"
	@python setup.py sdist

upload:
	@echo "Upload to the package registry"
	@find dist -type f | xargs twine upload --disable-progress-bar

test:
	@echo "Running the test cases"
	@coverage run -m pytest

coverage: test
	@echo "Analyzing the code coverage for all test cases"
	@coverage report

clean:
	@echo "Delete all temporary files"
	@find simplethread tests -type f -name '*.py[cod]' | xargs rm --force
	@find simplethread tests -type d -name '__pycache__' | xargs rm --force --recursive
