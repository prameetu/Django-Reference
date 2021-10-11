from django.shortcuts import render
from students.forms import userForm
# Create your views here.

def index(request):
    return render(request,'students/index.html')

def records_view(request):
    form = userForm

    if request.method == 'POST':
        form = userForm(request.POST)


        if form.is_valid():
            # print("SUBMIT SUCCES")
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['roll'])
            # print(form.cleaned_data['dob'])
            # print(form.cleaned_data['email'])
            form.save(commit=True)
            return index(request)
        else:
            print("Error in Form Validation")

    return render(request,'students/forms.html',{'form':form})







