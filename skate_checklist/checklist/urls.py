from django.urls import path

from . import views

app_name = 'checklist'
urlpatterns = [
    # ex: /checklist/
    path('checklist/', views.type, name='type'),
        # ex: /checklist/3/
    path('checklist/<int:type_id>/', views.skill, name='skill'),
        # ex: /checklist/3/2/
    path('checklist/<int:type_id>/<int:skill_id>/', views.point, name='point'),

    path('checklist/<int:type_id>/<int:skill_id>/check', views.check, name='check'),

    path('checklist/<int:type_id>/<int:skill_id>/result', views.result, name='result'),
    ]