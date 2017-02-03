from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'pycryptodome'
]

setup(
    name='trustpilot_authenticated_encryption',
    version='1.0.0',
    description="Library for authenticated encryption used with Trustpilot",
    long_description=readme,
    url='https://github.com/trustpilot/python-authenticated-encryption',
    packages=['trustpilot_authenticated_encryption'],
    package_dir={'trustpilot_authenticated_encryption': 'trustpilot_authenticated_encryption'},
    include_package_data=True,
    install_requires=requirements,
)
