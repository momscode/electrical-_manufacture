# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in electrical_manufacture/__init__.py
from electrical_manufacture import __version__ as version

setup(
	name='electrical_manufacture',
	version=version,
	description='Custom Application For Electrical Manufacturing',
	author='Momscode Technologies',
	author_email='info@momscode.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
