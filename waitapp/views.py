from django.shortcuts import render, redirect, HttpResponse
from .forms import TruckDriverForm
from .models import TruckDriver
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime


# Create your views here.
def driver_form(request):
    if request.method == 'POST':
        form = TruckDriverForm(request.POST)
        if form.is_valid():
            # Do something with the form data, e.g., save it to the database
            form.save()

            return render(request, 'success.html')
    else:
        form = TruckDriverForm()
        print('Form not submitted', form.errors)

    return render(request, 'driver_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def queue_list(request):
    drivers=TruckDriver.objects.all()
    return render(request, 'queue_list.html', {'drivers':drivers})


@login_required
def menu(request):
    return render(request, 'menu.html')

def manage_queue(request):
    submissions = TruckDriver.objects.exclude(status='Finished').order_by('check_in')

    return render(request, 'manage_queue.html', {'submissions': submissions})

def update_status(request):
    if request.method == 'POST':
        submission_id = request.POST.get('submission_id')
        new_status = request.POST.get('new_status')

        try:
            submission = TruckDriver.objects.get(id=submission_id)
            if new_status == 'In Progress':
                submission.status = 'In Progress'
                submission.in_progress_time = datetime.now()
            elif new_status == 'Finished':
                submission.status = 'Finished'
                submission.finished_time = datetime.now()
                
            submission.save()
            return JsonResponse({'success': True})
        except TruckDriver.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Submission not found'})
        
    return JsonResponse({'success': False, 'error': 'Invalid request'})