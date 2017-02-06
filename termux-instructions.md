# fedoralovespython.org - Termux support
Fedora Loves Python website

# Problems
- pip doesn't work
- elsa not available as RPM

# Instructions

For running on an Android device:

- 1. Install Termux and Termux-Fedora from https://github.com/nmilosev/termux-fedora
- 2. Setup:
```
dnf update -y
dnf install -y git python3-flask python3-markdown python3-yaml

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

git clone https://github.com/fedora-python/fedoralovespython.org
cd fedoralovespython.org
```
- 3. You have to edit site.py (comment/remove these lines):
```
#L5
from elsa import cli

#L40
if __name__ == '__main__':
    cli(app, base_url='https://fedoralovespython.org')
```

- 4. Add at the end:
```
app.run()
```

- 5. Run the app:
```
$ python3 site.py
```
