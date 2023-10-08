# Web Scraping Vacation Opportunities with Flask

This project is a web scraping application that scrapes vacation opportunities from the Polish portal wakacje.pl and generates reports. It allows you to configure search parameters using a web interface and schedule daily scraping tasks. For Scraping i am using Python libraries BeautifulSoup and Selenium.

# Getting Started

To run the project:

1. Clone the repository and install the required Python packages:

```
pip install -r requirements.txt
```
2. Set up the Flask app configuration in main.py.
3. Create the database and start the Flask app:
```
flask db init
flask db migrate
flask db upgrade
flask run
```
4. Access the web application at http://localhost:5000.

# Usage

Adding Search Parameters: Add search parameters such as country, date range, stay length, hotel stars, max price, transportation, amenities, and departure city via the web interface.

Scheduling and Running Scraping Tasks: Schedule scraping tasks to run automatically, or run them manually to collect vacation offers from wakacje.pl. Reports can be generated and emailed to selected recipients.

For email notification to work, 4 env variable need to be set up: Notification_email, Notification_receivers_email, Notification_pass, Notification_smtp_server. Names of the variable can be changed at email_notification.py
