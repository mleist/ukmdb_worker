#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup    # pylint: disable=E0401,E0611


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'python-decouple',
    'docopt',
    'schema',
    'celery>=3.1',
    'ukmdb_settings',
]

test_requirements = [
    'ukmdb_settings',
]

setup(
    name='ukmdb_worker',
    version='0.0.3',
    description="UKMDB Worker processes.",
    long_description=readme + '\n\n' + history,
    author="Markus Leist",
    author_email='markus@lei.st',
    url='https://github.com/mleist/ukmdb_worker',
    packages=[
        'ukmdb_worker',
    ],
    package_dir={'ukmdb_worker':
                 'ukmdb_worker'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='ukmdb worker',
    entry_points={
        'console_scripts': [
            'ukm_worker = ukmdb_worker.worker:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Topic :: Internet :: Log Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
