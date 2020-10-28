# Push To Git
Simple application that allows the user to automatically push data to staging and production branches


![Python 3](https://img.shields.io/badge/Python-Python3-yellowgreen "Python 3")


![PySide2](https://img.shields.io/badge/PySide2-Qt%20for%20Python-blue "PySide2")


## UI Preview
***
<img src="/images/push_to_git_img.png" alt="push to git ui screenshot" width="600"/>

## Installation for Mac
---
- Clone this repo to your local drive
- Start up Terminal
- Inside the repo create a virtual environment by typing `python3 -m venv venv`
- Start the virtual environment by typing `source ./venv/bin/activate`.  You should see the words `venv` prefixed in your terminal
- Install the required packages from the provided requirements file by typing `pip install -r requirements.txt`
- Still inside the repo and with the virtual environment activated type `python px_to_rem.py`
- Application should initialize

## Usage
---
- Add a git repository locaton by clicking File >> Add Repo Location
- The repository will de displayed in the dropdown/combobox that says Pick a Stored Location
- Pick either Master >> Staging or Staging >> Production
- The buttons will pass all commits from the current branch to the requested branch and create a back-up branch.  Eg Master to Staging will push all commits from Master into the Staging Branch
