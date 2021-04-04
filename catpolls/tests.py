import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Catuestion


class CatuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Catuestion(publication_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Catuestion(publication_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Catuestion(publication_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_catuestion(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Catuestion.objects.create(catuestion_text=question_text, publication_date=time)


class CatuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('catpolls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_catuestion_list'], [])

    def test_past_question(self):
        create_catuestion(question_text="Past question.", days=-30)
        response = self.client.get(reverse('catpolls:index'))
        self.assertQuerysetEqual(
            response.context['latest_catuestion_list'],
            ['<Catuestion: Past question.>']
        )

    def test_future_question(self):
        create_catuestion(question_text="Future question.", days=30)
        response = self.client.get(reverse('catpolls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_catuestion_list'], [])

    def test_future_question_and_past_question(self):
        create_catuestion(question_text="Past question.", days=-30)
        create_catuestion(question_text="Future question.", days=30)
        response = self.client.get(reverse('catpolls:index'))
        self.assertQuerysetEqual(
            response.context['latest_catuestion_list'],
            ['<Catuestion: Past question.>']
        )

    def test_two_past_questions(self):
        create_catuestion(question_text="Past question 1.", days=-30)
        create_catuestion(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('catpolls:index'))
        self.assertQuerysetEqual(
            response.context['latest_catuestion_list'],
            ['<Catuestion: Past question 2.>', '<Catuestion: Past question 1.>']
        )


class QuestionDetailViewTest(TestCase):

    def test_future_question(self):
        future_question = create_catuestion(question_text="Future question.", days=5)
        url = reverse('catpolls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_catuestion(question_text="Past question.", days=-5)
        url = reverse('catpolls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.catuestion_text)
