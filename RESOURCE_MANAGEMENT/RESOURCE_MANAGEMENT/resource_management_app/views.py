from django.shortcuts import render, redirect,get_object_or_404
from .models import PersonalDetails  
from .forms import EmployeeDetailsForm,Client
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Project, Client
from django.http import HttpResponseForbidden


@login_required
def personal_details(request):
    reporting_managers = [
    '',
    'Akanchha Saxena',
    'Andy Gwisdala',
    'Arun John',
    'Ashina Sipiora',
    'Ashley Ulloque',
    'Avinash Bhat',
    'Balaji Muralikrishnan',
    'Barney',
    'Gopakumar Nair',
    'Jason Volm',
    'Jessica Westerlund',
    'Mahesh Gupta',
    'Noah Dewey',
    'Prathyus Tripathi',
    'Sumar Loomba',
    'Trevor Mohan',
    'Vijay Mohan'
]
    locations = ['', 'Bengaluru', 'Hyderabad']

    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        reporting_manager = request.POST.get('reporting_manager')
        location = request.POST.get('location')
        date_of_joining = request.POST.get('date_of_joining')

        PersonalDetails.objects.create(emp_id=emp_id, first_name=first_name, last_name=last_name, email=email, reporting_manager = reporting_manager, location=location, date_of_joining=date_of_joining)

        return redirect('technical_details')
    
    return render(request, 'personal_details.html', {'reporting_managers':reporting_managers, 'locations':locations})

