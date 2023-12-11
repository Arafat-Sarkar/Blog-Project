
from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_categorie(request):
    if request.method=='POST':
        category_form = forms.categoryForm(request.POST)
        if category_form.is_valid():
         category_form.save()
         return redirect('add_post')
    
    else:
      category_form = forms.categoryForm()
       
      return render(request, 'add_category.html' , {'form':category_form})
