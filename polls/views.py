import json
from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Choice, Question
from django.utils import timezone
from common.base import successResponse, datetime2Normal
from django.template import loader
from django.http import HttpResponseRedirect
from django.views import generic


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

class QuestionView(object):
    def __init__(self):
        pass

    def create_question(self):
        q_data = json.loads(self.body)
        q = Question(question_text=q_data['data'], pub_date=timezone.now())
        q.save()
        return successResponse()

    def get_question(self):
        result = []
        q_data = Question.objects.all()
        for item in q_data:
            result.append({'question_text': item.question_text,
                           'pub_date': datetime2Normal(item.pub_date)})
        return successResponse(data=result)

