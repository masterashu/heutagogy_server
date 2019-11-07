import mimetypes
import os
from wsgiref.util import FileWrapper
from django.conf import settings
from django.http import HttpResponse
from django.utils.encoding import smart_str
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lesson
from .serializers import LessonSerializer


class LessonsGetView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True, context={'request': request})
        return Response(serializer.data)


def download_file(request, file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(open(file_path, 'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    return response
