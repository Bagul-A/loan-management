from django.urls import path
from . import views

urlpatterns = [
    path('api/get-statement',views.getStatement),
    path('api/register-user',views.registerUser),
    path('api/apply-loan',views.applyLoan),
    path('api/make-payment',views.makePayment),
]