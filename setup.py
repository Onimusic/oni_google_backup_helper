from distutils.core import setup

from setuptools import find_packages

import os

current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    # Project name:
    name='oni_google_backup_helper',
    # Packages to include in the distribution:
    packages=['oni_google_backup_helper', *find_packages(',')],
    # Project version number:
    version='1.0',
    # List a license for the project, eg. MIT License
    license='',
    # Short description of your library:
    description='Helper de Backup para o Google dos OniDevs',
    # Long description of your library:
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Your name:
    author='Daniel Santana Santos',
    # Your email address:
    author_email='gc04346@gmail.com',
    # Link to your github repository or website:
    url='https://github.com/Gc04346',
    # Download Link from where the project can be downloaded from:
    download_url='https://github.com/Onimusic/oni_google_backup_helper.git',
    # List of keywords:
    keywords=['onimusic'],
    # List project dependencies:
    install_requires=[
        'cachetools',
        'certifi',
        'charset-normalizer',
        'google-api-core',
        'google-auth',
        'google-cloud-bigquery',
        'google-cloud-bigquery-datatransfer',
        'google-cloud-bigquery-storage',
        'google-cloud-core',
        'google-cloud-storage',
        'google-crc32c',
        'google-resumable-media',
        'googleapis-common-protos',
        'grpcio',
        'grpcio-status',
        'idna',
        'numpy',
        'packaging',
        'proto-plus',
        'protobuf',
        'pyarrow',
        'pyasn1',
        'pyasn1-modules',
        'pyparsing',
        'python-dateutil',
        'pytz',
        'requests',
        'rsa',
        'six',
        'urllib3',
    ],
    # https://pypi.org/classifiers/
    classifiers=["Private :: Do Not Upload"]
)
