from rest_framework import mixins, viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """List, create, read and delete notes. Reading is public; writing needs a token."""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
