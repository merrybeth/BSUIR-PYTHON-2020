from multiprocessing.pool import ThreadPool

from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
from datetime import date

from django.dispatch import receiver


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre ")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre ")
    isbn = models.CharField('ISBN', max_length=13)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    publisher = models.ManyToManyField(Publisher, help_text="Select a publisher for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def display_publisher(self):
        return ', '.join([publisher.name for publisher in self.publisher.all()[:3]])

    display_publisher.short_description = 'Publisher'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    date_take = models.DateField(null=True, blank=True)
    date_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["date_back"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)

    @property
    def is_overdue(self):
        if self.date_back and date.today() > self.date_back:
            return True
        return False


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["author_detail"]

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)                                   #added
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()




class Mail(models.Model):                                                         #added
    email_caption = models.CharField('Заголовок сообщения', max_length=100)
    email_text = models.TextField('Текст сообщения', null=True)
    email_date = models.DateField('Время отправки', null=True)
    email_time = models.TimeField(null=True)
    resp = models.ManyToManyField(Profile, limit_choices_to={'is_verified': True}, blank=False)
    posted = models.BooleanField(default=False)

    def __str__(self):
        if not self.posted:
            self.posted = True
            self.send()
            self.save()
        return str(self.email_caption)

    def send(self):
        mess = render_to_string('library/mail.html', {
            'email_text': self.email_text,
            'email_date': self.email_date,
            'email_time': self.email_time
        })
        email_caption = self.email_caption
        count = self.resp.count()
        pool = ThreadPool(count)
        result = []
        for profile in self.resp.all():
            to_email = profile.user.email
            email = EmailMessage(email_caption, mess, to=[to_email])
            result.append(email)
        pool.map(send_mail, result)


def send_mail(email):                                                #added
    email.send()

