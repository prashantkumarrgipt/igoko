# Generated by Django 4.0.4 on 2023-07-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_blogsitebackend'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('specialNotes', models.TextField()),
            ],
        ),
    ]
