from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ArchiveForm
from .models import Archive, Subject
from .serializers import SubjectSerializer,ArchiveSerializer,ArchiveDetailSerializer


class SubjectView(APIView):
    def get(self, request, format=None):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)

        return Response(serializer.data)


class NewestArchiveView(APIView):
    def get(self, request, format=None):
        archive = Archive.objects.all()[0:4]
        serializer = ArchiveSerializer(archive, many=True)

        return Response(serializer.data)


class MyArchiveView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        archive= Archive.objects.filter(created_by=request.user)
        serializer = ArchiveSerializer(archive, many=True)

        return Response(serializer.data)


class CreateArchiveView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = ArchiveForm(request.data)

        if form.is_valid():
            archive = form.save(commit=False)
            archive.created_by = request.user
            archive.save()

            return Response({'status': 'created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})
    
    def put(self, request, pk):
        archive = Archive.objects.get(pk=pk, created_by=request.user)
        form = ArchiveForm(request.data, instance=archive)
        form.save()

        return Response({'status': 'updated'})
    
    def delete(self, request, pk):
        archive = Archive.objects.get(pk=pk, created_by=request.user)
        archive.delete()

        return Response({'status': 'deleted'})
    

class BrowseArchiveView(APIView):
    def get(self, request, format=None):
        archive= Archive.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')

        if query:
            archive = archive.filter(title__icontains=query)

        if categories:
            archive = archive.filter(category_id__in=categories.split(','))

        serializer = ArchiveSerializer(archive, many=True)

        return Response(serializer.data)


class ArchiveDetailView(APIView):
    def get(self, request, pk, format=None):
        archive = Archive.objects.get(pk=pk)
        serializer = ArchiveDetailSerializer(archive)

        return Response(serializer.data)