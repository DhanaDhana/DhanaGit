# Generated by Django 3.0.4 on 2020-04-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
