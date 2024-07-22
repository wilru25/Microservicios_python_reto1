import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from usuarios.models import Usuario

def handle_uploaded_file(f):
    decoded_file = f.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    for row in reader:
        Usuario.objects.create(
            nombre=row[0],
            apellido_paterno=row[1],
            apellido_materno=row[2],
            edad=row[3],
            nombre_cuenta=row[4],
            contraseña=row[5],
        )

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/url/')
            return render(request, 'sitio_usuarios/success.html')
    else:
        form = UploadFileForm()
    return render(request, 'sitio_usuarios/upload.html', {'form': form})
