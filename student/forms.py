from django.forms.models import ModelForm

from student.models import Student, Group


class StudentForm(ModelForm):
    class Meta:
        model = Student


class GroupForm(ModelForm):
    class Meta:
        model = Group