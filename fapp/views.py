# apps/files/views.py
from django.conf import settings
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
from .models import File

def download_by_code(request, code):
    try:
        file_obj = File.objects.get(code=code)
    except File.DoesNotExist:
        raise Http404("File not found")

    if settings.DEBUG:
        return FileResponse(
            open(file_obj.file.path, 'rb'),
            as_attachment=True,
            filename=file_obj.filename
        )
    response = HttpResponse()
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{file_obj.filename}"'
    response['X-Accel-Redirect'] = f"/protected/{file_obj.file.name}"

    return response
def main(request):
    data = {}
    return render(request, "main.html", data)