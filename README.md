YouTube Shorts Views Finder
This script fetches and extracts the view count of a YouTube Shorts video from its URL using web scraping techniques. It utilizes the requests library to fetch the raw HTML content of the page and BeautifulSoup for parsing the HTML. A regular expression is used to find the view count pattern in the parsed HTML.

Prerequisites
Ensure you have at least Python 3.8 installed on your system. You will also need the following Python libraries:

- requests
- beautifulsoup4

1)Clone the repository

```bash
git clone https://github.com/ulassahillioglu/YoutubeShortsViewsFinder.git
cd YoutubeShortsViewsFinder
```

2)Install the requirements
```bash
pip install requests beautifulsoup4
```

3)Run the script
```bash
python main.py
```
4)Enter the YouTube Shorts/Video URL when prompted

Explanation:
* Import Libraries: Imports necessary libraries (requests, beautifulsoup4, and re).
* Pattern for Views: Defines a regular expression pattern to find the view count in the HTML.
* URL Input: Prompts the user to input a YouTube Shorts video URL.
* Fetch HTML: Makes a GET request to fetch the HTML content of the provided URL.
* Parse HTML: Uses BeautifulSoup to parse the fetched HTML content.
* Find Matches: Uses re.findall to find all instances of the view count pattern.
* Display Result: Prints the first matched view count if available.

Additional Information
- Save HTML (Optional): Uncomment the provided lines to save the HTML content to a file for inspection

Contributing
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.

