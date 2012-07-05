from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    middle_name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos', blank=True)
    birth_day = models.DateField()
    number_ticket = models.IntegerField()
    group = models.ForeignKey('Group')

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    group_name = models.CharField(max_length=120)
    elder = models.OneToOneField(Student, related_name='elder', blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.group_name