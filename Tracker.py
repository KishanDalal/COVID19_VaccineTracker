import requests
from bs4 import BeautifulSoup

# URL get function 
def getdata(url):
  r = requests.get(url)
  r.raise_for_status()  # Raise an error for bad responses
  return r.text

# URL getdata functionand convert that data into HTML code
htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')
# Extract the data from the HTML code
res = soup.find_all('div', class_='is_h5-2 is_developer w-richtext')
print(str(res))
