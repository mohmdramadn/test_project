from django.contrib import admin
from .models import AmortizationTablesForBank, AmortizationTableForProvider, AmortizationTableForCustomer, RequiredLoan
from .models import Profile
# Register your models here.
admin.site.register(AmortizationTablesForBank)
admin.site.register(AmortizationTableForCustomer)
admin.site.register(AmortizationTableForProvider)
admin.site.register(RequiredLoan)
admin.site.register(Profile)
