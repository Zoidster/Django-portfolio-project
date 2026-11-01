from django.test import TestCase
from django.urls import reverse

from .models import Portfolio, Project, Student


class PortfolioViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.create(
            name="Test Student",
            email="student@example.com",
            major="CSCI-BS",
        )
        cls.portfolio = Portfolio.objects.create(
            student=cls.student,
            title="Test Portfolio",
            contact_email="portfolio@example.com",
            is_active=True,
            about="A test portfolio.",
        )
        cls.other_student = Student.objects.create(
            name="Second Student",
            email="second@example.com",
            major="CSCI-BS",
        )
        cls.other_portfolio = Portfolio.objects.create(
            student=cls.other_student,
            title="Portfolio Without Projects",
            contact_email="second@example.com",
            is_active=False,
            about="No projects yet.",
        )
        Project.objects.create(
            portfolio=cls.portfolio,
            title="Related Project",
            description="Belongs to the test portfolio.",
        )
        Project.objects.create(
            portfolio=cls.other_portfolio,
            title="Different Portfolio Project",
            description="Must not appear on the first portfolio.",
        )

    def test_home_page_lists_portfolios_with_detail_links(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Portfolio")
        self.assertContains(response, "Portfolio Without Projects")
        self.assertContains(
            response, reverse("portfolio-detail", args=[self.portfolio.pk])
        )

    def test_detail_page_shows_portfolio_fields_and_related_project(self):
        response = self.client.get(
            reverse("portfolio-detail", args=[self.portfolio.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Portfolio")
        self.assertContains(response, "A test portfolio.")
        self.assertContains(response, "portfolio@example.com")
        self.assertContains(response, "Active")
        self.assertContains(response, "Related Project")
        self.assertContains(response, "Belongs to the test portfolio.")
        self.assertNotContains(response, "Different Portfolio Project")

    def test_detail_page_shows_message_when_no_projects_exist(self):
        response = self.client.get(
            reverse("portfolio-detail", args=[self.other_portfolio.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This portfolio does not have any projects yet.")
        self.assertContains(response, "Inactive")

    def test_nonexistent_portfolio_returns_404(self):
        response = self.client.get(reverse("portfolio-detail", args=[999999]))
        self.assertEqual(response.status_code, 404)

    def test_detail_page_has_home_navigation(self):
        response = self.client.get(
            reverse("portfolio-detail", args=[self.portfolio.pk])
        )
        self.assertContains(response, 'href="{}"'.format(reverse("index")))
