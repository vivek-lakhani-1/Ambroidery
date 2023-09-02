# Generated by Django 4.0 on 2023-04-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='challandata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challan_id', models.CharField(max_length=108)),
                ('invoice', models.CharField(max_length=108)),
            ],
        ),
        migrations.CreateModel(
            name='challanin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=108)),
                ('from_to', models.CharField(max_length=108)),
                ('Item_id', models.CharField(max_length=108)),
                ('item_name', models.CharField(max_length=108)),
                ('price', models.CharField(max_length=108)),
                ('date', models.CharField(max_length=108)),
            ],
        ),
        migrations.CreateModel(
            name='partymodel',
            fields=[
                ('username', models.CharField(max_length=108)),
                ('firmname', models.CharField(max_length=108, primary_key=True, serialize=False)),
                ('GST_no', models.CharField(max_length=108)),
                ('address', models.CharField(max_length=108)),
                ('mobile_no', models.CharField(max_length=108)),
            ],
        ),
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('username', models.CharField(max_length=108, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=108)),
                ('firm', models.CharField(max_length=108)),
                ('first_name', models.CharField(max_length=108)),
                ('last_name', models.CharField(max_length=108)),
                ('gst', models.CharField(max_length=108)),
                ('pancard', models.CharField(max_length=9)),
                ('address', models.TextField()),
            ],
        ),
    ]
