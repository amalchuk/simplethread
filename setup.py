#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

setuptools_attributes = {
    "name": "simplethread",
    "version": "0.1.2",
    "author": "Andrew Malchuk",
    "author_email": "andrew.malchuk@yandex.ru",
    "description": "Some useful utilities for Python's threading module",
    "long_description": Path(__file__).with_name("README.md").read_text("utf-8"),
    "long_description_content_type": "text/markdown",
    "license": "MIT",
    "url": "https://gitlab.com/amalchuk/simplethread",
    "packages": ["simplethread"],
    "extras_require": {
        "development": [
            "coverage",
            "isort",
            "mypy",
            "pytest",
            "twine"
        ]
    },
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed"
    ],
    "package_data": {
        "simplethread": ["py.typed"]
    },
    "include_package_data": True,
    "python_requires": ">=3.6, <4.0",
    "zip_safe": False,
    "project_urls": {
        "Bug Reports": "https://gitlab.com/amalchuk/simplethread/issues",
        "Source": "https://gitlab.com/amalchuk/simplethread"
    }
}

if __name__ == "__main__":
    from setuptools import setup
    setup(**setuptools_attributes)
