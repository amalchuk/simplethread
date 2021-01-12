.PHONY: all install install-development build update upload test coverage clean

all: install clean

install:
	@echo "Installing the package"
	@poetry install --no-dev --no-interaction

install-development:
	@echo "Installing the package in the development mode"
	@poetry install --no-root --no-interaction

build:
	@echo "Building the package"
	@poetry build --format sdist --no-interaction

update:
	@echo "Downloading the latest versions of the dependencies"
	@python -m pip install pip setuptools wheel --upgrade --force-reinstall --no-cache-dir
	@poetry update --no-interaction

upload:
	@echo "Upload to the package registry"
	@poetry publish --no-interaction

test:
	@echo "Running the test cases"
	@poetry run coverage run -m pytest --exitfirst --quiet

coverage: test
	@echo "Analyzing the code coverage for all test cases"
	@poetry run coverage report

clean:
	@echo "Delete all temporary files"
	@find simplethread tests -type f -name '*.py[cod]' | xargs rm --force
	@find simplethread tests -type d -name '__pycache__' | xargs rm --force --recursive
