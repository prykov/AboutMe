from django.core.management.base import BaseCommand
from mainapp.models import Work, Hobby, Study, Organization

class Command(BaseCommand):
	help = 'Fill DB new data'

	def handle(self, *args, **option):
		organizations = [
			{'name': 'Организация1', 'phone_number': '+7-999-123-456', 'region': 'г. Москва', 'site': '/org1'},
			{'name': 'Организация2', 'phone_number': '+7-999-123-654', 'region': 'г. Красноярск', 'site': '/org2'}
		]
		works = [
			{'organization': 'Организация1', 'post': 'Рыбочий', 'desc': 'работал', 'period': 2},
			{'organization': 'Организация1', 'post': 'Рыбочий', 'desc': 'работал', 'period': 4},
			{'organization': 'Организация2', 'post': 'Рыбочий', 'desc': 'работал', 'period': 3}
		]
		hobbies = [
			{'name': 'Автомобили', 'year': '2008'},
			{'name': 'Путешествия', 'year': '2011'}
		]
		studies = [
			{'name': 'Сибирский федеральный университет', 'spec': 'Программная инженерия'},
			{'name': 'GeekBrains', 'spec': 'Web-разработчик python/django'}
		]

		Organization.objects.all().delete()
		for organization in organizations:
			organization = Organization(**organization)
			organization.save()

		Work.objects.all().delete()
		for work in works:
			org_name = work["organization"]
			# Получаем организацию по имени
			organization = Organization.objects.get(name=org_name)
			# Заменяем название организации объектом
			work['organization'] = organization
			work = Work(**work)
			work.save()		

		Hobby.objects.all().delete()
		for hobby in hobbies:
			hobby = Hobby(**hobby)
			hobby.save()		

		Study.objects.all().delete()
		for study in studies:
			study = Study(**study)
			study.save()

		print('Команда выполнена')