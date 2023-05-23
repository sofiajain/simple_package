import setuptools

with open("README.md",'r') as f:
    long_description = f.read()

setuptools.setup(
    name="simplepackage",
    version="0.2",
    author="Jose Toledo",
    author_email="toledo60@protonmail.com",
    description="Simple Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['numpy','pandas','matplotlib'],
    url="https://github.com/toledo60/simple_package",
    project_urls={
        "Bug Tracker": "https://github.com/toledo60/simple_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)