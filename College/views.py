from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from Student.models import StudentInfo
from CollegeAdmin.models import CollegeAdminInfo
from Mentor.models import MentorInfo


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('acc')
        password = request.POST.get('pwd')
        match len(username):
            case 8:
                student_info = StudentInfo.objects.filter(id = username).first()
                if student_info is not None and check_password(password, student_info.password):
                    request.session['username'] = username
                    return redirect('')
            case 7:
                mentor_info = MentorInfo.objects.filter(id = username).first()
                if mentor_info is not None and check_password(password, mentor_info.password):
                    request.session['username'] = username
                    return redirect('/teacher/home')
            case 6:
                college_info = CollegeAdminInfo.objects.filter(id = username).first()
                if college_info is not None and check_password(password, college_info.password):
                    request.session['username'] = username
                    return redirect('/collegeadmin/list')
    return render(request, 'index.html')
