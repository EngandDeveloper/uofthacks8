from django.contrib import admin
from split.models import SharedExp, PendingPay
# Register your models here.
admin.site.register(SharedExp)
admin.site.register(PendingPay)