# Generated by Django 5.2.1 on 2025-06-21 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_pageviewlog_ip_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='tag',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blogpost')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(to='main.tag'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.ManyToManyField(to='main.tag'),
        ),
    ]
