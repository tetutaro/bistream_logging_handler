#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import bistream_logging_handler


def setup_packages():
	metadata = dict()
	metadata['name'] = bistream_logging_handler.__package__
	metadata['version'] = bistream_logging_handler.__version__
	metadata['description'] = bistream_logging_handler.__doc__
	metadata['url'] = bistream_logging_handler.__url
	metadata['author'] = bistream_logging_handler.__author
	metadata['license'] = 'MIT'
	metadata['packages'] = find_packages()
	metadata['include_package_data'] = False
	metadata['install_requires'] = []
	setup(**metadata)
	return


if __name__ == "__main__":
	setup_packages()
