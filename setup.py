from setuptools import setup, find_packages

with open("README.md", "r") as read_me:
    long_description = read_me.read()


setup(
    name="TRACE Institutional Repository Work Types",
    description="docs explaining the Work Types we want in our institutional repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    author="Mark Baggett",
    author_email="mbagget1@utk.edu",
    maintainer_email="mbagget1@utk.edu",
    url="https://github.com/markpbaggett/utk_dc_content_models",
    packages=find_packages(),
    extras_require={
        "docs": [
            "sphinx >= 4.3.2",
            "sphinx-rtd-theme >= 1.0.0",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
    keywords=["libraries", "preservation", "digital repositories", "documentation"],
)