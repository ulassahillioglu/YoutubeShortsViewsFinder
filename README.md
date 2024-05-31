YouTube Shorts Views Finder
This repository contains a Python script to scrape and extract the number of views from a YouTube Shorts video page. The script uses the requests library to fetch the HTML content of the page and the BeautifulSoup library to parse the HTML. A regular expression is used to find the number of views from the parsed HTML content.

Requirements
To run this script, you need to have the following Python packages installed:

requests
beautifulsoup4
You can install these packages using pip:

sh
Copy code
pip install requests beautifulsoup4
Usage
Clone the repository to your local machine:
sh
Copy code
git clone https://github.com/ulassahillioglu/YoutubeShortsViewsFinder.git
cd YoutubeShortsViewsFinder
Create a new Python script or use the existing script provided in the repository. The script should look like this:
python
Copy code
import requests as rq
from bs4 import BeautifulSoup as bs
import re

# URL to be scraped
pattern = r'"views":{"simpleText":"(\d+[.]?\d+ \w+)"}'

url = input("Enter the URL: ")

# Make a GET request to fetch the raw HTML content
html_content = rq.get(url).text

# Parse the HTML content
soup = bs(html_content, "html.parser")

# Find the number of views using regular expression
matches = re.findall(pattern, soup.prettify())

if matches:
    print("Number of views:", matches[0])
else:
    print("Views not found")

# Uncomment the following lines if you want to save the HTML content to a file
# with open("shorts.html", "w", encoding="utf-8") as f:
#     f.write(soup.prettify())
Run the script:
sh
Copy code
python script.py
Enter the URL of the YouTube Shorts video when prompted. The script will output the number of views for the video.
Additional Information
The script uses a regular expression pattern to search for the views count in the HTML content. The pattern is designed to match the specific structure of the YouTube Shorts page.

The script includes an option to save the fetched HTML content to a file. This can be useful for debugging or further analysis. Uncomment the relevant lines in the script to enable this feature.

Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
This script makes use of the following Python libraries:

Requests
BeautifulSoup
We thank the developers of these libraries for their hard work and contributions to the open-source community.
