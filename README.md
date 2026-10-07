# Django + Postgres API

A Django REST Framework API with token auth, the Django admin and a Postgres database.

[![Deploy on Naijacloud](https://img.shields.io/badge/Deploy%20on-Naijacloud-008751)](https://naijacloud.com/new?template=django-postgres-api&ref=template-django-postgres-api)

## Deploy

Click **Deploy** above, or open <https://naijacloud.com/new?template=django-postgres-api&ref=template-django-postgres-api>. Naijacloud builds it from this public repo and gives you a live HTTPS address. No GitHub connection needed; you can switch the service to your own fork later.

## What's inside

- Django 5.2 and Django REST Framework, with a `notes` resource: list, create, read and delete at `/api/notes/`
- Token auth for writes (reads are public), and the Django admin at `/admin/`
- Postgres through `DATABASE_URL`, static files through WhiteNoise, served by gunicorn
- The `Procfile` runs `migrate` and `collectstatic` before gunicorn starts, so every deploy is migrated

## Using the API

Create an admin user and a token from the service shell, then write with it:

```sh
python manage.py createsuperuser
python manage.py drf_create_token <username>

curl https://<your-app>.naijacloud.app/api/notes/
curl -X POST https://<your-app>.naijacloud.app/api/notes/ \
  -H "Authorization: Token <token>" -H "Content-Type: application/json" \
  -d '{"title": "First note"}'
```

## Environment variables

| Name | What it's for | Default |
| --- | --- | --- |
| `DATABASE_URL` | Postgres connection | Set by Naijacloud when the database is attached |
| `DJANGO_SECRET_KEY` | Signs sessions and tokens. Required | Generated on the deploy screen |
| `DJANGO_ALLOWED_HOSTS` | Hosts Django will answer, comma-separated | `.naijacloud.app,localhost,127.0.0.1` |
| `DJANGO_DEBUG` | Debug pages. Keep it off in production | `False` |

## Run it locally

```sh
git clone https://github.com/naijacloud/template-django-postgres-api
cd template-django-postgres-api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_DEBUG=True   # uses SQLite when DATABASE_URL is unset
python manage.py migrate
python manage.py runserver
```

## License

MIT
