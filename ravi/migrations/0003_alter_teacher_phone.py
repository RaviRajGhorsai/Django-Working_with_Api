# Generated by Django 5.0.1 on 2024-01-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravi', '0002_teacher_student_address_alter_student_roll_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
