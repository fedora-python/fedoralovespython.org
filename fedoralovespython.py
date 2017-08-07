import textwrap

import jinja2
import yaml
from flask import Flask, Response, render_template, jsonify
from markdown import markdown
import ansicolor

app = Flask('fedoralovespythonorg')
app.config['TEMPLATES_AUTO_RELOAD'] = True


def read_points(hide_upcoming=True):
    points = read_yaml('points.yml')
    if hide_upcoming:
        points = [p for p in points if p.get('ready', True)]
    return points


@app.route('/')
def index():
    points = read_points()
    return render_template('index.html', points=points)


@app.route('/__future__/')
def future():
    points = read_points(hide_upcoming=False)
    return render_template('index.html', points=points)


@app.route('/index.txt')
def plaintext():
    points = read_points()
    return Response(
        render_template('index.txt', points=points, colors=NoColors()),
        mimetype='text/plain'
    )


@app.route('/index.term')
def terminal():
    points = read_points()
    return Response(
        render_template('index.txt', points=points, colors=ansicolor),
        mimetype='application/octet-stream'
    )


@app.route('/index.json')
def json():
    points = read_points()
    return jsonify(points)


@app.template_filter('markdown')
def convert_markdown(text):
    text = textwrap.dedent(text)
    result = jinja2.Markup(markdown(text))
    return result


@app.template_filter('term_indent')
def term_indent(text):
    text = textwrap.dedent(text)
    text = '    ' + text.strip().replace('\n', '\n    ')
    return text


@app.template_filter('apply')
def apply_color(text, color):
    """Apply the given colorizing function to text"""
    return color(text)


class NoColors:
    """No-op replacement for the "ansicolor" module"""
    def __getattr__(self, name):
        return lambda text: text


def read_yaml(filename):
    with open(filename, encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data


if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='https://fedoralovespython.org')
