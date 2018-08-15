from flask import Flask
from flask import render_template
from flask import request
from flask import escape

app = Flask(__name__)


def log_request(req:'flask_request', res:str) -> None:
    """"Report requests and results in log file."""
    with open('search.log','a') as log:
        #print(str(dir(req)),res, file = log)
        #print(req.form, file=log, end='|')
        #print(req.remote_addr, file=log, end='|')
        #print(req.user_agent, file=log, end='|')
        #print(res, file=log, end='|')
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
    

@app.route('/search', methods = ['POST'])
def search_for_letters(phrase:str='life, the universe, and everything', letters:str='aeiou') -> set:
    """Search the chosen letters in the givin phrase."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(set(phrase).intersection(set(letters)))
    log_request(request,results)
    return render_template('results.html', the_results = results, the_phrase = phrase, the_letters = letters, the_title = title)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Entry page"""
    return render_template('entry.html', the_title = 'Welcome to search for letters on the web!')


@app.route('/results')
def results_page() -> 'html':
    """Result page."""
    return render_template('results.html', the_title = 'Here are your results:')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """View search log."""
    #with open('search.log','r') as log:
        #return escape(''.join(log.readlines()))
    contents=[]
    with open('search.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View log', the_row_title=titles, the_data=contents,)
    #return str(contents)

if __name__ == '__main__':
    app.run(debug=True)
