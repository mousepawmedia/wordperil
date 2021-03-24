#!/usr/bin/env python3
from setuptools import find_packages, setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='wordperil',
    version='1.1.0',
    description='A party game for word nerds.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MousePaw Games',
    author_email='info@mousepawmedia.com',
    url='https://mousepawgames.com/wordperil',
    project_urls={
        'Bug Reports': 'https://phabricator.mousepawmedia.net',
        'Source': 'https://github.com/mousepawmedia/wordperil',
    },
    keywords='game, multiplayer, words',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Office/Business',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),

    include_package_data=True,

    python_requires='>=3.6, <4',
    install_requires=[
        'appdirs >= 1.4.3',
        'PySide2 >= 5.15.0'
    ],

    entry_points={
          'gui_scripts': [
              'wordperil = wordperil.__main__:main'
          ]
      }
)
