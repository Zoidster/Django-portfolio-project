from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio


# Create your views here.

#def index(request):
#    return HttpResponse("Portfolio Home Page")             1st in slides

#def index(request):
#    return render(request, 'portfolio_app/index.html')     2nd in slides

def index(request):
    # Retrieve active portfolios
    active_portfolios = Portfolio.objects.filter(
        is_active=True
    )

    return render(
        request,
        'portfolio_app/index.html',
        {'active_portfolios': active_portfolios}
    )                                                      #3rd in slides

from django.views.generic import ListView, DetailView
from .models import Student
from .models import Project

class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'projects'
