from django.contrib.auth.models import User
from django.test import TestCase, Client
from .apps import WebConfig
from django.urls import reverse
from .forms import SignupForm
from .models import Author, Genre, Book, Publisher



class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Publisher.objects.create(name='publisher', isbn='1234567890123')
        Genre.objects.create(name='genre')
        Author.objects.create(first_name='firstname', last_name='lastname',
                              date_of_birth = '2000-01-01',date_of_death = '2001-01-01')

        publisher = Publisher.objects.get(id=1)
        genre = Genre.objects.get(id=1)
        author = Author.objects.get(id=1)

        for book in range(3):
            book = Book.objects.create( author=author,title = 'book',summary = 'summary')
            book.publisher.add(publisher)
            book.genre.add(genre)


    def test_field_length(self):
        book = Book.objects.get(id=1)
        length = book._meta.get_field('summary').max_length
        self.assertEqual(length, 1000)

    def test_name_model(self):
        book = Book.objects.get(id=1)
        title = book.title
        self.assertEqual(title, str(book))





class TestApp(TestCase):

    def test_app_name(self):
        app = WebConfig
        assert app.name == 'library'


class User_Test(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='user', password='password', email='mail@mail.ru')
        cls.test_user.save()


    def test_login(self):
        resp = self.client.post(reverse('login'), {'username':'user', 'password': 'password'})
        self.assertEqual(resp.url, '/')

    def test_login_html(self):
        resp = self.client.get('/accounts/login/')
        assert resp.status_code == 200

    def test_fail_login(self):
        resp = self.client.post(reverse('login'), {'username': 'user', 'password': 'notapassword'})
        self.assertRaisesMessage(resp, 'Invalid login')

    def test_register(self):
        client = Client()
        resp = client.post('/accounts/register')
        assert resp.status_code == 200
        resp = client.post('/accounts/register', {'username': 'username', 'email': 'mail@mail.ru',
                                          'password1': 'pass','password2':'pass'})
        assert resp.status_code == 200
        resp = client.get('/accounts/register')
        assert resp.status_code == 200

    def test_invalid_register(self):
        form = SignupForm()
        self.assertFalse(form.is_valid())


    def test_logout(self):
        resp = self.client.get('/accounts/logout/')
        assert resp.status_code == 200




