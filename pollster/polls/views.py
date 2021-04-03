from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Question, Choice

# Get Questions and display


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_questions_list": latest_questions_list
    }
    return render(request, "polls/index.html", context)

# show specific Qs and Choices


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# get Q and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# vote


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "Polls/detail.html", {'question': question, "error_message": "You didn't select a choice!"})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Polls:results', args=(question.id,)))
