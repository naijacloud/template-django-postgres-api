from django.contrib import admin
from django.db import connection
from django.http import JsonResponse
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


urlpatterns = [
    path("healthz", healthz),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
