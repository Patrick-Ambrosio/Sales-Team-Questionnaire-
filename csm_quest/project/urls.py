from django.urls import path
from . import views
#from .views import CreateMyModelView

urlpatterns = [
    path('', views.csm_view),
    path('firstparty/',views.firstparty),
    path('CRM/',views.CRM),
    path('thirdparty/',views.thirdparty)

]