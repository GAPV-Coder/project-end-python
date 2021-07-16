from django.test import TestCase
import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from newsletters.models import Newsletter
from tags.models import Tag
from users.models import User

#To perform the tests you must disable authentication in settings.py and view permissions IsAuthenticated
# Create your tests here.

class TagsTestCase(APITestCase):

    def setUp(self):
        self.url = 'http://localhost:8000'

        self.user = User.objects.create(
            name='user1t',
            lastName='user1t',
            email='user1@test.com',
            password='user'
        )
        self.tag = Tag.objects.create(
            name='tag1',
            slug='url'
        )
        self.tag2 = Tag.objects.create(
            name='tag2',
            slug='url23'
        )
        self.newsletter = Newsletter.objects.create(
            name='newsletter1',
            description='newsletter1',
            image='assets/newsletters/chat.png',
            meta='meta',
            frequency='15'
        )
        self.newsletter2 = Newsletter.objects.create(
            name='newsletter2',
            description='newsletter2',
            image='assets/newsletters/chat.png',
            meta='meta',
            frequency='10'
        )
        self.newsletter.tags.add(self.tag)
        self.newsletter.users.add(self.user)
        self.newsletter2.users.add(self.user)
        self.newsletter2.tags.add(self.tag2)

    def test_get_newsletters_by_id(self):
        newurl2 = self.url + f'/api/v1/tags/{self.tag.id}/newsletters/'
        response = self.client.get(newurl2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_newsletters_by_id(self):
        newurl = self.url + f'/api/v1/tags/{self.tag.id}/newsletters/'
        response = self.client.post(newurl, {'id': [f'{self.newsletter2.id}'], })
        self.assertEqual(response.status_code, 201)

    def test_delete_newsletters_by_id(self):
        newurl = self.url + f'/api/v1/tags/{self.tag.id}/newsletters/'
        response = self.client.delete(newurl, {'id': [f'{self.newsletter2.id}'], })
        self.assertEqual(response.status_code, 204)

