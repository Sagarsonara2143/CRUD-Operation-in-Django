from django.db import models

class Student(models.Model):
	roll_no = models.PositiveSmallIntegerField()
	f_name = models.CharField(max_length = 100)
	l_name = models.CharField(max_length = 100)
	percentage = models.PositiveSmallIntegerField()

	def _str__(self):
		return self.f_name + " " + sef.l_name