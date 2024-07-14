# Generated by Django 4.2.1 on 2023-12-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bigdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Cloud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ML',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='NLP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Announcement1', models.TextField(max_length=300)),
                ('Announcement2', models.TextField(max_length=300)),
                ('Announcement3', models.TextField(max_length=300)),
                ('Link_text_1', models.TextField(max_length=100)),
                ('Link_text_2', models.TextField(max_length=100)),
                ('Link_text_3', models.TextField(max_length=100)),
                ('Link_text_4', models.TextField(max_length=100)),
                ('Link', models.URLField()),
            ],
        ),
    ]