from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question, Choice
# Create your views here.
# from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# def index(request):
#     # return HttpResponse("Hellio you are inside api app views.py/index")
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template('api/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # response = template.render(context, request)
#     # response = ", ".join([q.q_text for q in latest_question_list])
#     # return HttpResponse(response)
#     return render(request, 'api/index.html', context)

class IndexView(generic.ListView):
    template_name = "api/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]

# def detail(request, question_id):
#     # return HttpResponse("Detail view .. question_id {} "\
#     #                     .format(question_id))
#     try:
#        question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#        raise Http404("Question not found")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "api/details.html", {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "api/details.html"


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'api/results.html', {'question': question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = "api/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'api/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('api:results',
                                    args=(question.id,)))
