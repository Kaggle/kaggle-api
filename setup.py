from setuptools import setup, find_packages

setup(
    name = 'kaggle',
    version = '1.3.0',
    description = 'Kaggle API',
    long_description = 'Official API for https://www.kaggle.com, accessible using a command line tool implemented in Python. Beta release - Kaggle reserves the right to modify the API functionality currently offered.',
    author = 'Kaggle',
    author_email = 'support@kaggle.com',
    url = 'https://github.com/Kaggle/kaggle-api',
    keywords = ['Kaggle', 'API'],
    entry_points = {
        'console_scripts': [
          'kaggle = kaggle.cli:main'
        ]
    },
    install_requires = ['urllib3 >= 1.15', 'six >= 1.10', 'certifi', 'python-dateutil'],
    packages = find_packages(),
    license = 'Apache 2.0'
)
