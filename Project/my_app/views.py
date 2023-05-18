from django.shortcuts import render
from django.http import HttpResponseRedirect
# from my_app.models import Methodological_materials, Photo
from .forms import CoursesForm
from .models import Courses, Institutions

from django.views.generic import ListView

# Create your views here.
 
def index(request):
    return render(request, 'my_app/index.html')

def student(request):
    student_courses = Courses.objects.all()
    institution_list = Institutions.objects.all()
    return render(request, 'my_app/student.html', {
        'institution_list': institution_list,
        'student_courses': student_courses,
    })

def admin(request):
    admin_courses = Courses.objects.all()
    return render(request, 'my_app/admin.html', {
        'admin_courses': admin_courses
    })

def teachers(request):
    teach_courses = Courses.objects.all()
    if request.method == 'POST':
        courses_form = CoursesForm(request.POST)

        if courses_form.is_valid(): 
            course = courses_form()
            course.course_name = courses_form.cleaned_data['course_name']
            course.category = courses_form.cleaned_data['category']
            course.info = courses_form.cleaned_data['info']
            if 'image' in request.FILES:
                course.image = request.FILES['image']
            course.duration = courses_form.cleaned_data['duration']
            course.price = courses_form.cleaned_data['price']
            course.save()
            courses_form = course()
            return HttpResponseRedirect('/')
        
        else:
            print(courses_form.errors)

    else:
        courses_form = CoursesForm()

    return render(request, 'my_app/teacher.html', {
        'courses_form': courses_form,
        'teach_courses': teach_courses,
    })

class TeacherListView(ListView):
    model = Courses
    template_name = 'my_app/teacher.html'
    queryset = Courses.objects.all()
    # def get_queryset(self):
    #     return Courses.objects.all()

class StudentListView(ListView):
    model = Courses
    template_name = 'my_app/student.html'
    queryset = Courses.objects.all()