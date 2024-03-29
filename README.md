# nonogram
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Actions status](https://github.com/monpie3/nonogram/actions/workflows/django.yml/badge.svg)](https://github.com/monpie3/nonogram/actions)


This web application will be your go-to platform for generating logical puzzles for problem-solving. My aim is to create images that not only serve as puzzles but also convey meaningful representations once they are solved.

---
### Deployment

[DEMO](https://nonogram-hfdi.onrender.com/) 🚀


This project is deployed on [Render](https://dev.to/vincod/django-on-render-1g9a), with the database hosted on [Railway](https://dev.to/dennisivy11/easiest-django-postgres-connection-ever-with-railway-11h6).


---

### Launch Project Locally

It's highly recommended to use a virtual environment when working with third-party packages to ensure dependencies are managed effectively.

0. Virtual Environment Setup.

    For instructions on setting up a virtual environment, click [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments).

1. Repository Cloning.

    `git clone https://github.com/monpie3/nonogram.git`


2. Directory Change.

    `cd nonogram`

3. Package Installation.

* For the minimum set of packages required to run the project:

    `pip install -e .`

* For development purposes, including additional packages:

    `pip install -e .'[dev]'`

4. Environmental Variable Configuration.

    Rename `.env.template` to `.env` and fill in all the environmental variables.

5. Project Launch.

    `python manage.py runserver`


Project will run on http://127.0.0.1:8000/

---
### Key Features To Implement
- [ ] 🖼️ **Puzzle Generation and Solving:** Generate puzzles and solve them directly on the platform to sharpen your logical thinking skills.

- [ ] 🔍 **Hint Assistance:** Stuck on a puzzle? Request a hint to nudge you in the right direction.

- [ ] 🏆 **Hall of Fame:** Explore a showcase of solved challenges and celebrate your achievements.

- [ ] 📸 **Upload Your Puzzles:** Upload images of physical logic puzzles, whether it's a snapshot of a paper puzzle or a hand-drawn challenge. Seek hints or complete solutions along with detailed analyses.

---

### Used Technologies

[`tailwind`](https://tailwindcss.com/docs/) → CSS framework

[`daisyUI`](https://daisyui.com/docs/) → A component library for Tailwind CSS

[`three.js`](https://threejs.org/docs/) → 3D graphics JavaScript library

[`Django`](https://docs.djangoproject.com/) → Python web framework

[`Django REST Framework`](https://www.django-rest-framework.org/) → Toolkit for building REST APIs in Django

[`django-silk`](https://silk.readthedocs.io/en/latest/) → Profiling and monitoring tool for Django

[`drf-spectacular`](https://drf-spectacular.readthedocs.io/en/latest/) → Automated API Documentation for Django REST Framework

[`PostgreSQL`](https://www.postgresql.org/docs/) → Open-source relational database system

[`GitHub Actions`](https://docs.github.com/en/actions) & [`Pre-Commit`](https://pre-commit.com/) → Used for testing and linting
