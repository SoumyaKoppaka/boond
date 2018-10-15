from django.contrib import admin

from .models import BloodDonationEvent,User,Donor,Recipient,Hospital,BloodBank,LocalBodies, Request, Blood

# Register your models here.
admin.site.register(BloodDonationEvent)
admin.site.register(User)
admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Hospital)
admin.site.register(BloodBank)
admin.site.register(LocalBodies)
admin.site.register(Request)
admin.site.register(Blood)
admin.site.register(BloodDonationEvent)
