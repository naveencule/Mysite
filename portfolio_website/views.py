from django.shortcuts import render
from .models import Education, Skill, Experience, Project, Contact

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        contact_success = True
    else:
        contact_success = False

    education_list = Education.objects.all()
    skill_list = Skill.objects.all()
    experience_list = Experience.objects.all()
    project_list = Project.objects.all()

    return render(request, 'home.html', {
        'education': education_list,
        'skills': skill_list,
        'experience': experience_list,
        'projects': project_list,
        'contact_success': contact_success,
    })
