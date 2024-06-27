import requests
import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_repositories(query, sort, order, per_page, max_pages, language=None, created_after=None, updated_after=None):
    repositories = []
    for page in range(1, max_pages + 1):
        url = f'https://api.github.com/search/repositories?q={query}'
        if language:
            url += f'+language:{language}'
        if created_after:
            url += f'+created:>{created_after}'
        if updated_after:
            url += f'+pushed:>{updated_after}'
        url += f'&sort={sort}&order={order}&per_page={per_page}&page={page}'

        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(url, headers=headers)

        if response.status_code == 403:
            logging.error('Error: %s - %s', response.status_code, response.json().get('message', ''))
            break
        elif response.status_code != 200:
            logging.error('Failed to fetch repositories: %s', response.status_code)
            break

        data = response.json()
        repositories.extend(data.get('items', []))
        if 'items' not in data or len(data['items']) == 0:
            break

    logging.info('Fetched %d repositories', len(repositories))
    return repositories

def save_to_csv(repositories, output_file):
    if not repositories:
        logging.info('No repositories found.')
        return

    # Επιλέγουμε μόνο τα απαραίτητα πεδία για το πρώτο φύλλο
    filtered_repos = [
        {
            'name': repo['name'],
            'owner': repo['owner']['login'],
            'created_at': repo['created_at'],
            'language': repo['language']
        }
        for repo in repositories
    ]

    # Αποθήκευση του πρώτου φύλλου
    with open(output_file, 'w', newline='', encoding='utf-8') as output:
        writer = csv.DictWriter(output, fieldnames=filtered_repos[0].keys())
        writer.writeheader()
        writer.writerows(filtered_repos)

    logging.info('Successfully saved filtered repositories to %s', output_file)

    # Αποθήκευση όλων των δεδομένων στο δεύτερο φύλλο
    all_headers = repositories[0].keys()
    with open(output_file.replace('.csv', '_all.csv'), 'w', newline='', encoding='utf-8') as output_all:
        writer = csv.DictWriter(output_all, fieldnames=all_headers)
        writer.writeheader()
        writer.writerows(repositories)

    logging.info('Successfully saved all repositories to %s', output_file.replace('.csv', '_all.csv'))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GitHub Repository Scraper')
    parser.add_argument('--description', required=True, help='Search query for repository description')
    parser.add_argument('--sort', choices=['stars', 'forks', 'updated'], default='stars', help='Sort by stars, forks, or updated')
    parser.add_argument('--order', choices=['asc', 'desc'], default='desc', help='Order by ascending or descending')
    parser.add_argument('--per_page', type=int, default=10, help='Results per page (max 100)')
    parser.add_argument('--max_pages', type=int, default=10, help='Maximum number of pages to fetch')
    parser.add_argument('--language', help='Programming language of the repositories')
    parser.add_argument('--created_after', help='Filter repositories created after this date (YYYY-MM-DD)')
    parser.add_argument('--updated_after', help='Filter repositories updated after this date (YYYY-MM-DD)')
    parser.add_argument('--output', required=True, help='Output CSV file')

    args = parser.parse_args()

    repositories = fetch_repositories(args.description, args.sort, args.order, args.per_page, args.max_pages, args.language, args.created_after, args.updated_after)
    save_to_csv(repositories, args.output)
