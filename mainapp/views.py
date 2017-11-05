from django.shortcuts import render, render_to_response
from .models import Work, Study, Hobby, Organization


def main(request):
	name = "павел"
	surname = "рыков"
	middle_name = "геннадьевич"
	hobbys = Hobby.objects.all()
	return render_to_response('index.html',{'name':name, \
		'surname': surname, \
		'middle_name' : middle_name, \
		'hobbys': hobbys})


def education(request):
	page = "education"
	study_places = Study.objects.all()
	return render_to_response('education.html', {'page' : page, 'study_places' : study_places})

def work(request):
	page = 'work'
	work_places = Work.objects.all()
	return render_to_response('work.html', {'page' : page, 'work_places': work_places})

def organization(request, org):
	org = Organization.objects.get(site=org)
	return render_to_response('organization.html', {'org': org})