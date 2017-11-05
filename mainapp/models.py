from django.db import models

class Organization(models.Model):
	name = models.CharField(verbose_name='Название', max_length=32, unique=True)
	phone_number = models.CharField(verbose_name='Номер телефона', max_length=14)
	region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
	site = models.URLField(verbose_name='Сайт', blank=True, db_index=True)

	def __str__(self):
		return self.name

class Work(models.Model):
	organization = models.ForeignKey(Organization, verbose_name='Организация', null=True)
	post = models.CharField(max_length=32, verbose_name='Должность')
	desc = models.TextField(verbose_name='Описание')
	period = models.PositiveIntegerField()
	site = models.URLField(verbose_name='Сайт',blank=True, db_index=True)
	
	def __str__(self):
		return self.post;

class Study(models.Model):
	name = models.CharField(max_length=32)
	spec = models.CharField(max_length=32)

class Hobby(models.Model):
	name = models.CharField(max_length=32)
	year = models.PositiveIntegerField()
		