@login_required
def technical_details(request):
    primary_skills = [
    '',
    'OpenShift',
    '.NET',
    '.Net build',
    'Android',
    'Angular',
    'Ansible',
    'Apache Spark',
    'API',
    'APM tools',
    'Appium Tools',
    'Ariba',
    'Armory',
    'ASP.NET',
    'AUC (Asset Under Construction)',
    'Testing',
    'AWS',
    'Azure Cloud',
    'Azure Data Factory',
    'Azure Data Lake',
    'Azure Databricks',
    'Azure SQL',
    'Azure SQL Managed Instance',
    'Azure Synapse',
    'Bitbucket',
    'C#',
    'C++',
    'CA Rally',
    'Cassandra',
    'Cmake',
    'Confluence',
    'Control-M',
    'CSS3',
    'DevOps',
    'Docker',
    'EDI',
    'Fullstack',
    'GCP',
    'GitHub tools',
    'HTML5',
    'IBM MDM',
    'Informatica PowerCenter',
    'Java',
    'JavaScript',
    'Jenkins',
    'JIRA',
    'JQuery',
    'Kafka',
    'Kotlin',
    'Kubernetes',
    'Lakehouse',
    'Linux',
    'Linux Kernel',
    'LogiAnalytics',
    'Logic Apps',
    'Machine Learning',
    'Microservices',
    'Microsoft Azure',
    'Mongo DB',
    'MS SQL',
    'MS Stack (OS/Application)',
    'MS Visual Studio',
    'MVC',
    'NodeJS',
    'ObjectiveC',
    'OCR (Optical Character Recognition)',
    'Octopus',
    'Oracle',
    'PCF',
    'PEGA',
    'Performance Testing',
    'Perl',
    'PostGres',
    'Postman',
    'Power Automate',
    'PowerBI',
    'PowerShell',
    'PySpark',
    'Python',
    'QTest',
    'Quay',
    'Ranorex',
    'React JS',
    'Rest API',
    'RPA Tool',
    'Salesforce',
    'SAP ERP',
    'SAP EWM',
    'SAP MM',
    'SAP S/4 Hana',
    'SAP SRM',
    'SAP TM',
    'SauceLabs',
    'Scons',
    'Scrum Master',
    'SDET',
    'Selenium',
    'ServiceNow',
    'SharePoint',
    'Shell Scripting',
    'Snowflake',
    'SoapUI',
    'Spark',
    'Spring Boot',
    'SQL Server',
    'SRE (Site Reliability Engineering)',
    'SSIS',
    'SSRS',
    'SWIFT',
    'Tableau',
    'TeamCity',
    'Terraform',
    'TFS',
    'Tivoli',
    'Tosca',
    'T-SQL',
    'TypeScript',
    'UI/UX',
    'UIPath',
    'Unix scripts',
    'VMware hypervisor',
    'WCF',
    'WebAPI',
    'Mainframe',
    'Cobol',
    'Fullstack',
    'SAP Commerce Cloud',
    'ADAS',
    'Gitlab',
    'Cypress',
    'Preevision',
    'Testing',
    'Automotive Android',
    'Preevision',
    'Model Based Clustering',
    'Tool Development',
    'AWS DevOps',
    'Solidworks',
    'Catia',
    'Adobe Experience Manager',
    'Arc-GIS / QGIS',
    'Creo',
    'AutoCAD',
    'Quality Assurance',
    'Cybersecurity',
    'Project Manager',
    'Auto SAR',
    'CAN/CANOE',
    'DRUPAL',
]

    demand_roles = [
    '',
    'QA Engineer',
    'SDET - Lead',
    'Product Development',
    'Associate Project Manager',
    'Azure Data Analyst',
    'Software Systems Engineer',
    'Sr. Scrum Master',
    'Senior Developer CRM Digital Experience Platform (DXP eCommerce)',
    'QA Analyst / Tester',
    'Project Manager/ Scrum Master',
    'Java Backend Engineer',
    'Foundational-Java Developer',
    'Kernel Developer',
    'GO Developer OR Sr Java developer',
    'Tools Support Engineer',
    'Java Angular Fullstack Developer',
    'Java Angular Fullstack Developer - Mid',
    'Mainframe / Cobol Developer',
    'Informatica Developers',
    'Sr . Net Developer',
    'SAP Commerce Business Analyst',
    'Data Engineer- IA/RPA/Blue Prism',
    'Sr. Business Analyst - AI knowledge',
    'ServiceNow Lead Engineer',
    'LEAD SDET (Software Developer Engineer in Test)',
    'Terraform Engineer',
    'Deskside Technician',
    '.Net Developer',
    '.Net Technical Lead',
    'Full Stack UI/UX Lead',
    'Front End Developers',
    'ETL Informatica Developer',
    'API Developer',
    'AEM Developer',
    'System Analyst I',
    'Salesforce LWC Developer',
    'DevOps NGA Admin',
    'Lead Developer Java Sping',
    'UI /UX Developer',
    'Data and Analytics',
    'Sap ABAP Developer',
    'Cloud Engineer',
    'cloud & infra',
    'Senior SFMC Campaign Developer',
    'Presentation specialist',
    'Content Writer',
    'Presentation specialist',
    'Proofreader',
    'Sr Retoucher Marketing Creative',
    'Creative Project Manager',
    'Production Designer - Senior',
    'Proofreader',
    'Presentation Designer',
    'Graphic Designer',
    'AV Tech',
    'Junior Developer - IVR',
    'Sr. Fullstack Java Developers',
    'Jr. Fullstack Java Developers',
    'Full Stack Software Development Engineer in Test (SDET)',
    'Python Developer',
    'Sap MM Analyst',
    'ADAS System Engineering leader',
    'ADAS MIL validation',
    'Lead SW Validation (Cluster MBD)',
    'Preevision Architect',
    'Android Developer',
    'Lead DevOps Engineer',
    'Design Engineer',
    'Automation Engineer',
    'IOS Developer',
    'Trainee',
    'Python Lead Engineer',
    'Lead Software Engineer',
    'Design Associate',
    'Software Engineer',
    'Quality assurance',
    'Engineering Manager',
    'Sr.Software Engineer',
    'Autosar Developer',
    'Jr. Fullstack Java Developers',
    'Sr. Fullstack Java Developer',
    'Architect Manager',
    'Testing Engineer',
    'Lead Engineer',
    'Delivery Lead',
    'Technical Lead',
    'Lead Consultant',
    'Program Manager',
    'React, Node JS FrontEnd Developer',
    'Angular, node js FrontEnd Developer',
    'F# Back End Developer',
]

    career_roles = [
    '',
    'Admin Lead',
    'Admin Manager',
    'Analyst PMO',
    'Analyst Workforce management',
    'Architect',
    'Associate Analyst',
    'Business Analyst',
    'Chief Architect',
    'Consultant',
    'Customer Support Analyst',
    'Customer Support Associate',
    'Delivery Director',
    'Delivery Head - Cloud & Infrastructure',
    'Delivery Head - Customer Experience',
    'Delivery Head - Data & Analytics',
    'Delivery Head - Digital & product Engineering',
    'Delivery Manager',
    'Design associate',
    'Design Engineer',
    'Director of Engineering',
    'Director Operations',
    'Director PMO',
    'Director Workforce management',
    'Engineering Manager',
    'Head of Operations delivery',
    'Head of Program Management Office',
    'Head of workforce management',
    'Lead Consultant',
    'Lead Customer Support',
    'Lead Design Engineer',
    'Lead Software Engineer',
    'Lead Software Engineer / Project Manager',
    'Manager Operations',
    'Manager PMO',
    'Manager Workforce management',
    'Practice Head - Customer Experience',
    'Practice Head - Cloud & Infrastructure',
    'Practice Head - Data & Analytics',
    'F# Back End Developer',
]

    service_lines = [
    '',
    'Customer Experience',
    'Digital And Product Engineering',
    'Data & Analytics',
    'Cloud & Infrastructure',
]

    sub_service_lines = [
    '',
    'CX design and strategy',
    'Digital Marketing and Automation',
    'UI/UX',
    'Digital Commerce',
    'CRM & Loyalty',
    'Application Development',
    'Application Maintenance',
    'Quality Engineering',
    'Embedded Software',
    'Embedded Hardware',
    'Embedded Testing and Validation',
    'Connected Products',
    'Devops',
    'Enterprise Apps Dev',
    'Enterprise Apps Maintainance',
    'Enterprise Apps Testing',
    'Communication Network',
    'Data Engineering',
    'Insights Engineering',
    'Data Science (ML, AI, Gen AI, Advance Analytics)',
    'Data Systems Support, AIOps',
    'Cloud-Migration',
    'Cloud-Moderanisation',
    'Native Apps',
    'Workplaces',
    'Hybrid Runops-Traditional',
    'Hybrid Runops-Digital',
    'Hybrd Runops-T&D',
    'ERP',
    'ServiceNow',
]

    if request.method == 'POST':
        primary_skill = request.POST.get('primary_skill')
        detailed_skill = request.POST.get('detailed_skill')
        trained_skill = request.POST.get('trained_skill')
        demand_role = request.POST.get('demand_role')
        career_role = request.POST.get('career_role')
        service_line = request.POST.get('service_line')
        sub_service_line = request.POST.get('sub_service_line')
        experience = request.POST.get('experience')

        PersonalDetails.objects.create(primary_skill=primary_skill, detailed_skill=detailed_skill, trained_skill=trained_skill, demand_role=demand_role, career_role=career_role, service_line=service_line, sub_service_line=sub_service_line, experience=experience)

        return redirect('recent_project_details')
    
    return render(request, 'technical_details.html', {'primary_skills':primary_skills, 'demand_roles':demand_roles, 'career_roles':career_roles, 'service_lines':service_lines, 'sub_service_lines':sub_service_lines})
