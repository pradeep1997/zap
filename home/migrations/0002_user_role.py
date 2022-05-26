# Generated by Django 4.0.4 on 2022-05-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Manager', 'Manager'), ('Client', 'Client')], default='Employee', max_length=20),
        ),
    ]