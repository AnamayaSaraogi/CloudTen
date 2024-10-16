from django.db import models
class labtest(models.Model):
    uno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.IntegerField()
    address=models.TextField(max_length=200)
    email=models.CharField(max_length=50)
    tests=models.CharField(max_length=50)

    class Meta:
         db_table="labtest"

class appointment(models.Model):
    unique_number=models.IntegerField(primary_key=True)
    patient_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    phone_number=models.CharField(max_length=10)
    address=models.TextField(max_length=200)
    appointment_time=models.TimeField()
    doctor_name=models.CharField(max_length=50)
    class Meta:
         db_table="appointmentsct"