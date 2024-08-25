from django import forms
from . models import BatchMaster
from . models import PaperMaster
from . models import CourseMaster
from . models import SemMaster
from . models import ExamMaster
from . models import StudentMaster
from . models import StudentInternalTransMaster



class BatchForm(forms.ModelForm):
    class Meta:
        model=BatchMaster
        fields='__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    
class PaperForm(forms.ModelForm):
    class Meta:
        model=PaperMaster
        fields='__all__'
class CourseForm(forms.ModelForm):
    class Meta:
        model=CourseMaster
        fields='__all__'
class SemForm(forms.ModelForm):
    class Meta:
        model=SemMaster
        fields='__all__'
class ExamForm(forms.ModelForm):
    class Meta:
        model=ExamMaster
        fields='__all__'
class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentMaster
        fields='__all__'
class StudentInternalTransForm(forms.ModelForm):
    class Meta:
        model=StudentInternalTransMaster
        fields='__all__'





