import os
from django.conf.urls import patterns, include, url

from django.contrib import admin
from studentsdb import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'student.views.groups', name='groups'),
    url(r'^group/(?P<group_id>\d+)/$', 'student.views.students',
        name='students'),
    url(r'^group/add/$', 'student.views.manage_group',
        name='add_group'),
    url(r'^group/edit/(?P<group_id>\d+)/$',
        'student.views.manage_group', name='edit_group'),
    url(r'^group/delete/(?P<group_id>\d+)/$',
        'student.views.del_group', name='del_group'),
    url(r'^group/(?P<group_id>\d+)/student/add/$',
        'student.views.manage_student', name='add_student'),
    url(r'^group/(?P<group_id>\d+)/student/(?P<student_id>\d+)/$',
        'student.views.manage_student', name='edit_student'),
    url(r'^group/(?P<group_id>\d+)/student/delete/(?P<student_id>\d+)/$',
        'student.views.del_student', name='del_student'),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': os.path.join(settings.PROJECT_ROOT, '../uploads')}
        )
    )
