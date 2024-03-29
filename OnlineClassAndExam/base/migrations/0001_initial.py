# Generated by Django 3.2.9 on 2022-01-03 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='discussionRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(max_length=200)),
                ('roomPrivacy', models.CharField(max_length=200, null=True)),
                ('roomDescription', models.TextField(blank=True, null=True)),
                ('roomUpdated', models.DateTimeField(auto_now=True)),
                ('roomCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-roomUpdated', '-roomCreated'],
            },
        ),
        migrations.CreateModel(
            name='discussionTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicName', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=200, null=True)),
                ('userEmail', models.EmailField(max_length=254, null=True, unique=True)),
                ('userPassword', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='messageOnTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageBody', models.TextField()),
                ('messageUpdated', models.DateTimeField(auto_now=True)),
                ('messageCreated', models.DateTimeField(auto_now_add=True)),
                ('roomName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.discussionroom')),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.useraccount')),
            ],
        ),
        migrations.AddField(
            model_name='discussionroom',
            name='hostName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.useraccount'),
        ),
        migrations.AddField(
            model_name='discussionroom',
            name='roomParticipants',
            field=models.ManyToManyField(blank=True, related_name='roomParticipants', to='base.userAccount'),
        ),
        migrations.AddField(
            model_name='discussionroom',
            name='topicName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.discussiontopic'),
        ),
    ]
