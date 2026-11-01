"""URL patterns for the portfolio application."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "portfolios/<int:pk>/",
        views.PortfolioDetailView.as_view(),
        name="portfolio-detail",
    ),
]
