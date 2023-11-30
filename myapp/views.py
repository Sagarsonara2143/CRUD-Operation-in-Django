from django.shortcuts import render, redirect
from . models import Student

def index(request):
	if request.method == "POST":
		roll_no = request.POST['roll_no']
		f_name = request.POST['f_name']
		l_name = request.POST['l_name']
		percentage = request.POST['percentage']

		stu = Student(roll_no=roll_no, f_name=f_name, l_name = l_name, percentage=percentage)
		stu.save()
		students = Student.objects.all()
		return render (request,"index.html",{'students':students})
	else:
		students = Student.objects.all()
		return render (request,"index.html",{'students':students})

def delete(request,pk):
	roll_no = Student.objects.get(pk=pk)
	roll_no.delete()
	return redirect ('index')

def update(request,pk):
	if request.method == "POST":
		roll_no = Student.objects.get(pk=pk)
		roll_no = request.POST['roll_no']
		f_name = request.POST['f_name']
		l_name = request.POST['l_name']
		percentage = request.POST['percentage']
		stu = Student(roll_no=roll_no, f_name=f_name, l_name = l_name, percentage=percentage)
		stu.save()
		students = Student.objects.all()
		return render (request,"index.html",{'students':students})
	else:
		roll_no = Student.objects.get(pk=pk)
		return render(request,"update.html",{'roll_no':roll_no})