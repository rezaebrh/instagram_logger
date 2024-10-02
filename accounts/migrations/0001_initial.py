# Generated by Django 5.1.1 on 2024-10-02 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('instagram_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.instagramaccount')),
            ],
        ),
    ]
