from django.shortcuts import render
from .models import (
    Skill, Language, Certification, Education,
    WorkExperience, Project, Interest, PersonalInfo, Quote
)
from django.contrib.auth.models import User


def home(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        user, _ = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'example@example.com'}
        )
        personal_info = PersonalInfo.objects.create(
            user=user,
            job_title='Full Stack Developer | Software Engineer',
            location='City, Country',
            email='example@example.com',
            phone='+1234567890'
        )

    # جلب الاقتباس النشط فقط
    quote = Quote.objects.filter(is_active=True).first()

    context = {
        'personal_info': personal_info,
        'skills': Skill.objects.all().order_by('order'),
        'languages': Language.objects.all(),
        'certifications': Certification.objects.all().order_by('order', '-date_obtained'),
        'education': Education.objects.all().order_by('-start_date'),
        'experiences': WorkExperience.objects.all().order_by('-start_date'),
        'projects': Project.objects.filter(is_featured=True).order_by('order'),  # ✅ featured فقط
        'interests': Interest.objects.all(),
        'quote': quote,  # ✅ جديد
    }

    return render(request, 'home.html', context)