from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).absolute().parent
with open(here / "README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="human-dates2",
    version="1.0.1",
    description="Dates for humans",
    long_description=long_description,
    url="https://github.com/AleCandido/human_dates",
    author="Alessandro Candido",
    author_email="candido.ale@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="datetime pretty-print human-readable",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["sphinx", "alabaster", "recommonmark", "sphinxcontrib-bibtex",],
    setup_requires=["wheel"],
    project_urls={
        "Original SO": "http://stackoverflow.com/a/1551394/192791",
        "Original Package": "https://pypi.org/project/human_dates/0.1.0/",
    },
)
