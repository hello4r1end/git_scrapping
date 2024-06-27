# GitHub Repository Scraper

This project is a GitHub repository scraper that allows users to search for repositories based on specific criteria, save the results to an Excel file with two sheets (one with filtered data and one with full data), and view a web-based frontend to initiate searches.

## Features

- Search GitHub repositories based on description, language, creation date, update date, and more.
- Save search results to an Excel file with two sheets:
  - **Filtered Repositories:** Includes selected fields such as name, owner, creation date, and language.
  - **Full Repositories:** Includes all available repository fields.
- Web-based frontend for easy search and download of results.

## Requirements

- Python 3.7+
- Flask
- Requests
- OpenPyXL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/git_scrapping.git
   cd git_scrapping
