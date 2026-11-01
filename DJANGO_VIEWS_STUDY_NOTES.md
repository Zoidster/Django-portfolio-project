# Django Views, URLs, Templates — Quick Notes

## Request flow (MVT)

1. The browser sends an HTTP request for a URL.
2. The project URL configuration (`django_project/urls.py`) matches the URL and includes the app URL configuration.
3. The app URL configuration (`portfolio_app/urls.py`) chooses a view.
4. The view gets data from models through the Django ORM when needed.
5. The view returns an HTTP response, often by rendering a template with a context dictionary.
6. Django returns the response to the browser.

**MVT:** Model = data and relationships; View = request-handling logic; Template = presentation/HTML.

## URLs and views

- `urlpatterns` is the list of URL patterns Django checks.
- `path("", include("portfolio_app.urls"))` sends root-level routes to the app's URL configuration.
- `path("admin/", admin.site.urls)` keeps the built-in admin available.
- `name="index"` and `name="portfolio-detail"` give routes stable names.
- `{% url 'portfolio-detail' portfolio.pk %}` generates a link using a route name and the selected object's primary key. This avoids hardcoding the URL.
- A function-based view is a Python function that accepts `request` and returns a response.
- A class-based view packages behavior in a class. `DetailView` retrieves one model object; `.as_view()` makes the class usable by URL routing.

## Templates

- App templates live under `portfolio_app/templates/portfolio_app/` so Django can find them with app template discovery enabled.
- `{% extends "portfolio_app/base_template.html" %}` inherits the shared page structure.
- `{% block content %}` marks the section a child template fills in.
- `{{ value }}` displays a value.
- `{% for item in items %}` loops through data; `{% empty %}` supplies a fallback when there are no items.
- `render(request, template_name, context)` combines a template with data and returns an HTTP response.
- The context dictionary passes data from the view into the template. Keep database queries in Python views rather than embedding query logic in HTML.

## Models and relationships in this project

- `Student` has a one-to-one relationship with `Portfolio`: each portfolio is linked to one student.
- `Project.portfolio` is a foreign key to `Portfolio`: one portfolio can have many projects.
- Since `Project` does not define a `related_name`, Django's reverse relation is `portfolio.project_set`.
- `PortfolioDetailView` gets the portfolio identified by `<int:pk>` and returns 404 if no matching record exists.
- `portfolio.project_set.all` provides the projects associated with the selected portfolio.
- Reading/querying records does not itself change the database. Admin is currently used to create test records; user-facing create/update/delete forms are for a later sprint.

## Current implementation in this project copy

- The project URL configuration includes `portfolio_app.urls` at the root.
- The app URL configuration routes `/` to `index` and `/portfolios/<pk>/` to `PortfolioDetailView`.
- The home page lists portfolios and links to each detail page.
- The detail page shows title, about text, contact email, active status, and related project titles/descriptions. It includes a message when there are no projects and a link back home.
- `portfolio_app/tests.py` contains tests for listing, details, correct project relationships, empty portfolios, 404 behavior, and navigation.

## Manual test checklist

1. Start the server and open `/`.
2. Confirm the home page lists the portfolios created in Django Admin.
3. Click a portfolio and verify its title, about text, contact email, and active status.
4. Verify only that portfolio's projects appear.
5. Open a portfolio with no projects and confirm the fallback message appears.
6. Change a portfolio's active status in Admin and verify the detail page reflects it.
7. Request `/portfolios/999999/` (or another nonexistent primary key) and confirm a 404 page.
8. Use the home navigation link to return to `/`.

## Before continuing

- Run `python manage.py check` and `python manage.py test` inside the project's virtual environment.
- Confirm the app works with your own local database and records.
- Make the required Git branch in your actual repository before applying changes there, if your instructor expects the lecture's `views_template_sprint2` branch.
- Write any required individual technical summary yourself, using your own screenshots, test results, and understanding.
