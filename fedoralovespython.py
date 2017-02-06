import textwrap

import jinja2
import yaml
from flask import Flask, render_template
from markdown import markdown


app = Flask('fedoralovespythonorg')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    points = read_yaml('points.yml')
    points = [p for p in points if p.get('ready', True)]
    return render_template('index.html', points=points)


@app.route('/__future__/')
def future():
    points = read_yaml('points.yml')
    return render_template('index.html', points=points)


@app.template_filter('markdown')
def convert_markdown(text):
    text = textwrap.dedent(text)
    result = jinja2.Markup(markdown(text))
    return result


def read_yaml(filename):
    with open(filename, encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

# to serve with Flask server: FLASK_APP=fedoralovespython.py python3 -m flask run
if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='https://fedoralovespython.org')
