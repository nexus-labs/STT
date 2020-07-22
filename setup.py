import os
import platform
import sys
from pathlib import Path

from pkg_resources import parse_version
from setuptools import find_packages, setup

def _requires_from_file(filename):
    return open(filename).read().splitlines()

def main():
    version_file = Path(__file__).parent / 'VERSION'
    with open(str(version_file)) as fin:
        version = fin.read().strip()

    setup(
        name='deepspeech_training',
        version=version,
        description='Training code for mozilla DeepSpeech',
        url='https://github.com/mozilla/DeepSpeech',
        author='Mozilla',
        license='MPL-2.0',
        # Classifiers help users find your project by categorizing it.
        #
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Topic :: Multimedia :: Sound/Audio :: Speech',
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Programming Language :: Python :: 3',
        ],
        package_dir={'': 'training'},
        packages=find_packages(where='training'),
        python_requires='>=3.5, <4',
        install_requires=_requires_from_file('requirements.txt'),
        # If there are data files included in your packages that need to be
        # installed, specify them here.
        package_data={
            'deepspeech_training': [
                'VERSION',
                'GRAPH_VERSION',
            ],
        },
    )

if __name__ == '__main__':
    main()
