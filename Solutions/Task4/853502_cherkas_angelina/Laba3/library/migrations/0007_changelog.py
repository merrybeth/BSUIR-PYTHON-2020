# Generated by Django 3.0.5 on 2020-05-18 12:09

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0006_auto_20200427_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Дата/время изменения')),
                ('model', models.CharField(max_length=255, null=True, verbose_name='Таблица')),
                ('record_id', models.IntegerField(null=True, verbose_name='ID записи')),
                ('action_on_model', models.CharField(choices=[('create', 'Создание'), ('update', 'Изменение'), ('delete', 'Удаление')], max_length=50, null=True, verbose_name='Действие')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Изменяемые данные модели')),
                ('ipaddress', models.CharField(max_length=15, null=True, verbose_name='IP адресс')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор изменения')),
            ],
            options={
                'verbose_name': 'Change log',
                'verbose_name_plural': 'Change logs',
                'ordering': ('changed',),
            },
        ),
    ]