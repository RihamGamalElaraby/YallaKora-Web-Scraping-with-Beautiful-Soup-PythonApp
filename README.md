YallaKora Match Scraper
This Python script scrapes match details from YallaKora's match center for a given date and saves the data in a CSV file.

Features
Input Date: Prompts the user to enter a date in MM/DD/YY format.
Web Scraping: Uses requests to fetch the webpage and BeautifulSoup to parse the HTML content.
Match Details Extraction: Extracts details of matches such as championship title, teams, match time, and score.
CSV Output: Saves the extracted match details in a CSV file named yallakora.csv.
Dependencies
requests: For sending HTTP requests to fetch the webpage.
beautifulsoup4: For parsing HTML content.
lxml: XML and HTML parsing library used by BeautifulSoup.