@login_required
def recent_project_details(request):
    last_release_accounts = [
    '',
    'Airbus',
    'American Heart Association',
    'Aviva',
    'Bank Of America',
    'BCE',
    'Bendigo and Adelaide Bank',
    'Bendigo Bank',
    'BioStream',
    'Boeing',
    'Bombardier',
    'Cerberus',
    'Cisco',
    'CVS Health',
    'Experian',
    'FTTH',
    'Goeasy',
    'Home Depot',
    'Internal',
    'Ivanti',
    'Johnson & Johnson',
    'KBC',
    'Lululemon',
    'Macquarie',
    'Mars',
    'McGraw Hill',
    'MyEyeDr',
    'NEB',
    'Orchid Orthopedic',
    'Pacific Life Insurance',
    'Prophix',
    'Regeneron Pharmaceuticals',
    'Renault-India',
    'Renault-Nearshore',
    'Rockwell Automation',
    'Southwest Business Corp',
    'Synerion',
    'Tenneco',
    'Teradata',
    'TrustEase',
    'TSSA',
    'Twin City Fan And Blower Company',
    'United Airlines',
    'Venerable',
    'Verizon GE',
    'Vrize',
    'Walmart',
    'World Shipping',
    'Valeo',
    'Proximus',
]

    last_release_igs = [
    '',
    'Banking, Financial Services and Insurance',
    'Healthcare and Life Science',
    'Consumer and Retail',
    'Technology, Media and Telecom',
    'Automotive, Aerospace, Defence, Manufacturing',
    'Public',
]
    
    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            last_release_account = form.cleaned_data.get('last_release_account')
            if not last_release_account:
                form.add_error('last_release_account', 'Last release account cannot be null.')
            else:
                form.save()
                return redirect('advanced_details.html')  
    else:
        form = EmployeeDetailsForm()

    return render(request, 'recent_project_details.html', {'form': form,'last_release_accounts':last_release_accounts,'last_release_igs':last_release_igs})

def success(request):
    return render(request, 'success.html')

