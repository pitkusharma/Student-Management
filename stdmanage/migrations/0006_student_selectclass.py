# Generated by Django 4.0.5 on 2022-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdmanage', '0005_remove_student_selectclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='selectClass',
            field=models.CharField(max_length=20, null=True),
        ),
    ]