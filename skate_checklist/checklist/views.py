from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Type, Skill, Point, Star


@login_required
def type(request):
    type_list = Type.objects.all()
    context = {'type_list':type_list}
    return render(request, 'checklist/type.html', context)

@login_required
def skill(request, type_id):
    type = Type.objects.filter(id=type_id).prefetch_related('skill')[0]
    skill_list = Skill.objects.filter(type__id=type_id).all()
    context = {'type':type, 'skill_list':skill_list}
    return render(request, 'checklist/skill.html', context)

@login_required
def point(request, type_id, skill_id):
    type = Type.objects.filter(id=type_id).all()[0]
    skill = Skill.objects.filter(id=skill_id).all()[0]
    point_list = Point.objects.filter(skill__id=skill_id).all()
    star_dict = {}
    for point in point_list:
        try:
            star = Star.objects.filter(user=request.user, point=point).all()[0].star
        except IndexError:
            star = 0
        star_dict[point.point_text]=star
    
    context = {'type':type, 'skill':skill, 'point_list':point_list, 'star_dict':star_dict}
    return render(request, 'checklist/point.html', context)

@login_required
def check(request, type_id, skill_id):
    type_list = Type.objects.filter(id=type_id).all()
    skill_list = Skill.objects.filter(id=skill_id).all()
    point_list = Point.objects.filter(skill__id=skill_id).all()
    user = request.user

    for point in point_list:
        try:
            star = request.POST[point.point_text]
        except:
            star = 0
        Star.objects.update_or_create(point=point, user=user, defaults={'star':int(star)})
    
    return redirect("checklist:point", type_id=type_id, skill_id=skill_id)

@login_required
def result(request):
    pass
