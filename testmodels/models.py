from django.db import models


class Country(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = {
        FRESHMAN: "Freshman",
        SOPHOMORE: "Sophomore",
        JUNIOR: "Junior",
        SENIOR: "Senior",
        GRADUATE: "Graduate",
    }

    date = models.DateTimeField(auto_now=True)
    number = models.IntegerField()
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )


class Area(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey("testmodels.Country", on_delete=models.CASCADE)


class Citizen(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    area = models.ForeignKey("testmodels.Area", on_delete=models.CASCADE)
    facility = models.ForeignKey(
        "testmodels.GovernmentFacility", on_delete=models.CASCADE
    )


class GovernmentFacility(models.Model):
    area = models.ForeignKey("testmodels.Area", on_delete=models.CASCADE)
