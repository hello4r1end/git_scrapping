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
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Usage
Command Line Interface
You can run the scraper directly from the command line with the following command:

bash
Copy code
python github_scraper.py --description "port scanning" --sort stars --order desc --per_page 10 --max_pages 10 --language python --created_after 2020-01-01 --output output.xlsx
Web Frontend
Run the Flask app:

bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000.

Fill in the search criteria and submit the form to start scraping. The results will be saved to an Excel file and a download link will be provided.

Arguments
Command Line Arguments
--description: Search query for repository description (required).
--sort: Sort by stars, forks, or updated (default: stars).
--order: Order by asc (ascending) or desc (descending) (default: desc).
--per_page: Number of results per page (default: 10, max: 100).
--max_pages: Maximum number of pages to fetch (default: 10).
--language: Programming language of the repositories.
--created_after: Filter repositories created after this date (YYYY-MM-DD).
--updated_after: Filter repositories updated after this date (YYYY-MM-DD).
--output: Output Excel file name (required).
Example
bash
Copy code
python github_scraper.py --description "machine learning" --sort stars --order desc --per_page 20 --max_pages 5 --language python --created_after 2021-01-01 --output ml_repos.xlsx
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Acknowledgments
This project uses the GitHub API to fetch repository data.
