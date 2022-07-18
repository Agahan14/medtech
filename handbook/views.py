from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import *


class HandBookViewSet(viewsets.ModelViewSet):
    serializer_class = HandBookSerializer
    queryset = Handbook.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = HandBookListSerializer(Handbook.objects.all(), many=True)
        return Response(serializer.data)


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = TodoListSerializer(Todo.objects.all(), many=True)
        return Response(serializer.data)


class EssentialsViewSet(viewsets.ModelViewSet):
    serializer_class = EssentialsSerializer
    queryset = Essentials.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated, ]


class PicturesViewSet(viewsets.ModelViewSet):
    serializer_class = PicturesSerializer
    queryset = Pictures.objects.all()
