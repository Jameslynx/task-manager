from django.test import TestCase
from django.urls import reverse
from django.utils import timezone


from .models import Todo

# Create your tests here.
class TestMainViews(TestCase):
    def test_home_view(self):
        """
        home page response code should equal 200
        :return:
        """
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 200)

    def test_add_todo_view(self):
        """
        add_todo page response code should equal 302
        :return:
        """
        response = self.client.post(reverse("main:add_todo"), {'todo': "Just do"})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("main:add_todo"))
        self.assertEqual(response.status_code, 302)

    def test_delete_todo_view(self):
        """
        delete_todo page response code should equal 302
        :return:
        """
        task = Todo.objects.create(added_date=timezone.now(), text="task")
        url = reverse("main:delete", args=(task.id,))
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        task = Todo.objects.create(added_date=timezone.now(), text="task")
        url = reverse("main:delete", args=(task.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
