# Description

Python package building semi-automatic :)

## How to

###  Without cloning project from a repo

1. Copy your python project to `./templates/src`

2. Copy your `'requirements.txt'` into `templates/src` (above your project level).

3. Edit the `./templates/setup.py` with your data

    - More for setting up at its official site [python-packaging](https://packaging.python.org/en/latest/)

4. Run the baby `./build` and let it build your package

5. Grab your package at `./core/dist/`

### Cloning project from a repo

1. Edit the `./templates/setup.py` with your data

2. Run the baby `./build my_remote_git_repo`
    - It will clone it, extract the requirements and copy to the path we need to and build the package.

3. Grab your package at `./core/dist/`
