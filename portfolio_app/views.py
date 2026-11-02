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
    )
