# Generated by Django 3.0.4 on 2020-04-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
                ('cfee', models.IntegerField()),
                ('Student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testapp.Student')),
            ],
        ),
    ]
