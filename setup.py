#!/usr/bin/env python
from setuptools import setup, Extension
from Cython.Build import cythonize

import numpy


extensions = [
    Extension("*", ["src/pyoptools/**/*.pyx"],
        include_dirs=[numpy.get_include()],
        define_macros=[
            ("CYTHON_INLINE", "")
        ]
    ),
]
setup(
    ext_modules=cythonize(extensions, language_level="2"),
)
