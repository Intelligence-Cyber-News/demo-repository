# Household Chore Tracker

A small Django app for tracking shared household chores: log when a
chore was done, and see which ones are overdue based on their expected
interval.

See [`_docs/plan.md`](_docs/plan.md) for the full scope and
[`_docs/backlog.md`](_docs/backlog.md) for the implementation backlog.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (or plain `pip` — see below)

## Setup

Install dependencies:

```sh
uv pip install -r requirements.txt
```

Apply database migrations:

```sh
uv run python manage.py migrate
```

## Running

Start the development server:

```sh
uv run python manage.py runserver
```

Then visit http://localhost:8000/.

## Testing

```sh
uv run python manage.py test
```

## Without uv

Any step above also works with a plain virtualenv and `pip`:

```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
