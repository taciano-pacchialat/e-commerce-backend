# Generated by Django 5.1.3 on 2024-11-15 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
    ]
