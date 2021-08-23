from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class RequiredLoan(models.Model):
    customer_name = models.ForeignKey(User, related_name='cutomer_required_loan', on_delete=models.CASCADE)
    provider_name = models.ForeignKey(User, related_name='provider_required_loan', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    loan_amount = models.IntegerField()
    interest = models.IntegerField()

    # def __str__(self):
    #     return self.customer_name


class AmortizationTablesForBank(models.Model):
    customer_name = models.ForeignKey(User, related_name='customer_amor_table_bank', on_delete=models.CASCADE)
    provider_name = models.ForeignKey(User, related_name='provider_amor_table_bank', on_delete=models.CASCADE)
    bank_emp = models.ForeignKey(User, related_name='emp_amor_table_bank', on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    loan_amount = models.ForeignKey(RequiredLoan, related_name='loan_atb', on_delete=models.CASCADE)
    principal = models.IntegerField()
    interest = models.IntegerField(default='12')


class AmortizationTableForProvider(models.Model):
    customer_name = models.ForeignKey(User, related_name='customer_amor_table_provider', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    loan_amount = models.ForeignKey(RequiredLoan, related_name='loan_atp', on_delete=models.CASCADE)
    principal = models.BigIntegerField()
    interest = models.IntegerField(default='12')


class AmortizationTableForCustomer(models.Model):
    provider_name = models.ForeignKey(User, related_name='providr_amor_table_customer', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    loan_amount = models.ForeignKey(RequiredLoan, related_name='loan_atc', on_delete=models.CASCADE)
    principal = models.BigIntegerField()
    interest = models.IntegerField(default='12')


class LoanFundsStatus(models.Model):
    available_fund_amount = models.BigIntegerField(default='0')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    balance = models.IntegerField()
    type = models.TextField(max_length=15)

    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
