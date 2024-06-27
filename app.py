from flask import Flask, render_template, request, redirect, url_for
import logging
from github_scraper import fetch_repositories, save_to_csv

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        sort = request.form['sort']
        order = request.form['order']
        per_page = int(request.form['per_page'])
        max_pages = int(request.form['max_pages'])
        language = request.form['language']
        created_after = request.form['created_after']
        updated_after = request.form['updated_after']
        output = 'output.csv'
        
        repositories = fetch_repositories(description, sort, order, per_page, max_pages, language, created_after, updated_after)
        save_to_csv(repositories, output)
        
        return redirect(url_for('download_file', filename=output))
    return render_template('index.html')

@app.route('/downloads/<filename>')
def download_file(filename):
    return f"Download the file <a href='/static/{filename}'>here</a>."

if __name__ == '__main__':
    app.run(debug=True)
