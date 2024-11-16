# LinkedIn Profile Image Scraper

This project is a simple Python script that logs into LinkedIn using your credentials and retrieves the profile image URL. The project uses Selenium for web scraping and logging for tracking execution.

## Features

- **Login to LinkedIn**: Automates the login process with your LinkedIn credentials.
- **Retrieve Profile Image URL**: Fetches the URL of your LinkedIn profile image.
- **Logging**: All actions and steps are logged in an `out.log` file to track the execution process.
- **Headless Browser**: The script uses Selenium in headless mode to avoid opening a visible browser window.

### Installation
```
git clone https://github.com/haldaniko/LinkedInAutoLogin-Script.git
cd LinkedInAutoLogin-Script

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

(Copy .env.sample to .env and populate it with all required data)

python main.py
```
