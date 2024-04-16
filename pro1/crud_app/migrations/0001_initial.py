# Generated by Django 5.0.4 on 2024-04-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('previous_marks', models.FloatField()),
                ('standard', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('admission_date', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
