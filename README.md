# COVID-19 Vaccine Tracker

## Overview
This project is a simple web scraping script that extracts and displays information about COVID-19 vaccine development from an archived version of the Milken Institute's COVID-19 tracker website. The script uses Python's `requests` library to fetch the webpage and `BeautifulSoup` from the `bs4` library to parse and extract relevant data.

## What I Have Learned
Through this project, I have gained the following insights and skills:

1. **Web Scraping Basics**:
   - Learned how to use the `requests` library to fetch HTML content from a webpage.
   - Understood how to handle HTTP errors using `raise_for_status()` to ensure robust error handling.

2. **HTML Parsing with BeautifulSoup**:
   - Learned how to parse HTML content using `BeautifulSoup` and extract specific elements using CSS class selectors.
   - Understood how to navigate and manipulate HTML elements to extract meaningful data.

3. **Data Extraction and Processing**:
   - Learned how to iterate through extracted HTML elements and clean the text content using `.text.strip()`.

4. **Error Handling and Debugging**:
   - Understood the importance of validating data (e.g., checking the length of lists) to avoid runtime errors.
   - Learned how to debug issues related to web scraping, such as handling changes in webpage structure or missing elements.

5. **Working with Archived Data**:
   - Learned how to use the Wayback Machine to access archived versions of websites when live data is unavailable.

## Goals
The goals of this project are as follows:

1. **Data Extraction**:
   - Successfully extract and display information about COVID-19 vaccine development from the archived webpage.

2. **Automation**:
   - Automate the process of fetching and parsing data to make it reusable for similar tasks in the future.

3. **Error Handling**:
   - Implement robust error handling to ensure the script can handle unexpected issues, such as changes in webpage structure or network errors.

4. **Scalability**:
   - Make the script flexible enough to handle additional data sources or different webpage structures with minimal modifications.

5. **Learning and Growth**:
   - Use this project as a stepping stone to explore more advanced web scraping techniques, such as handling JavaScript-rendered content or working with APIs.

## How It Works
1. The script fetches the HTML content of the archived webpage using the `requests` library.
2. It parses the HTML content using `BeautifulSoup` to create a structured representation of the webpage.
3. The script searches for specific HTML elements (`div` tags with the class `is_h5-2 is_developer w-richtext`) and extracts their text content.
4. The extracted data is printed to the console in a numbered format.

## Prerequisites
- Python 3.9 or higher
- Libraries: `requests`, `beautifulsoup4`

## How to Run
1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4

![image](https://github.com/user-attachments/assets/ae46abec-cb7d-4f55-9ac9-b671132325b1)

![image](https://github.com/user-attachments/assets/3e3c1195-6b65-48b0-ae98-07d8ebe96315)
