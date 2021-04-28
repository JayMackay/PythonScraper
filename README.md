# Python Raw Data Cleaner

This script takes raw data from an unformatted csv file which was scraped using an external Node module, in turn formatting the required relevant information.

To view the TikTok module visit:
https://github.com/drawrowfly/tiktok-scraper

To submit bug reports, feature suggestions, or track changes:
https://github.com/JayMackay/PythonScraper

### Contents Of This File

* Requirements
* Recommended modules
* Installation
* Configuration
* Troubleshooting
* Maintainers

### Requirements

This project is built using Python version 3.9.4 through VS Code. The framework requires the following Node package to run:

```
npm i -g tiktok-scraper
```

### Recommended Modules

Node.js version 14.16.1:
https://nodejs.org/en/download/ 

### Installation

To run ensure you have the latest version of VS Code and have installed the Node TikTok Scraper module using the previously mentioned command line. Clone the project from the GitHub repository using the “Clone from Github” option within VS Code and input the repository URL.

### Configuration

Once you have the TikTok scraper installed run the following command within the VS Code terminal to scrape your raw initial data:

*Note: Edit the filepath command to a directory of your choice
```
tiktok-scraper trend -n 10 --filepath /Users/username/source/repos/TikTokScraper -t csv -f tiktokdata
```

This utilizes the TikTok Scraper module and finds the top 10 trending videos, saving the data to a raw csv file. Run the following command in order to clean the data in a more usable format:

```
python parse.py -i tiktokdata.csv -o outputfile.csv
```

### Troubleshooting

There is a current issue regarding scraping specific hashtags or userdata using the TikTok scraper. This is a work in progress.

## Authors

Jared Mackay - https://github.com/JayMackay