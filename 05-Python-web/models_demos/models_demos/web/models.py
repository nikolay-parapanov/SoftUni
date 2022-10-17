from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30)


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30)
    last_name = models.CharField(
        max_length=40)
    email_address = models.EmailField()
    works_full_time = models.BooleanField()
    job_level = models.CharField(
        max_length=20,
        choices=(
            ('Jr.', 'Junior'),
            ('Reg', 'Regular'),
            ('Sr.', 'Senior')
        ),
        verbose_name="Seniority level")
    photo = models.URLField()
    birth_date = models.DateField
    start_date = models.DateField
    review = models.CharField(
        max_length=100,
        null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'ID: {self.pk};  Name: {self.first_name} {self.last_name}'

