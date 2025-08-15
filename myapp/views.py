from django.shortcuts import render
from . forms import AssigmentForm
from django.contrib import messages
from .models import Myform
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = AssigmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Submitted successfully!")
            return render(request, 'home.html', {
                'form': AssigmentForm(),
                'success': True
            })
    else:
        form = AssigmentForm()
    return render(request, 'home.html', {'form': form})



def details(request):
    data = Myform.objects.all()  # fetch all data from the table
    return render(request, 'details.html', {'data': data})

def update_data(request, pk):
    obj = get_object_or_404(Myform, pk=pk)
    if request.method == 'POST':
        form = AssigmentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully!")
            return redirect('details')
    else:
        form = AssigmentForm(instance=obj)
    return render(request, 'update.html', {'form': form, 'obj': obj})


def delete_data(request, pk):
    obj = get_object_or_404(Myform, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Deleted successfully!")
        return redirect('details')
    return render(request, 'delete_confirm.html', {'obj': obj})


def contactus(request):
    return render(request, 'contactus.html')
