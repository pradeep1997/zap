# Generated by Django 4.0.4 on 2022-06-08 15:46

import ckeditor_uploader.fields
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1, help_text='Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.TextField(default=1, help_text='short description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=160, populate_from='title', unique=True),
        ),
    ]
