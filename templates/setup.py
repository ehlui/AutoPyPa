import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MY_PACKAGE",
    version="0.0.1",
    author="Luis Luisito",
    author_email="",
    description="Supa dupa mix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ehlui",
    project_urls={
        "Bug Tracker": "https://github.com/ehlui",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
