from django.urls import include, path
from .views import donors, all_roles,local_bodies, hospitals
from django.conf.urls import url


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
                                   path('reserveBlood', hospitals.reserve_blood, name='hospital_reserve_blood'),
                                   path('search', hospitals.search, name='hospital_search'),
                                   url(r'^search/(?P<slug>[^\/]+)$', hospitals.block_blood, name='hospital_block_blood'),

                               ], 'roles'), namespace='hospital')),

    path('localBodies/', include(([
                                      path('', donors.DonorHomeView.as_view(), name='local_bodies_home'),
                                      path('uploadEvents', local_bodies.uploadEvent, name='uploadEvents'),

                                  ], 'roles'), namespace='local_bodies')),

]
