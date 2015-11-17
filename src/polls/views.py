#coding: utf-8
from datetime import time
from test.inspect_fodder2 import a
import time

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, response
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.views import generic

from .models import Choice, Question
#coding: utf-8


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
# 
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})



class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
class ResultsView(generic.DetailView):
    model =Question
    template_name ='polls/results.html'
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
class QueryView(generic.ListView):
    template_name='polls/query.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Question.objects.all()
def delete(request, question_id):
    try:
        p = get_object_or_404(Question,pk=question_id)
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'error_message': "You didn't select a choice.",
        })
    else:p.delete()
    return HttpResponseRedirect(reverse('polls:query'))
def add(request):
#     t1 =request.POST['pub_date']
#     t2=time.strptime(t1,'%Y-%m-%d %H:%M:%S')
#     pub_date=time.mktime(t2)
    s=Question(question_test=request.POST['question_test'])
    s.save()
    return HttpResponseRedirect(reverse('polls:query'))
def selectone(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/selectone.html', context)
def update(request):
    question_id=request.POST['id']
    p = get_object_or_404(Question,pk=question_id)
    if(request.POST['question_test']!=None):
        p.question_test=request.POST['question_test']
        p.save()
        return HttpResponseRedirect(reverse('polls:query'))
def chart(request):
    question=Question.objects.all()
    ls=[]
    lh=[]
    for a in question:
        ls.append(a.id)
        lh.append(a.question_test.encode("utf-8"))
        
    context = {'ls': ls,'lh':lh,'question':question}
    return render(request, 'polls/chart.html',context)
def tddiv(request):
    question=Question.objects.all()
    ls=[]
    lh=[]
    lt=[]
    l4=[]
    l5=[]
    for a in question:
        ls.append(int(a.id))
        lh.append(a.question_test.encode("utf-8"))
        lt.append(a.pub_date)
        l4.append(int(a.id/1))
        l4.append(int(a.id/2))
        l4.append(int(a.id/3))
        l4.append(int(a.id/4))
        l5.append(l4)   
    context = {'ls': ls,'lh':lh,'question':question,'lt':lt,'l4':l4,'l5':l4}
    return render(request, 'polls/tddiv.html',context)
def login(request):
    return render(request,'polls/login.html')
def login1(request):
    if request.POST['name']=='admin' and request.POST['Password']=='000000':
        return HttpResponseRedirect(reverse('polls:query'))
    else:
        p=u'账号密码错误'.encode("utf-8")
        context={'p':p}
        return render(request, 'polls/login.html',context)
def tddiv1(request):
    question=Question.objects.all()
    ls=[]
    lh=[]
    lt=[]
    l4=[]
    l5=[]
    for a in question:
        ls.append(a.id)
        lh.append(a.question_test.encode("utf-8"))
        lt.append(a.pub_date)
        l4.append(a.id/1)
        l4.append(a.id/2)
        l4.append(a.id/3)
        l4.append(a.id/4)
        l5.append(l4)   
    context = {'ls': ls,'lh':lh,'question':question,'lt':lt,'l4':l4,'l5':l4}
    return render(request, 'polls/tddiv1.html',context)
        
    
    