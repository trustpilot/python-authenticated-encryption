from setuptools import setup
from os import path


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


requirements = [
    'pycryptodome==3.6.6'
]

setup(
    name='trustpilot_authenticated_encryption',
    version='1.1.0',
    description="Library for authenticated encryption used with Trustpilot",
    long_description=read_md('README.md'),
    url='https://github.com/trustpilot/python-authenticated-encryption',
    packages=['trustpilot_authenticated_encryption'],
    package_dir={'trustpilot_authenticated_encryption': 'trustpilot_authenticated_encryption'},
    include_package_data=True,
    install_requires=requirements,
    author='Trustpilot',
    license='MIT',
    test_suite='tests'
)
