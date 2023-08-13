from django.test import TestCase
from django.urls import reverse
from .models import News, Comment

class NewsModelTest(TestCase):

    def setUp(self):
        self.news = News.objects.create(title="Test News", content="This is test content.")
        
    def test_news_with_comments(self):
        Comment.objects.create(content="Test Comment", news=self.news)
        self.assertTrue(self.news.has_comments())

    def test_news_without_comments(self):
        self.assertFalse(self.news.has_comments())


class NewsListViewTest(TestCase):

    def setUp(self):
        News.objects.create(title="News 1", content="Content 1")
        News.objects.create(title="News 2", content="Content 2")

    def test_news_are_sorted_by_created_at_descending(self):
        response = self.client.get(reverse('news_list'))
        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200)
        # Проверка порядка новостей
        self.assertEqual(response.context['news'][0].title, "News 2")
        self.assertEqual(response.context['news'][1].title, "News 1")

class NewsDetailViewTest(TestCase):

    def setUp(self):
        self.news = News.objects.create(title="News Detail", content="Content Detail")

    def test_news_detail_view(self):
        response = self.client.get(reverse('news_detail', args=[self.news.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "News Detail")
        self.assertContains(response, "Content Detail")

class NewsCommentsViewTest(TestCase):

    def setUp(self):
        self.news = News.objects.create(title="News with Comments", content="Content with Comments")
        Comment.objects.create(content="First Comment", news=self.news)
        Comment.objects.create(content="Second Comment", news=self.news)

    def test_news_comments_order(self):
        response = self.client.get(reverse('news_detail', args=[self.news.id]))
        self.assertEqual(response.status_code, 200)
        comments_in_template = list(response.context['comments'])
        self.assertEqual(comments_in_template[0].content, "Second Comment")
        self.assertEqual(comments_in_template[1].content, "First Comment")
