# Generated by Django 5.2.1 on 2025-06-09 15:24

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description'),
        ),
    ]
