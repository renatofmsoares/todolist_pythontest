# Welcome to my study area!

## Install a WebDriver (e.g., ChromeDriver)

Selenium requires a WebDriver to interact with web browsers. For Chrome, you can use ChromeDriver.

Download ChromeDriver:
Visit the ChromeDriver downloads page.
Download the version corresponding to your Chrome browser version.
Extract the downloaded ZIP file.

### Add ChromeDriver to PATH:

On Linux or macOS, you can move the chromedriver executable to a directory in your PATH:

```
sudo mv /path/to/chromedriver /usr/local/bin/
```

On Windows, you can add the directory containing 'chromedriver.exe' to your system's PATH.

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
# Activate the virtual environment
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application:
python run.py
```

Open your browser and go to http://127.0.0.1:5000/ to view the to-do list application.
