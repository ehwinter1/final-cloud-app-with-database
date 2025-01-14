# Generated by Django 3.1.3 on 2023-01-19 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_grade',
            new_name='grade',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.AddField(
            model_name='choice',
            name='question_text',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
            preserve_default=False,
        ),
    ]
