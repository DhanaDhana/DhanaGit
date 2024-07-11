
from django.db import models
from django.utils import timezone

class PersonalDetails(models.Model):
    emp_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    reporting_manager = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    last_release_account = models.CharField(max_length=100, default='Unknown')
    last_release_ig = models.CharField(max_length=100, default='Unknown')
    last_release_date = models.DateField(default=timezone.now)
    updated_resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    experience_level = models.CharField(max_length=100, default='Unknown')
    doj = models.DateField(default=timezone.now)
    last_release_industry_group = models.CharField(max_length=100, default='Unknown')
    bench_start_date = models.DateField(default=timezone.now)
    aging = models.IntegerField(default=0)
    aging_cluster = models.CharField(max_length=20, default='Unknown')
    bench_classification = models.CharField(max_length=100, default='Unknown')
    category = models.CharField(max_length=100, default='Unknown')
    sub_category = models.CharField(max_length=100, default='Unknown')
    talent_category = models.CharField(max_length=100, default='Unknown')
    talent_type = models.CharField(max_length=100, default='Unknown')
    relocation = models.CharField(max_length=100, default='Unknown')
    tm_spoc = models.ForeignKey('self', related_name='tm_spoc_set', on_delete=models.SET_NULL, null=True, default=None)
    sl_poc = models.ForeignKey('self', related_name='sl_poc_set', on_delete=models.SET_NULL, null=True, default=None)
    profile_available = models.CharField(max_length=100, default='Unknown')
    action_owner = models.CharField(max_length=100, default='Unknown')
    wfo = models.CharField(max_length=100, default='Unknown')
    assessment_score = models.IntegerField(default=0)
    proficiency_status = models.CharField(max_length=100, default='Unknown')
    experience_level_fresher = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.emp_id})"




class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensure unique client names
    contact_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)  # Optional for detailed address

    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold')
    ], default='Planning')

    def __str__(self):
        return self.name

