from setuptools import setup
from Cython.Build import cythonize

setup(
    name="MyBot",
    ext_modules=cythonize(
        "Jack.py",
        compiler_directives={"language_level": "3"},
        annotate=False
    ),
)
