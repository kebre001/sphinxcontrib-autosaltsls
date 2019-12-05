import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sphinxcontrib-autosaltsls',
    version='0.1.2',
    packages=['sphinxcontrib.autosaltsls'],
    include_package_data=True,
    license='Apache 2',
    description='Sphinx auto-document generator for SaltStack sls files',
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://bitbucket.tools.ficoccs-dev.net/projects/DEVOPS/repos/ccs-standard-templates/browse',
    author='John Hicks',
    author_email='johnhicks@fico.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Documentation',
    ],
    install_requires=[
        'Jinja2',
        'sphinx>=2.0.0'
    ],
)
