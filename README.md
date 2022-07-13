# Description

Python semi-automatic package building script

## How to

A minimal __setup.py__

```py
setup(
    name='MyPackageName',
    version='1.0.0',
    description='Description of my package',

    py_modules=["mymodule"] # Single modules project,
    package_dir={"":"src"} # Telling setuptools our code is in ./src directory
)
```

### Cloning project from a repo

1. Edit the ```./templates/setup.py``` with your data and Add your LICENSE if you want to:
    - More for setting up at its official site [python-packaging](https://packaging.python.org/en/latest/)

2. Run the script like `./build my_remote_git_repo`
    - It will clone it and create your package at ```./cloned_package/dist/```

Now your project is ready to be deployed or used anywhere else you need to :)

## Useful files - For more accurate behaviour

```
templates
    MANIFEST.in
    setup.py
    README.md
    ...
```

1. __[OPTIONAL]__ Edit the MANIFEST.in with the includes,excludes you need.

- If you happen to use MANIFEST.in you better add it in the __line 56__ from the __build__ script to enable the  copy of this file for packaging.

__Example of MANIFEST.in__

```md
include src/my_package/main.py
include src/my_package/requirements.txt
recursive-include src/my_package/libs *
recursive-exclude src/my_package/tests *
recursive-exclude .DS_Store *
```

2. __[OPTIONAL]__ pyproject.toml for telling which backend build system we're using.

    - More at [setuptools - toml](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use)

### Future updates - TODOs

- [ ] Creatre a windows-like script (or make it different)
- [ ] Make the process of setup.py automatic (cli for example)
- [ ] Automatic fetching a LICENSE or creating it
  - Download/scrape from [opensource.org](https://opensource.org/licenses/MIT)
  - Have some templates and make the subtitution using a cli
