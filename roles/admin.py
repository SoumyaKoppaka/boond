from django.contrib import admin
from .models import BloodDonationEvent,User,Donor,Recipient,Hospital,BloodBank,LocalBodies
# Register your models here.
admin.site.register(BloodDonationEvent)
admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Hospital)
admin.site.register(BloodBank)
admin.site.register(LocalBodies)