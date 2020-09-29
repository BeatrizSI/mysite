from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from polls.models import Question,Choice



def index(request, template_name="polls/index.html"):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]

    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request,template_name , context )

def detail(request, question_id, template_name='polls/detail.html'):
    question = get_object_or_404(Question,id=question_id)
    

    context = {
        "question": question,
    }

    return render(request,template_name , context )

def result(request,question_id,template_name='polls/result.html'):
    question = get_object_or_404(Question,id=question_id)
    

    context = {
        "question": question,
    }

    return render(request,template_name,context)

def vote(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    print(request.POST)

    return redirect('detail', question_id)


def sobre(request):
    print('view - sobre')
    return HttpResponse("Dupla: Antony Raul e Maria Beatriz")
