## fedoralovespython.org

A little webpage that shows why Fedora is a good operating system for
programmers, analysts, teachers, learners, and other people using Python.

It contains some talking points, each with a link to more information.


## How it's deployed

For local development, you have two options:

* Inside a Python 3 [virtual environment]:

        python -m pip install -r requirements.txt
        python fedoralovespython.py serve

* Alternately, with Fedora's system packages:

        sudo dnf install -y python3-flask python3-markdown python3-PyYAML
        FLASK_APP=fedoralovespython.py python3 -m flask run

The deployment at fedoralovespython.org uses [Elsa] to publish to GitHub Pages.


## Who made it

Made by people who maintain (or are interested in) Python in Fedora.
If you want to join, just send a pull request, or look at the
[Fedora Python SIG] page for more info.


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
[CC BY-SA]: https://creativecommons.org/licenses/by-sa/4.0/legalcode
[Fedora Python SIG]: https://fedoraproject.org/wiki/SIGs/Python
[MIT]: https://github.com/lancaster-university/microbit-docs/blob/master/LICENSE
