from django.test import TestCase
import unittest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from newsletters.models import Newsletter
from tags.models import Tag
from users.models import User

# Create your tests here.
# To perform the tests you must disable authentication in settings.py and view permissions IsAuthenticated

class NewslettersTestCase(APITestCase):

    def setUp(self):
        self.url = 'http://localhost:8000'

        self.user = User.objects.create(
            name='User1N',
            lastName='User1N',
            email='user1n@test.com',
            password='user1n'
        )
        self.user2 = User.objects.create(
            name='User2N',
            lastName='User2N',
            email='user2n@test.com',
            password='user2n'
        )
        self.tag = Tag.objects.create(
            name='Tag1n',
            slug='url'
        )
        self.tag2 = Tag.objects.create(
            name='Tag2n',
            slug='url2'
        )
        self.newsletter = Newsletter.objects.create(
            name='N1n',
            description='N1nd',
            image='assets/newsletters/chat.png',
            meta='N1M',
            frequency='15'
        )
        self.newsletter.tags.add(self.tag)
        self.newsletter.users.add(self.user)

    def test_get_tags_by_id(self):
        newurl = self.url + f'/api/v1/newsletters/{self.newsletter.id}/tags/'
        response = self.client.get(newurl)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_tags_by_id(self):
        newurl = self.url + f'/api/v1/newsletters/{self.newsletter.id}/tags/'
        response = self.client.post(newurl, {'tags': [f'{self.tag2.id}'], })
        self.assertEqual(response.status_code, 201)

    def test_delete_tags_by_id(self):
        newurl = self.url + f'/api/v1/newsletters/{self.newsletter.id}/tags/'
        response = self.client.delete(newurl, {'tags': [f'{self.tag2.id}'], })
        self.assertEqual(response.status_code, 204)

    def test_post_users_by_id(self):
        newurl = self.url + f'/api/v1/newsletters/{self.newsletter.id}/users/'
        response = self.client.post(newurl, {'id': [f'{self.user2.id}'], })
        self.assertEqual(response.status_code, 201)
