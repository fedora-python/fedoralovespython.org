import jinja2
import yaml
from elsa import cli
from flask import Flask, render_template
from glob import iglob
from markdown import markdown


app = Flask('fedoralovespythoncz')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    points = read_yaml('points.yml')
    return render_template('index.html', points=points)


@app.template_filter('markdown')
def convert_markdown(text):
    result = jinja2.Markup(markdown(text))
    return result


def read_yaml(filename):
    with open(filename, encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data


if __name__ == '__main__':
    cli(app, base_url='https://fedoralovespython.org')
