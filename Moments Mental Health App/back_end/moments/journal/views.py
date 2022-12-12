from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import EntrySerializer, EntryReadSerializer, MomentSerializer, PromptSerializer, UserSerializer
from .models import Entry, Moment, Prompt

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class IsOwner(permissions.BasePermission):
    """
    The request is authenticated as an owner.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as an admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and request.user.is_staff and
            request.user.is_authenticated
        )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    permission_classes = [
        IsOwner
    ]


    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return EntryReadSerializer
        return EntrySerializer

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MomentViewSet(viewsets.ModelViewSet):
    serializer_class = MomentSerializer

    permission_classes = [
        IsOwner
    ]

    def get_queryset(self):
        user = self.request.user
        return Moment.objects.filter(owner=user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

    permission_classes = [
        IsAdminOrReadOnly
    ]