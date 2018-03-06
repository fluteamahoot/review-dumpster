[![Build Status](https://travis-ci.org/fluteamahoot/review-dumpster.svg?branch=master)](https://travis-ci.org/fluteamahoot/review-dumpster)

# Review

Review is code that powers [reviews.thedumpster.party][2]. It is built with [Python][0] using the [Django Web Framework][1]. It is not in a working state yet.

This project has the following basic apps:

* Profile: Manages addition account information
* Review: Handles the CRUD of the reviews

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv venv`
    2. `$ . venv/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://reviews.thedumpster.party/
