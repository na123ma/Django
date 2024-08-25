from django.shortcuts import render ,get_object_or_404, redirect
from django . http import HttpResponse
from django . template import loader
from . forms import BatchForm
from . forms import CourseForm
from . forms import ExamForm
from . forms import PaperForm
from . forms import SemForm
from . models import BatchMaster
from . models import PaperMaster
from . models import CourseMaster
from . models import SemMaster
from . models import ExamMaster
from . models import StudentMaster
from . models import StudentInternalTransMaster


# Create your views here.
def display_Batch(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template('all_batch.html')
    context={
        'data':allbatch,
        }
    return HttpResponse(temp.render(context,request))
def print_Batch(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template('print_batch.html')
    context={
        'data':allbatch,
        }
    return HttpResponse(temp.render(context,request))


def display_Student(request):
    allstu=BatchMaster.objects.all().values()
    temp=loader.get_template('all_student.html')
    context={
        'data':allstu,
        }
    return HttpResponse(temp.render(context,request))
def display_Paper(request):
    allpaper=PaperMaster.objects.all().values()
    temp=loader.get_template('all_paper.html')
    context={
        'data':allpaper,
        }
    return HttpResponse(temp.render(context,request))
def display_Sem(request):
    allsem=SemMaster.objects.all().values()
    temp=loader.get_template('all_sem.html')
    context={
        'data':allsem,
        }
    return HttpResponse(temp.render(context,request))
def display_Exam(request):
    allexam=ExamMaster.objects.all().values()
    temp=loader.get_template('all_exam.html')
    context={
        'data':allexam,
        }
    return HttpResponse(temp.render(context,request))
def display_Course(request):
    allcourse=CourseMaster.objects.all().values()
    temp=loader.get_template('all_course.html')
    context={
        'data':allcourse,
        }
    return HttpResponse(temp.render(context,request))



def display_StudentTrans(request):
    allstudent=StudentInternalTransMaster.objects.all().values()
    temp=loader.get_template('all_trans.html')
    context={
        'data':allstudent,
        }
    return HttpResponse(temp.render(context,request))
def display_image(request):
    return render(request,"homepage.html")

def Batch_view(request):
    context={}
    context['form']=BatchForm()
    return render(request,"batch_view.html",context)
def displayBatchInput(request):
    return render(request,'batch_entry.html')
def process_batch_entry(request):
    if request.method== 'POST':
        batchNo_inp=int(request.POST.get('batchNo'))
        batchId_inp=request.POST.get('batchId')
        ob=BatchMaster(batchNo=batchNo_inp,batchId=batchId_inp)
        ob.save()
        return render(request,'retrive.html')
        
    else:
        return HttpResponse("invalid request method...")
    
def Exam_view(request):
    context={}
    context['form']=ExamForm()
    return render(request,"exam_view.html",context)
def displayExamInput(request):
    return render(request,'exam_entry.html')
def process_exam_entry(request):
    if request.method== 'POST':
        examId_inp=int(request.POST.get('examId'))
        examType_inp=request.POST.get('examType')
        ob=ExamMaster(examId=examId_inp,examType=examType_inp)
        ob.save()
        return render(request,'retrive.html')

    else:
        return HttpResponse("invalid request method...")
    
def Course_view(request):
    context={}
    context['form']=CourseForm()
    return render(request,"course_view.html",context)
def displayCourseInput(request):
    return render(request,'course_entry.html')
def process_course_entry(request):
    if request.method== 'POST':
        course_inp=request.POST.get('course')
        courseId_inp=request.POST.get('courseId')
        ob=CourseMaster(course=course_inp,courseId=courseId_inp)
        ob.save()
        return render(request,'retrive.html')
        
    else:
        return HttpResponse("invalid request method...")
    
def Paper_view(request):
    context={}
    context['form']=PaperForm()
    return render(request,"exam_view.html",context)
def displayPaperInput(request):
    return render(request,'exam_entry.html')
def process_paper_entry(request):
    if request.method== 'POST':
        paperCode_inp=request.POST.get('paperCode')
        papertype_inp=request.POST.get('papertype')
        paperShtName_inp=request.POST.get('paperShtName')
        paperName_inp=request.POST.get('paperName')
        ob=PaperMaster(paperCode=paperCode_inp,papertype=papertype_inp,paperShtName=paperShtName_inp,paperName=paperName_inp)
        ob.save()
        return render(request,'retrive.html')
        
    else:
        return HttpResponse("invalid request method...")
    
def Sem_view(request):
    context={}
    context['form']=SemForm()
    return render(request,"sem_view.html",context)
def displaySemInput(request):
    return render(request,'sem_entry.html')
def process_sem_entry(request):
    if request.method== 'POST':
        sem_inp=request.POST.get('sem')
        semId_inp=int(request.POST.get('semId'))
        ob=SemMaster(sem=sem_inp,semId=semId_inp)
        ob.save()
        return render(request,'retrive.html')        
    else:
        return HttpResponse("invalid request method...")

def Student_view(request):
    context={}
    context['form']=StudentForm()
    return render(request,"student_view.html",context)
def displayStudentInput(request):
    return render(request,'student_entry.html')
       
def process_student_entry(request):
    if request.method== 'POST':
        sem_inp=request.POST.get('sem')
        semId_inp=int(request.POST.get('semId'))
        ob=StudentMaster(sem=sem_inp,semId=semId_inp)
        ob.save()
        return render(request,'retrive.html')        
    else:
        return HttpResponse("invalid request method...")


def delete(request,pk):
    BatchMaster.objects.filter(id=pk).delete()
    return render(request,"retrieve1.html")

def delete_Batch(request):
    allbatch=BatchMaster.objects.all().values()
    temp=loader.get_template('delete_batch.html')
    context={
        'data':allbatch,
        }
    return HttpResponse(temp.render(context,request))
    
def delete1(request,pk):
    CourseMaster.objects.filter(id=pk).delete()
    return render(request,"retrieve2.html")
def delete_Course(request):
    allcourse=CourseMaster.objects.all().values()
    temp=loader.get_template('delete_course.html')
    context={
        'data':allcourse,
        }
    return HttpResponse(temp.render(context,request))

def delete2(request,pk):
    PaperMaster.objects.filter(id=pk).delete()
    return render(request,"retrieve3.html")

def delete_Paper(request):
    allpaper=PaperMaster.objects.all().values()
    temp=loader.get_template('delete_paper.html')
    context={
        'data':allpaper,
        }
    return HttpResponse(temp.render(context,request))
def delete3(request,pk):
    ExamMaster.objects.filter(id=pk).delete()
    return render(request,"retrieve4.html")
def delete_Exam(request):
    allexam=ExamMaster.objects.all().values()
    temp=loader.get_template('delete_exam.html')
    context={
        'data':allexam,
        }
    return HttpResponse(temp.render(context,request))
def delete4(request,pk):
    SemMaster.objects.filter(id=pk).delete()
    return render(request,"retrieve5.html")
def delete_Sem(request):
    allsem=SemMaster.objects.all().values()
    temp=loader.get_template('delete_sem.html')
    context={
        'data':allsem,
        }
    return HttpResponse(temp.render(context,request))
from .forms import SearchForm

def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = BatchMaster.objects.filter(batchId=query)  
        else:
            results = None
    else:
        form = SearchForm()
        results = None
    
    return render(request, 'search_results.html', {'form': form, 'results': results})
def search_view1(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = CourseMaster.objects.filter(courseId=query)  
        else:
            results = None
    else:
        form = SearchForm()
        results = None
    
    return render(request, 'search_results1.html', {'form': form, 'results': results})
def search_view2(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = PaperMaster.objects.filter(paperCode=query)  
        else:
            results = None
    else:
        form = SearchForm()
        results = None
    
    return render(request, 'search_results2.html', {'form': form, 'results': results})
def search_view3(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = ExamMaster.objects.filter(examId=query)  
        else:
            results = None
    else:
        form = SearchForm()
        results = None
    
    return render(request, 'search_results3.html', {'form': form, 'results': results})
def search_view4(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = SemMaster.objects.filter(semId=query)  
        else:
            results = None
    else:
        form = SearchForm()
        results = None
    
    return render(request, 'search_results4.html', {'form': form, 'results': results})

def edit_batch(request, batch_id):
    batch = get_object_or_404(BatchMaster, pk=batch_id)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('batch_detail', batch_id=batch_id)
    else:
        form = BatchForm(instance=batch)
    
    return render(request, 'edit_batch.html', {'form': form})

def batch_detail(request, batch_id):
    batch = get_object_or_404(BatchMaster, pk=batch_id)
    return render(request, 'batch_detail.html', {'batch': batch})

def batch_all_details(request):
    ob=BatchMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('batch_all_details.html')
    return HttpResponse(temp.render(context,request))

#coursemasterupdate
def edit_course(request,course_id):
    course = get_object_or_404(CourseMaster, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course_id)
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'edit_course.html', {'form': form})

def course_detail(request,course_id):
    course = get_object_or_404(CourseMaster, pk=course_id)
    return render(request, 'course_detail.html', {'course': course})
def course_all_details(request):
    ob=CourseMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('course_all_details.html')
    return HttpResponse(temp.render(context,request))
#Papermasterupdate
def edit_paper(request,paper_id):
    paper = get_object_or_404(PaperMaster, pk=paper_id)
    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('paper_detail', paper_id=paper_id)
    else:
        form = PaperForm(instance=paper)
    
    return render(request, 'edit_paper.html', {'form': form})
def paper_detail(request,paper_id):
    paper = get_object_or_404(PaperMaster, pk=paper_id)
    return render(request, 'paper_detail.html', {'paper': paper})
def paper_all_details(request):
    ob=PaperMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('paper_all_details.html')
    return HttpResponse(temp.render(context,request))
#exam masterupdate
def edit_exam(request,exam_id):
    exam = get_object_or_404(ExamMaster, pk=exam_id)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam_detail', exam_id=exam_id)
    else:
        form = ExamForm(instance=exam)
    
    return render(request, 'edit_exam.html', {'form': form})   

def exam_detail(request,exam_id):
   exam = get_object_or_404(ExamMaster, pk=exam_id)
   return render(request, 'exam_detail.html', {'exam': exam})
def exam_all_details(request):
    ob=ExamMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('exam_all_details.html')
    return HttpResponse(temp.render(context,request))
#semmaster update
def edit_sem(request,sem_id):
    sem = get_object_or_404(SemMaster, pk=sem_id)
    if request.method == 'POST':
        form = SemForm(request.POST, instance=sem)
        if form.is_valid():
            form.save()
            return redirect('sem_detail', sem_id=sem_id)
    else:
        form = SemForm(instance=sem)
    return render(request, 'edit_sem.html', {'form': form}) 
def sem_detail(request,sem_id):
   sem = get_object_or_404(SemMaster, pk=sem_id)
   return render(request, 'sem_detail.html', {'sem': sem})
def sem_all_details(request):
    ob=SemMaster.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('sem_all_details.html')
    return HttpResponse(temp.render(context,request))