from flask import Flask, render_template

from elsa import cli


app = Flask('naucsepythoncz')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    cli(app, base_url='https://fedoralovespython.org')
