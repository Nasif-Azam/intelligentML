#!/usr/bin/env python

"""The setup script."""

import io
from os import path as op
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

here = op.abspath(op.dirname(__file__))

# get the dependencies and installs
with io.open(op.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

requirements = [ 'numpy', 'pandas' ]

setup_requirements = [ 'numpy', 'pandas' ]

test_requirements = [ 'numpy', 'pandas' ]

setup(
    author="Nasif Azam",
    author_email='nasifazam07@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="An intelligent machine learning package. A Python library for handling duplicate data and performing data preprocessing on datasets. This library provides functions to identify and remove duplicate rows, handle missing values, and prepare data for analysis. All you have to do just provide the dataset url or path the library automatically do those tasks.",
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='intelligentML',
    name='intelligentML',
    packages=find_packages(include=['intelligentML', 'intelligentML.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Nasif-Azam/intelligentML',
    version='0.0.1',
    zip_safe=False,
)
