# Generated by Django 5.1.2 on 2024-11-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='No category', max_length=100),
        ),
    ]