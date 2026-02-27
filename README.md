# NoteNest Django

A simple Django CRUD notes app with Bootstrap UI. Users can create, view, edit, and delete notes using a SQLite database and Django messages for feedback.

## Repository Name

`notenest-django`

## Short Description

A beginner-friendly Django notes app demonstrating CRUD operations, routing, templates, and SQLite integration.

## Features

- Create notes with title and description
- List all saved notes on the home page
- Edit existing notes
- Delete notes
- Success/error alerts via Django messages

## Tech Stack

- Python
- Django 6
- SQLite
- Bootstrap 5
- Font Awesome

## Project Structure

```text
django/
|-- manage.py
|-- db.sqlite3
|-- project/
|   |-- settings.py
|   `-- urls.py
`-- app/
    |-- models.py
    |-- views.py
    |-- urls.py
    |-- templates/
    `-- static/
```

## Setup

1. Create and activate a virtual environment (optional if using existing `India/` env).
2. Install Django:

```bash
pip install django
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Open:

```text
http://127.0.0.1:8000/
```

## URL Endpoints

- `/` - home page (list + create form)
- `/about/` - about page
- `/save/` - save a note (POST)
- `/edit/<id>/` - edit note
- `/delete/<id>/` - delete note
- `/admin/` - Django admin

## Notes

- Database file is `db.sqlite3` in project root.
- Templates are under `app/templates/`.
- Static files are under `app/static/`.

## Future Improvements

- Register model in Django admin
- Add unit tests
- Use POST + confirmation for delete action
- Add authentication
- Add pagination/search
