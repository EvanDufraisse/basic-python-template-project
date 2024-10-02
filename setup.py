# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = {"": "src"}

packages = ["PACKAGE_NAME"]

package_data = {"": ["*"]}

install_requires = [PACKAGES]

dependency_links = []

entry_points = {"console_scripts": []}

setup_kwargs = {
    "name": "PROJECT_NAME",
    "version": "0.1.0",
    "description": "SHORT_DESCRIPTION",
    "long_description": f"PROJECT_NAME: TODO: make a full description of the project",
    "author": "FIRST_LAST_AUTHOR",
    "author_email": "CONTACT_MAIL",
    "maintainer": "None",
    "maintainer_email": "None",
    "url": "None",
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "dependency_links": dependency_links,
    "python_requires": ">=PYTHON_VERSION",
}


setup(**setup_kwargs)
