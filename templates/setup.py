from setuptools import find_namespace_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="project-name",
    version="0.0.1",
    author="ehLui",
    description="My super package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ehlui",
    project_urls={
        "Documentation": "DOCUMENTATION_URL",
        "Source": "SOURCE_CODE_VCS",
    },
    classifiers=[  # More classifiers at :  https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    packages=find_namespace_packages(  # Python >=3 does not need __init__ in the root/any package
        where="src",
        include=["package.to-be-included"],
        exclude=["package.to-be-excluded"],
    ),
    py_modules=["my_module_a"],  # -> Modules to be add individually
    package_dir={"": "src"},  # Where our package relies on
    install_requires=[
        # "requests>=2.28" If you project need any dependency which need to be installed
        # along with the package
    ],
)
