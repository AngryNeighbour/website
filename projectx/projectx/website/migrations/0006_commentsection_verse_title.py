# Generated by Django 4.2 on 2023-07-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_commentsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsection',
            name='verse_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
