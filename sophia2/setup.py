import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sophia2",
    version="0.0.1",
    description="Python library for news dircourse analysis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Team Sophia2",
    author_email="sophia2.uach@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sophia2"],
    #include_package_data=True, #permite agregar archivos que no son codigo en el MANIFEST.in
    install_requires=["pandas"],
    #entry_points={
    #    "console_scripts": [
    #        "realpython=reader.__main__:main",
    #    ]
    #},
)