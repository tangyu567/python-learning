from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/search', methods = ['POST'])
def search_for_letters(phrase:str='life, the universe, and everything', letters:str='aeiou') -> set:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(set(phrase).intersection(set(letters)))
    return render_template('results.html', the_results = results, the_phrase = phrase, the_letters = letters, the_title = title)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title = 'Welcome to search for letters on the web!')


@app.route('/results')
def results_page() -> 'html':
    return render_template('results.html', the_title = 'Here are your results:')

if __name__ == '__main__':
    app.run(debug=True)