@login_required
def dashboard(request):
    query = request.GET.get('search')
    if query:
        employees = PersonalDetails.objects.filter(
            Q(emp_id__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(reporting_manager__icontains=query) |
            Q(location__icontains=query) |
            Q(date_of_joining__icontains=query)
        )
    else:
        employees = PersonalDetails.objects.all()
    
    context = {
        'employees': employees,
    }
    return render(request, 'dashboard.html', context)

def addnewemployee(request):
    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeDetailsForm()
    return render(request, 'addnewemployee.html', {'form': form})

@login_required
def updateemployee(request, empid):
    employee = get_object_or_404(PersonalDetails, pk=empid)

    if request.method == "POST":
        form = EmployeeDetailsForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeDetailsForm(instance=employee)

    return render(request, 'updateemployee.html', {'form': form})


@login_required
def deleteemp(request, empid):
    if request.user.is_superuser or request.user.is_staff:
        # Get the specific employee to delete
        employee = get_object_or_404(PersonalDetails, pk=empid)
        employee.delete()
        return redirect('dashboard')
    else:
        return HttpResponseForbidden("You are not authorized to view this page.")


@login_required
def advanced_details(request):
    countries = [
        '',
        'Belgium',
        'Germany',
        'India',
        'Romania',
        'France',
        'Italy',
        'USA',
        'New Zealand',
        'Canada',
        'Australia',
    ]
    
    bench_classifications = ['', 'Non deployable', 'Deployable', 'Invest']
    
    regions = ['', 'Europe', 'US', 'Canada', 'Australia']
    
    categories = [
        '',
        'Category',
        'Available',
        'Allocation',
        'Future allocated',
        'Attrition',
        'Performance issue',
        'Fake',
        'Training',
        'Long Leave',
        'Billing',
        'New',
        'Practice Development',
        '30Days',
        '60Days',
        '90Days',
        'Out Of RD',
        'No Plan',
        '180Days',
    ]
    
    sub_categories = [
        '',
        'Sub category',
        'Confirmed',
        'Pending',
        'LWD Confirmed',
        'PIP',
        'Fake',
        'Planned, In progress',
        'Maternity Leave',
        'Sabbatical',
        'Medical Leave',
        'Validation in progress',
        'Training',
        'Completed',
        'No Visibility for next 90days',
        'Presales',
        'Delivery',
        'Enabling',
    ]
    
    
    talent_categories = ['', 'Billable', 'Non-Billable']

    talent_types = ['', 'Employee', 'Contract', 'Intern']

    relocations = ['', 'Yes', 'No']

    tm_spocs = ['', 'Deepti Asthana', 'Karthik Madappa', 'Arul AjitKumar', 'ManchikantiKamal VIkram', 'Sudharsan Manohar']

    sl_pocs = ['', 'Akanchha Saxena', 'Srinivasan Gurukannan', 'Arun John', 'Soma Janavikulam', 'Pratyus Tripathy', 'Avinash Bhat']

    profiles = ['', 'Yes', 'No']

    action_owners = ['', 'SL SPOC', 'CP', 'TA', 'TM']

    aging_buckets = ['', '0-30 Days', '31-60 Days', '61-90 Days', '90 Days Above']

    wfos = ['', 'Yes', 'No']
    
    
    proficiencies = ['', 'Strong', 'Medium', 'Need Training', 'Non-Deployable', 'Pending']

    experience_levels = ['', 'Fresher', '01-03', '03-06', '06-09', '09-12', '12-16', '16-19', '19+']
    
    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advanced_details_success')  # Redirect to a success page
    else:
        form = EmployeeDetailsForm()

    return render(request, 'advanced_details.html', {
        'form': form,
        'tm_spocs': tm_spocs,
        'sl_pocs': sl_pocs,
        'countries':countries,
        'bench_classifications':bench_classifications,
        'categories':categories,
        'sub_categories':sub_categories,
        'talent_categories':talent_categories,
        'talent_types':talent_types,
        'relocations':relocations,
        'profiles':profiles,
        'action_owners':action_owners,
        'aging_buckets':aging_buckets,
        'wfos':wfos,
        'proficiencies':proficiencies,
        'experience_levels':experience_levels,
        'regions':regions
          
    })
    
    
@login_required
def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'list_projects.html', {'projects': projects})

@login_required
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        start_date = request.POST.get('start_date')  # Get the start date from the form
        existing_client_id = request.POST.get('client')  # Existing client ID
        new_client_name = request.POST.get('new_client_name')  # New client name (optional)

        if new_client_name:
            new_client = Client.objects.create(name=new_client_name)
            client = new_client
        else:
            client = Client.objects.get(pk=existing_client_id)

        try:
            project = Project.objects.create(name=project_name, client=client, start_date=start_date)
            return redirect('list_projects')  # Or other appropriate redirect
        except (Client.DoesNotExist, IntegrityError) as e:
            context = {
                'error_message': str(e),
                'clients': Client.objects.all()
            }
            return render(request, 'add_project.html', context)

    else:
        clients = Client.objects.all()
        context = {'clients': clients}
        return render(request, 'add_project.html', context)



@login_required
def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.name = request.POST.get('project_name')
        client_id = request.POST.get('client')
        project.client = get_object_or_404(Client, pk=client_id)
        project.save()
        return redirect('list_projects')
    else:
        clients = Client.objects.all()
        context = {'project': project, 'clients': clients}
        return render(request, 'update_project.html', context)

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('list_projects')
    else:
        context = {'project': project}
        return render(request, 'delete_project.html', context)
    
    