# forms.py
from django import forms
from .models import PersonalDetails,Client

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = [
            'emp_id', 'first_name', 'last_name', 'email', 'reporting_manager', 'location', 'date_of_joining',
            'last_release_account', 'last_release_ig', 'last_release_date', 'updated_resume',
            'experience_level', 'doj', 'last_release_date', 'last_release_account',
            'last_release_industry_group', 'bench_start_date', 'aging', 'aging_cluster',
            'bench_classification', 'category', 'sub_category', 'talent_category',
            'talent_type', 'relocation', 'tm_spoc', 'sl_poc', 'profile_available',
            'action_owner', 'wfo', 'assessment_score', 'proficiency_status',
            'experience_level_fresher'
        ]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        

        
        

