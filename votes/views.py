from votes.serializers import VoteSerializer
from votes.models import Vote
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from tags.serializers import TagSerializer
from tags.models import Tag
from users.models import User, User, User
from users.serializers import UserSerializer
from  rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated
 )

# Create your views here.

class VotesViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    pagination_class = PageNumberPagination
    permission_classes = ( IsAuthenticated,)
