# Generated by Django 3.0.4 on 2020-04-06 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Student_id',
        ),
        migrations.AddField(
            model_name='course',
            name='Student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='testapp.Student'),
        ),
    ]
