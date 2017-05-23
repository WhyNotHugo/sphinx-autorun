#!/usr/bin/env python3

from setuptools import setup

setup(
    name='sphinx-autorun',
    url='https://github.com/hobarrera/sphinx-autorun',
    download_url='http://pypi.python.org/pypi/sphinx-autorun',
    license='BSD',
    author='Hugo Osvaldo Barrera',
    author_email='hugo@barrera.io',
    description='Sphinx extension autorun',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=[
        'sphinx_autorun'
    ],
    include_package_data=True,
    install_requires=[
        'Sphinx>=0.6',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    use_scm_version={
        'version_scheme': 'post-release',
        'write_to': 'sphinx_autorun/version.py',
    },
)
