from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer



class ImageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer


    def get_queryset(self):
        """
        This view should return a list of all the images
        for the currently authenticated user.
        """
        user = self.request.user
        return Image.objects.filter(owner=user.id)

    def perform_create(self, serializer):
        """
        Saves an image and assigns current user as owner.
        """
        serializer.save(owner=self.request.user)


