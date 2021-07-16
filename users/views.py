from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from users.serializers import UserSerializer
from users.models import User
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from users.serializers import UserSerializer
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from newsletters.models import Newsletter
from newsletters.serializers import NewsletterSerializer
from votes.models import Vote
from users.pagination import StandardResultsSetPagination
from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated
 )

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)

    # Paginación y busqueda
    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item not in ['page_size']:
                continue
                if item in ['users', 'tags']:
                    query[item + '__id'] = self.request.query_params[item]
                    continue
                query[item + '__icontains'] = self.request.query_params[item]
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def newsletters(self, request, pk=None):
        user = self.get_object()
        # As a user I want to log in so I can see the newsletters I am subscribed to.
        if request.method == 'GET':
            id = Newsletter.objects.filter(users=int(user.id))
            serialized = NewsletterSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        # As a user I want to be able to subscribe to a newsletter to receive related news in my mailbox.
        if request.method == 'POST':
            id_user = user.id
            newsletters_id = request.data['id']
            for newsletter_id in newsletters_id:
                newsletter = Newsletter.objects.get(id=int(newsletter_id))
                newsletter.users.add(id_user)
            return Response(status=status.HTTP_201_CREATED)
        # As a user I want to be able to unsubscribe from the newsletters to stop receiving news.
        if request.method == 'DELETE':
            id_user = user.id
            newsletters_id = request.data['id']
            for newsletter_id in newsletters_id:
                newsletter = Newsletter.objects.get(id=int(newsletter_id))
                newsletter.users.remove(id_user)
            return Response(status=status.HTTP_204_NO_CONTENT)