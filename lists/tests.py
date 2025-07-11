from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.


# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1 + 1, 3)

# Old test versions

# class HomePageTest(TestCase):
#     """Test the home page"""

#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)

#         html = response.content.decode("utf8")
#         self.assertIn("<title>To-Do lists</title>", html)
#         self.assertTrue(html.startswith("<html>"))
#         self.assertTrue(html.endswith("</html>"))

#     def test_home_page_returns_correct_html(self):
#         response = self.client.get("/")
#         self.assertContains(response, "<title>To-Do lists</title>")


# Final test version


class HomePageTest(TestCase):
    """Test the home page"""

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do lists</title>")
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")
