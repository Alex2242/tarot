import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tarot-pkg-ensta-agile-project", # Replace with your own username
    version=os.getenv("TRAVIS_TAG", "0.0.1"),
    author="ensta-agile-project",
    author_email="author@example.com",
    description="A small tarot game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ensta-agile-project/tarot",
    packages=setuptools.find_packages(include=("game", "ui",)),
    classifiers=[
        "Python :: 3",
        "License :: MIT License",
    ],
    python_requires='>=3.6',
)
