"""Views for displaying portfolios and their projects."""

from django.shortcuts import render
from django.views.generic import DetailView

from .models import Portfolio


def index(request):
    """Display portfolios that users can open."""
    portfolios = Portfolio.objects.select_related("student").all()
    return render(
        request,
        "portfolio_app/index.html",
        {"portfolios": portfolios},
    )


class PortfolioDetailView(DetailView):
    """Display one portfolio and the projects related to it."""
    model = Portfolio
    template_name = "portfolio_app/portfolio_detail.html"
    context_object_name = "portfolio"
