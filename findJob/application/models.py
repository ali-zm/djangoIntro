from django.db import models

# Create your models here.
class Application(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    salary = models.IntegerField()
    createdTime = models.DateTimeField(auto_now_add=True)
    expirationTime = models.DateTimeField(null=True, default=None, blank=True)
    employer = models.ForeignKey("employer.Employer", on_delete=models.CASCADE, null=True, default=None)
    applicant = models.OneToOneField("applicant.Applicant", on_delete=models.DO_NOTHING, null=True, default=None, blank=True)

    def __str__(self) -> str:
        return self.title+" " + str(self.salary)

