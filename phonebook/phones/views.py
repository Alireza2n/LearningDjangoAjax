from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from . import forms


@csrf_exempt
@require_POST
def create_entry(request):
    """
    Creates an entry via AJAX
    """
    form_instance = forms.EntryForm(data=request.POST)
    if form_instance.is_valid():
        entry_object = form_instance.save()
        return JsonResponse(data={
            'success': True,
            'pk': entry_object.pk,
            'name': entry_object.name,
            'last_name': entry_object.last_name,
            'phone_number': entry_object.phone_number
        }, status=201)
    else:
        return JsonResponse(data={
            'success': False,
        }, status=400)


@csrf_exempt
@require_GET
def show_add_entry_form(request):
    """
    Show the add entry form page
    """
    return render(request, 'phones/add_entry.html', {
        'form': forms.EntryForm()
    })
