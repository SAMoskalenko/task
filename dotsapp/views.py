from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin,
                                   RetrieveModelMixin)

from dotsapp.serializer import *


class TimeDataViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = TimeDataSerializer

    def get_queryset(self):
        return TimeData.objects.all()


class DotsDataViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = DotDataSerializer

    def get_queryset(self):
        return DotData.objects.all()


class CommentDataViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = CommentDataSerializer

    def get_queryset(self):
        return CommentData.objects.all()
