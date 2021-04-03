from django.shortcuts import render
from .models import Question, Choice

#Get Questions and display

def index(request):
    latest_questions_list = Question.objects.all()
    return render(request, "polls/index.html")