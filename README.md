# Description

Python semi-automatic package building script

## How to

### Cloning project from a repo

1. Edit the ```./templates/setup.py``` with your data and Add your LICENSE if you want to:
    - More for setting up at its official site [python-packaging](https://packaging.python.org/en/latest/)

2. Run the script like `./build my_remote_git_repo`
    - It will clone it and create your package at ```./cloned_package/dist/```

Now your project is ready to be deployed or used anywhere else you need to :)

### Future updates - TODOs

- [ ] Creatre a windows-like script (or make it different)
- [ ] Make the process of setup.py automatic (cli for example)
- [ ] Automatic fetching a LICENSE or creating it
  - Download/scrape from [opensource.org](https://opensource.org/licenses/MIT)
  - Have some templates and make the subtitution using a cli
