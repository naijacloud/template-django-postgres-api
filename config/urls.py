from pathlib import Path

from django.contrib import admin
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notes.views import NoteViewSet

router = DefaultRouter()
router.register("notes", NoteViewSet)


def healthz(_request):
    """200 when the app is up and can reach its database."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        db = "ok"
    except Exception:  # noqa: BLE001 - report, don't crash the probe
        db = "unreachable"
    return JsonResponse({"status": "ok" if db == "ok" else "degraded", "database": db},
                        status=200 if db == "ok" else 503)


# The page a browser gets at /. Every other client gets a JSON index.
WELCOME_PAGE = (Path(__file__).parent / "welcome.html").read_text(encoding="utf-8")


def index(request):
    if "text/html" in request.headers.get("Accept", ""):
        return HttpResponse(WELCOME_PAGE)
    return JsonResponse({
        "name": "django-postgres-api",
        "routes": ["GET /healthz", "GET /api/notes/", "POST /api/notes/",
                   "GET /api/notes/{id}/", "PUT /api/notes/{id}/", "DELETE /api/notes/{id}/"],
    })


urlpatterns = [
    path("", index),
    path("healthz", healthz),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
