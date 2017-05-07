# Django Admin: Basics and Beyond

From PyCon 2017, given by Kenneth Love

## Setup

This tutorial assumes Python 3.6. If you're using other versions, you'll have to change strings from f-strings to `.format()` calls. Other pieces may not work, either, without editing.

1. Download the project and put it somewhere you can find it later
2. Create a virtual environment with `python -m venv <venv name>`
3. Activate your virtual environment
4. Install the required packages with `pip install -r requirements.txt` while inside the project's directory
5. Check out the `start` tag for the project, this is where the tutorial will pick up (`git checkout start`)
6. Run `python manage.py migrate` to apply all migrations
7. Run `python manage.py createsuperuser` and create your user
8. Run `python manage.py generate_purchases 20` to add 20 purchases and all related records to your database

