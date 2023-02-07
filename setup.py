import setuptools

with open("aphos_openapi/aphos_openapi_README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aphos_openapi",                     # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="Pavel Kinc",                     # Full name of the author
    description="Test",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    install_requires=[]                     # Install other dependencies if any
)