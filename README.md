## [fedoralovespython.org]

A little webpage that shows why Fedora is a good operating system for
programmers, analysts, teachers, learners, and other people using Python.

It contains some talking points, each with a link to more information.


## Who made it

Made by people who maintain (or are interested in) Python in Fedora.
If you want to join, just send a pull request, or look at the
[Fedora Python SIG] page for more info.


## How it works

The website is powered by [Elsa]. That means it is a Flask website that
produces static HTML pages. Those pages are pushed to [GitHub Pages].
[Cloudflare] is used for [Let's Encrypt HTTPS].

When you push some changes, the Flask website is frozen by Elsa on [Travis CI].
When the commit is from the `master` branch, the frozen HTML site is pushed to
the `gh-pages` branch and the cache is purged on Cloudflare.
Feel free to explore `.travis.yml` to see how it's done.

The content if mainly in the `points.yml` file (as in talking points).
It's a YAML file with Markdown. `fedoralovespython.py` defines what's done with
the content and files in `templates` and `static` define the form.

## Hacking

For local development, you have two options:

* Inside a Python 3 [virtual environment]:

        python -m pip install -r requirements.txt
        python fedoralovespython.py serve

* Alternately, with Fedora's system packages:

        sudo dnf install -y python3-flask python3-markdown python3-PyYAML
        FLASK_APP=fedoralovespython.py python3 -m flask run

The above commands will serve the website locally;
in case you want to test freezing, use the virtual environment option and run:

    python fedoralovespython.py freeze --serve

That command will freeze the site and then serve it locally from the static
files.

When doing pull requests it is very helpful to show us the result online.
Especially if you are chnaging anything but content.
You can do it by deploying your changes to your fork's GitHub Pages:

    python fedoralovespython.py deploy --no-push --no-cname

The above command will freeze the site, and commit it frozen to your `gh-pages`
branch (be careful though because it will rewrite the branch's history).
Then you can push the branch to your fork on GitHub as you would push the
branch with your changes, except you might need to use `--force`.

*If you happen to have push permissions to the original `fedora-python`
repository, never deploy the site from your computer, let the automatic
machinery do it instead.*

The `--no-cname` option makes sure your deployed site won't redirect back to
[fedoralovespython.org].

Once pushed, your website should live online on the following URL,
where `<github-username>` is a placeholder for your GitHub username:

    http://<github-username>.github.io/fedoralovespython.org

Please add this link to the Pull Request description so we can fast-check what
you've changed.


## License

This site is not affiliated with either the Fedora Project
or the Python Software Foundation.

The content, except for any trademarked logos or unless otherwise
noted, is licensed under [CC BY-SA] (by members of
[Fedora Python SIG]).

The micro:bit picture is *Copyright © 2016 British
Broadcasting Corporation*, licensed under [MIT].

All product names, logos, and brands are property of their
respective owners.



[virtual environment]: https://docs.python.org/3/library/venv.html
[Fedora Python SIG]: https://fedoraproject.org/wiki/SIGs/Python
[Elsa]: https://github.com/pyvec/elsa
[GitHub Pages]: https://pages.github.com/
[Cloudflare]: https://www.cloudflare.com/
[Let's Encrypt HTTPS]: https://letsencrypt.org/
[Travis CI]: https://travis-ci.org/
[fedoralovespython.org]: https://fedoralovespython.org/
[CC BY-SA]: https://creativecommons.org/licenses/by-sa/4.0/legalcode
[Fedora Python SIG]: https://fedoraproject.org/wiki/SIGs/Python
[MIT]: https://github.com/lancaster-university/microbit-docs/blob/master/LICENSE
