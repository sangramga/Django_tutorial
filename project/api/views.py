from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
# from django.template import loader
from django.shortcuts import get_object_or_404


def index(request):
    # return HttpResponse("Hellio you are inside api app views.py/index")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('api/index.html')
    context = {
            'latest_question_list': latest_question_list,
    }
    # response = template.render(context, request)
    # response = ", ".join([q.q_text for q in latest_question_list])
    # return HttpResponse(response)
    return render(request, 'api/index.html', context)


def detail(request, question_id):
    # return HttpResponse("Detail view .. question_id {} ".format(question_id))
    # try:
    #    question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404("Question not found")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "api/details.html", {'question': question})


def results(request, question_id):

    return HttpResponse(" Results View .. question_id %s " % question_id)


def vote(request, question_id):
    return HttpResponse("VOting view ... question_id %s " % question_id)
