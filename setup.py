# coding=utf-8
from setuptools import setup, find_packages

# Note: pyproject.toml seems to be chosen by pip install over setup.py, so this
# file should not be used anymore. However, cloudbuild.yaml still uses setup.py
# to drive the build that is published to pypi.org. That needs to be changed
# before this file can be removed. And, due to that, pyproject.toml needs to be
# deleted before a release can be made.
# https://packaging.python.org/en/latest/guides/modernize-setup-py-project/
setup(
    name='kaggle',
    version='1.7.3b1',
    description='Kaggle API',
    long_description=(
        'Official API for https://www.kaggle.com, accessible using a command line '
        'tool implemented in Python. Beta release - Kaggle reserves the right to '
        'modify the API functionality currently offered.'),
    author='Kaggle',
    author_email='support@kaggle.com',
    url='https://github.com/Kaggle/kaggle-api',
    project_urls={
        'Documentation': 'https://www.kaggle.com/docs/api',
        'GitHub': 'https://github.com/Kaggle/kaggle-api',
        'Tracker': 'https://github.com/Kaggle/kaggle-api/issues',
    },
    keywords=['Kaggle', 'API'],
    entry_points={'console_scripts': ['kaggle = kaggle.cli:main']},
    install_requires=[
        'six >= 1.10', 'certifi >= 2023.7.22', 'python-dateutil', 'requests',
        'tqdm', 'python-slugify', 'urllib3', 'bleach', 'protobuf',
        'hatchling >= 1.27.0'
    ],
    packages=find_packages(
        where='src',
        include=['kaggle*'],
    ),
    package_dir={"": "src"})
