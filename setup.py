#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup, find_packages

setup(
    name="distortopia",
    version="0.1",
    author="Riya Rampalli",
    author_email="rr3491@columbia.edu",
    license="GPLv3",
    description="A tool for simulating F1 hybrids and detecting segregation distortion from VCF files.",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
        "biopython",
        "pandas",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            "distortopia = distortopia.__main__:main"
        ]
    },
)
