#!/usr/bin/env python
from setuptools import setup, find_packages
import versioneer

INSTALL_REQUIRES = ['intake >=0.6.6', 'msgpack', 'requests']

setup(
    name='intake-warning',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='warning plugin for Intake',
    url='https://github.com/observingClouds/intake-warning',
    maintainer='Hauke Schulz',
    license='BSD',
    py_modules=['intake_warning'],
    packages=find_packages(),
    entry_points={
        'intake.drivers': [
            'error = intake_warning.error:ErrorSource',
            'warning = intake_warning.error:WarningSource',
        ]
    },
    package_data={'': ['*.csv', '*.yml', '*.html']},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    zip_safe=False, )
