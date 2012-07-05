from django.db.models.aggregates import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from student.models import Group, Student
from student.forms import GroupForm, StudentForm


def groups(request):
    groups = Group.objects.all().annotate(students_cnt=Count('student'))
    return render_to_response('groups.html', {'groups': groups},
                              RequestContext(request))


def manage_group(request, group_id=None):
    if group_id:
        instance = Group.objects.get(id=group_id)
    else:
        instance = None

    form = GroupForm(instance=instance)

    if request.POST:
        form = GroupForm(request.POST, instance=instance)
        form.save()
        return HttpResponseRedirect(reverse("groups"))

    return render_to_response('manage_groups.html', {'form': form},
                              RequestContext(request))


def del_group(request, group_id=None):
    Group.objects.get(id=group_id).delete()
    return HttpResponseRedirect(reverse("groups"))


def students(request, group_id):
    group = Group.objects.get(id=group_id)
    students = Student.objects.filter(group=group_id)
    paginator = Paginator(students, 1)

    page = request.GET.get('page')

    try:
        students= paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render_to_response('students.html',
                              {'students': students, 'group': group},
                              RequestContext(request))


def manage_student(request, group_id, student_id=None):
    if student_id:
        instance = Student.objects.get(id=student_id)
    else:
        instance = None

    form = StudentForm(instance=instance)

    if request.POST:
        form = StudentForm(request.POST, request.FILES, instance=instance)
        form.save()
        return HttpResponseRedirect(reverse("students", args=[group_id]))

    return render_to_response('manage_student.html',
                              {'form': form},
                              RequestContext(request))


def del_student(request, group_id, student_id=None):
    Student.objects.get(id=student_id).delete()
    return HttpResponseRedirect(reverse("students", args=[group_id]))

