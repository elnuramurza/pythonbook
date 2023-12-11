# Generated by Django 4.2.7 on 2023-12-08 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='profile',
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_list', to='students.student'),
        ),
    ]
