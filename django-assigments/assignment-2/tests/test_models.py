import pytest
from polls.models import Question, Choice
from django.utils import timezone

@pytest.mark.django_db
def test_Question():
    assert Question.objects.count() == 0


@pytest.mark.django_db
def test_str_Question():
    sub_field = Question.objects.create(question_text="Test", pub_date=timezone.now())
    assert str(sub_field) == "Test"


@pytest.mark.django_db
def test_Choice():
    assert Choice.objects.count() == 0


@pytest.mark.django_db
def test_str_Choice():

    question_obj = Question.objects.create(
        question_text="Test", pub_date=timezone.now()
    )

    sub_field = Choice.objects.create(
        question=question_obj, choice_text="Test", votes=0
    )
    assert str(sub_field) == "Test"
