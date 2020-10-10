from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


''' def detail(request, question_id, template_name='polls/detail.html'):
        question = get_object_or_404(Question, id=question_id)
        context = {
            "question": question,
         }
        return render(request, template_name, context)'''


class ResultView(generic.ListView ):
    template_name = 'polls/result.html'
    context_object_name = "question"
    model = Question


'''def result(request, question_id, template_name='polls/result.html'):
    question = get_object_or_404(Question, id=question_id)

    context = {
        "question": question,
    }
    
    return render(request, template_name, context)'''

class VoteView(generic.View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        choice = question.choice_set.get(id=request.POST['choice'])
        choice.votes += 1
        choice.save()
        return redirect('result', question_id)


        #return redirect('detail', question_id)



class SobreView(generic.TemplateView):
    template_name = 'polls/sobre.html'

    def get_queryset(self):
        return redirect('sobre')

'''def sobre(request):
    print('view - sobre')
    return HttpResponse("Dupla: Antony Raul e Maria Beatriz")
'''

