# Generated by Django 4.0.5 on 2022-07-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdmanage', '0008_student_fullname_student_homeaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dateOfBirth',
            field=models.DateField(auto_now=True),
        ),
    ]