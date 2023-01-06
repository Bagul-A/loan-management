from django.db import models

# Create your models here.

class User(models.Model):
    aadhar_id = models.CharField(max_length=15, default = 0)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    annual_income = models.IntegerField()
    credit_score = models.IntegerField(default=0)

class Loan(models.Model):
    user_id = models.IntegerField(default=-1)
    loan_type = models.TextChoices('loan_type', 'CAR HOME EDUCATIONAL PERSONAL')
    loan_amount = models.IntegerField()
    repayment_amount = models.IntegerField(default=0)
    intrest_rate = models.IntegerField()
    term_period = models.IntegerField()
    disbursement_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

class Transaction(models.Model):
    user_id = models.IntegerField()
    loan_id = models.IntegerField()
    amount_paid = models.IntegerField()
    principal = models.IntegerField()
    interest = models.IntegerField()
    paid_on = models.DateTimeField(auto_now_add=True)
    emi_count = models.IntegerField()






# {
#     "name":"john",
#     "email":"john@gmail.com",
#     "annual_income":20000
# }