# Generated by Django 4.0 on 2023-04-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('gst_no', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=12)),
                ('pancard', models.CharField(max_length=9)),
                ('address', models.TextField()),
            ],
        ),
    ]
