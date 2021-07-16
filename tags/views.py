from tags.serializers import TagSerializer
from tags.models import Tag
from rest_framework import viewsets, status, decorators
from rest_framework.response import Response
from rest_framework.decorators import action
from newsletters.serializers import NewsletterSerializer
from newsletters.models import Newsletter
from tags.pagination import StandardResultsSetPagination
from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated
 )

# Create your views here.

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)

    # Pagination and search
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
        tag = self.get_object()

        if request.method == 'GET':
            id = Newsletter.objects.filter(tags=int(tag.id))
            serialized = NewsletterSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method == 'POST':
            newsletters_id = request.data['id']
            for newsletter_id in newsletters_id:
                newsletter = Newsletter.objects.get(id=int(newsletter_id))
                newsletter.tags.add(tag.id)
            return Response(status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            newsletters_id = request.data['id']
            for newsletter_id in newsletters_id:
                newsletter = Newsletter.objects.get(id=int(newsletter_id))
                newsletter.tags.remove(tag)
            return Response(status=status.HTTP_204_NO_CONTENT)