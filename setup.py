import os

from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as _f:
        return _f.read()


setup(
    author="Benjamin Staneck",
    author_email="staneck@gmail.com",
    description="Custom HTML anchor slogs for Python-Markdown",
    install_requires=["Markdown~=3.0"],
    keywords="markdown html anchor slug",
    license="MIT",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    name="pymdown-custom-slugs",
    py_modules=["pymdown-custom-slugs"],
    python_requires=">=3.6",
    version=0.0.1",
    url="https://github.com/Stanzilla/pymdown-custom-slugs",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)