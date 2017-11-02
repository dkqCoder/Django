# -*- coding: utf-8 -*-
from models import Question,Choice
def get_data_by_id(id):
    resultDict = Question.objects.filter(id=id).first()
    return resultDict

def get_data_all():
    resultDict = Question.objects.all()
    return resultDict

def save_date(question):
    question.save()