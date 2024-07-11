# Generated by Django 4.2.13 on 2024-06-20 16:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resource_management_app', '0005_remove_advanceddetails_aging_bucket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advanceddetails',
            name='sl_poc',
        ),
        migrations.RemoveField(
            model_name='advanceddetails',
            name='tm_spoc',
        ),
        migrations.DeleteModel(
            name='RecentProjectDetails',
        ),
        migrations.DeleteModel(
            name='TechnicalDetails',
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='action_owner',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='aging',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='aging_cluster',
            field=models.CharField(default='Unknown', max_length=20),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='assessment_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='bench_classification',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='bench_start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='category',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='doj',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='experience_level',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='experience_level_fresher',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='last_release_account',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='last_release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='last_release_ig',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='last_release_industry_group',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='proficiency_status',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='profile_available',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='relocation',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='sl_poc',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sl_poc_set', to='resource_management_app.personaldetails'),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='sub_category',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='talent_category',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='talent_type',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='tm_spoc',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tm_spoc_set', to='resource_management_app.personaldetails'),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='updated_resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='wfo',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.DeleteModel(
            name='AdvancedDetails',
        ),
    ]
