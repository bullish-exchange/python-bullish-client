from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='bullish',
    version=os.getenv('BUILD_VERSION', 'develop'),
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    test_suite='nose.collector',
    install_requires = [
        'colander',
        'requests',
        'eosio_signer @ git+ssh://git@github.com/bullish-exchange/python-signer@main#egg=eosio_signer'
    ],
    entry_points={
    })
