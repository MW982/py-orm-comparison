from django.db import models


class Country(models.Model):
    founding_date = models.DateField()
    name = models.CharField(max_length=200)
    description = models.TextField()

    number = models.IntegerField()

    class Meta:
        db_table = "country"


class Area(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey("testmodels.Country", on_delete=models.CASCADE)

    class Meta:
        db_table = "area"


class Citizen(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    area = models.ForeignKey("testmodels.Area", on_delete=models.CASCADE)
    facility = models.ForeignKey(
        "testmodels.GovernmentFacility", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "citizen"


class GovernmentFacility(models.Model):
    name = models.CharField(max_length=200)

    identifing_uuid = models.UUIDField()
    area = models.ForeignKey("testmodels.Area", on_delete=models.CASCADE)

    class Meta:
        db_table = "government_facility"
