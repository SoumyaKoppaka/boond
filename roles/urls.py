from django.urls import include, path
from .views import donors, all_roles

app_name = 'roles'

urlpatterns = [

    path('', all_roles.home, name='home'),

    path('donor/', include(([
                                path('', donors.DonorHomeView.as_view(), name='donor_home'),
                            ], 'roles'), namespace='donor')),

    path('recipient/', include(([
                                    path('', donors.DonorHomeView.as_view(), name='recipient_home'),
                                ], 'roles'), namespace='recipient')),

    path('bloodBank/', include(([
                                    path('', donors.DonorHomeView.as_view(), name='blood_bank_home'),
                                ], 'roles'), namespace='blood_bank')),

    path('hospital/', include(([
                                   path('', donors.DonorHomeView.as_view(), name='hospital_home'),
                               ], 'roles'), namespace='hospital')),

    path('localBodies/', include(([
                                      path('', donors.DonorHomeView.as_view(), name='local_bodies_home'),
                                  ], 'roles'), namespace='local_bodies')),

]
