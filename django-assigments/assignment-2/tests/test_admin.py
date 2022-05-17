import pytest
from polls.models import Question
from django.utils import timezone


def test_admin_create_questionsd(client, admin_user):
    client.force_login(admin_user)
    assert Question.objects.count() == 0

    response = client.post(
        "/admin/polls/question/add/",
        {"question_text": "Test", "pub_date": timezone.now()},
    )
    # 200 means the form is being re-displayed with errors
    assert response.status_code == 200
    # question = Question.objects.order_by("-id")[0]

    # assert question == "Test"
