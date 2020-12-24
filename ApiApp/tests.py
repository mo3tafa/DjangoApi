from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class Post(SimpleTestCase):
    databases = '__all__'
    multi_db = True

    def test_get(self):
        url = reverse("ApiApp:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_other_methods(self):
        post   = self.client.post(reverse("ApiApp:list"))
        delete = self.client.delete(reverse("ApiApp:list"))
        put    = self.client.put(reverse("ApiApp:list"))
        patch  = self.client.patch(reverse("ApiApp:list"))
        head   = self.client.head(reverse("ApiApp:list"))

        self.assertEqual(post.status_code, 405)
        self.assertEqual(delete.status_code, 405)
        self.assertEqual(put.status_code, 405)
        self.assertEqual(patch.status_code, 405)
        self.assertEqual(head.status_code, 405)

