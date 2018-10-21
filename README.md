# Team24
Source code for the Team 24 website

Our website: https://cscc01.github.io/Team24/index.html

# Latest updates
- 2018.10.15 Started sprint 1.
- 2018.10.15 Deliverable two, containing user stories and personas is now available on our website.
- 2018.09.26 Our team website is up and running!

# Development setup

## Setup

Note: This project *requires* Python 3.6+, Docker and Docker Compose installed. For Mac users, ensure you are using the correct version of Python because the OS preinstalls Python 2.7 and default `pip` and `python` commands execute in v2.7 rather than v3.x.

If you don't have Python 3 installed on your Mac, you can install [Homebrew](https://brew.sh/) and run `brew install python3` on your terminal.

1. Create a virtual environment for the project and activate it. Run `pip3 install virtualenv` if virtualenv is not installed on Python3.6+
```
$ virtualenv team24-venv --python=/usr/local/bin/python3
$ source team24-venv/bin/activate
```

2. Clone the repository to your directory
```
(team24-venv) $ git clone git@github.com:CSCC01/Team24.git
(team24-venv) $ cd Team24
```

3. Install the required dependencies
```
(team24-venv) $ pip install -r app/requirements.txt
```

4. Spin up the Dockerized databases.
```
(team24-venv) $ docker-compose up -d
```

5. If using PyCharm as the IDE, set the Project Interpreter as the Python from your venv
    - PyCharm -> Preferences -> Project -> Project Interpreter
    - Settings (gear icon) -> Add
    - Select "Existing Interpreter"
    - Look for Python3.x in `team24-venv/bin/python3.x`

## How to run locally
1. Make sure you are in your virtualenv that you setup
```
$ source team24-venv/bin/activate
```
2. Start server
```
$ FLASK_APP=app/app.py flask run
```
3. You should now able to access the server
```
http://localhost:5000
```

## Accessing databases
- icare_data: `localhost:5433`

## Resetting databases
1. Remove database volumes attached to docker-compose
```
$ docker-compose -f docker-compose-dev.yml down -v
```
2. Restart the database containers to get a fresh database
```
$ docker-compose -f docker-compose-dev.yml up -d
```

# Project structure
- Deliverable One - `deliverable-one` branch
- Deliverable Two - `deliverable-two` branch
- Our current website - `gh-pages` branch
- The product releases - `master` branch
