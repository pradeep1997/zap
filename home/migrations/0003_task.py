# Generated by Django 4.0.4 on 2022-05-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('date', models.DateField()),
                ('desc', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('utimestamp', models.DateTimeField(auto_now=True)),
                ('track', models.TextField(blank=True, editable=False)),
                ('utrack', models.TextField(blank=True, editable=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete')], default='pending', max_length=10)),
            ],
            options={
                'verbose_name_plural': '02. Tasks',
            },
        ),
    ]