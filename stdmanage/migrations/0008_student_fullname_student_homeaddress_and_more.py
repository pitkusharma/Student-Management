# Generated by Django 4.0.5 on 2022-07-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdmanage', '0007_remove_student_fullname_remove_student_homeaddress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fullName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='homeAddress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phNumber',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='selectClass',
            field=models.CharField(max_length=20, null=True),
        ),
    ]