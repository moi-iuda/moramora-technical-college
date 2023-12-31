from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('department/<str:pk>/', views.department, name='department'),
    path('programmes/', views.programmes, name='programmes'),
    path('programme/<str:pk>/', views.programme, name='programme'),
    path('latest_updates/', views.latest_updates, name='latest_updates'),
    path('latest_update/<str:pk>/', views.latest_update, name='latest_update'),
    path('notices/', views.notices, name='notices'),
    path('notice/<str:pk>/', views.notice, name='notice'),
    path('acadcalendar_fees_contact/', views.acadcalendar_fees_contact,
         name='acadcalendar_fees_contact'),
    path('trades/',
         views.trades, name='trades'),
    path('trade_images/<str:pk>/',
         views.trade_images, name='trade_images'),
    path('add_department/',
         views.add_department, name='add_department'),
    path('add_academic_calendar/',
         views.add_academic_calendar, name='add_academic_calendar'),
    path('add_fees/',
         views.add_fees, name='add_fees'),
    path('add_contact/',
         views.add_contact, name='add_contact'),
    path('add_institution/',
         views.add_institution, name='add_institution'),
    path('add_latest_update/',
         views.add_latest_update, name='add_latest_update'),
    path('add_notice/',
         views.add_notice, name='add_notice'),
    path('add_programme/',
         views.add_programme, name='add_programme'),
    path('add_trade_image/',
         views.add_trade_image, name='add_trade_image'),
    path('add_trade/',
         views.add_trade, name='add_trade'),
    path('update_trade/<str:pk>/',
         views.update_trade, name='update_trade'),
    path('update_trade_image/<str:pk>/',
         views.update_trade_image, name='update_trade_image'),
    path('update_department/<str:pk>/',
         views.update_department, name='update_department'),
    path('update_academic_calendar/<str:pk>/',
         views.update_academic_calendar, name='update_academic_calendar'),
    path('update_fees/<str:pk>/',
         views.update_fees, name='update_fees'),
    path('update_contact/<str:pk>/',
         views.update_contact, name='update_contact'),
    path('update_institution/<str:pk>/',
         views.update_institution, name='update_institution'),
    path('update_latest_update/<str:pk>/',
         views.update_latest_update, name='update_latest_update'),
    path('update_notice/<str:pk>/',
         views.update_notice, name='update_notice'),
    path('update_programme/<str:pk>/',
         views.update_programme, name='update_programme'),
    path('login_user/',
         views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('delete_department/<str:pk>/',
         views.delete_department, name='delete_department'),
    path('delete_programme/<str:pk>/',
         views.delete_programme, name='delete_programme'),
    path('delete_latest_update/<str:pk>/',
         views.delete_latest_update, name='delete_latest_update'),
    path('delete_notice/<str:pk>/',
         views.delete_notice, name='delete_notice'),
    path('delete_trade/<str:pk>/',
         views.delete_trade, name='delete_trade'),
]
