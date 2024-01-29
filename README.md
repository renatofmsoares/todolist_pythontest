# Welcome to my study area!

My goal here is to create a ToDo List system using in python using BDD.

I want that at the end of this project I can use it to demonstrate my experience with python in developing a web application using testing frameworks, automated scripts, integration with AWS, version control, documentation, database testing and integration with CI /CD.

### Current Application Overview:

- This to-do list application is being built using Flask, a Python web framework.
- BDD is being applied (Behavior Driven Development).
- The modules are being encapsulated using Blueprint.

### Current State:

- Basic routing and views for displaying and adding tasks have already been implemented.
- Tasks are stored in memory as a list (**`tasks`**) in the **`routes.py`** file, simulating a simple data layer.
- The application uses the Flask app factory pattern, and we have registered a blueprint for handling tasks (**`routes.py`**).

### Some difficulties encountered along the way:

I started this project using WSL (Windows Subsystem for Linux), but I faced some difficulties that were taking up a lot of my time so I decided to work directly on an Ubuntu operating system.

# Let's get this project running on your machine:

I will try to leave a step-by-step guide here so that you can download and run the project locally on your machine, but I will only focus on the instructions for Linux. (To users of other OS, I apologize!)

First of all, the project is being developed in Python. Let's start by installing 'pyenv'. It is a Python version management tool that allows you to easily install, manage, and switch between multiple versions of Python on your system.

## pyenv - python version management tool

```
# Step 1: Install Dependencies

sudo apt-get update
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# Step 2: Install pyenv
curl https://pyenv.run | bash

# Step 3: Add pyenv to your shell (Here we are using the bash shell). Copy the following commands to your '.bashrc':

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Reload your bashrc:
source ~/.bashrc

# Step 4: Install Python versions using pyenv

pyenv install 3.12.1

# Step 5: Set Global and Local Python Versions

pyenv global 3.12.1

# Step 6: Set a local Python version for a specific project (run this command in the project directory):

pyenv local 3.12.1
```

## Creating our virtual environment:
```
pyenv virtualenv 3.12.1 venv
pyenv activate venv
```

## Installing our dependencies:
```
pip install -r requirements.txt
```
Now, as the next step, to run our Seleninum tests we will need a webdrive available. Let's configure it now.

## Install a WebDriver (e.g., ChromeDriver)

```
# Selenium requires a WebDriver to interact with web browsers. For Chrome, you can use ChromeDriver.

# Download ChromeDriver:
# Visit the ChromeDriver downloads page.
# Download the version corresponding to your Chrome browser version.
# Extract the downloaded ZIP file.

### Add ChromeDriver to PATH:

# On Linux or macOS, you can move the chromedriver executable to a directory in your PATH:

sudo mv /path/to/chromedriver /usr/local/bin/

# On Windows, you can add the directory containing 'chromedriver.exe' to your system's PATH.
```

After installation, you can verify that Behave and Selenium are installed correctly:

```
# Check Behave version
behave --version

# Check Selenium version
python -c "import selenium; print(selenium.__version__)"
```

If everything is set up correctly, you should see the versions of Behave and Selenium without any errors.

### Commands to run our application:

```
# If you are not inside the virtual environment, you need to activate:
pyenv activate venv

# Install dependencies
pip install -r requirements.txt

# Run the application:
python run.py
```

Open your browser and go to http://127.0.0.1:5000/ to view the to-do list application.

### Run the behave tests
```
behave -t ~ForFutureImplementation
```
