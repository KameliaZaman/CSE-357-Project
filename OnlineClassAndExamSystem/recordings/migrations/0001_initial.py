# Generated by Django 3.2.9 on 2022-01-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoClass',
            fields=[
                ('videoId', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=200)),
                ('courseName', models.CharField(default='', max_length=200)),
                ('teacherId', models.IntegerField(default=0)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]