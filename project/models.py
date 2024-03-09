from django.db import models

from core.models import User

# Create your models here.

class Company(models.Model):
    fax = models.CharField(max_length=50)
    website = models.URLField()
    no_of_employee = models.IntegerField()
    private = models.BooleanField(default=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    education_level = models.CharField(max_length=100)
    working_field = models.CharField(max_length=255)
    current_position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year_at_company = models.IntegerField()

    def __str__(self) -> str:
        return self.user.email

class KnowledgeArea(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    STAGE_CHOICES = (
        ('standardize', 'Standardize'),
        ('measure', 'Measure'),
        ('control', 'Control'),
        ('improve', 'Improve'),
        ('humanresources', 'Human Resources'),
        ('cultural', 'Cultural'),
        ('technological', 'Technological'),
        ('structural', 'Structural'),
    )
    DOMAIN_CHOICES = (
        ('program', 'Program'),
        ('project', 'Project'),
        ('portfolio', 'Portfolio'),
        ('oe', 'OE'),
    )
    PROCESS_CHOICES = (
        ('Initiating', 'Initiating'),
        ('Planning', 'Planning'),
        ('Integration Management', 'Integration Management'),
        ('Executing', 'Executing'),
        ('Monitoring and Controlling', 'Monitoring and Controlling'),
        ('Closing', 'Closing'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    process_group = models.CharField(max_length=50, choices=PROCESS_CHOICES, null=True, blank=True)
    knowledge_area = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Result(models.Model):
    STAGE_CHOICES = (
        ('standardize', 'Standardize'),
        ('measure', 'Measure'),
        ('control', 'Control'),
        ('improve', 'Improve'),
        ('humanresources', 'Human Resources'),
        ('cultural', 'Cultural'),
        ('technological', 'Technological'),
        ('structural', 'Structural'),
    )
    DOMAIN_CHOICES = (
        ('program', 'Program'),
        ('project', 'Project'),
        ('portfolio', 'Portfolio'),
        ('oe', 'OE'),
    )
    PROCESS_CHOICES = (
        ('Initiating', 'Initiating'),
        ('Planning', 'Planning'),
        ('Integration Management', 'Integration Management'),
        ('Executing', 'Executing'),
        ('Monitoring and Controlling', 'Monitoring and Controlling'),
        ('Closing', 'Closing'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    domain = models.CharField(max_length=20, choices=DOMAIN_CHOICES, null=True, blank=True)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, null=True, blank=True)
    process_group = models.CharField(max_length=50, choices=PROCESS_CHOICES, null=True, blank=True)
    knowledge_area = models.ForeignKey(KnowledgeArea, on_delete=models.CASCADE, null=True, blank=True)
    result = models.IntegerField()
    total_number = models.IntegerField()



    def __str__(self) -> str:
        return f"{self.company} {self.employee}"