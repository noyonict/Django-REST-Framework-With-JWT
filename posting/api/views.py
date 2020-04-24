from rest_framework import generics, mixins
from django.db.models import Q
from posting.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostApiView(mixins.CreateModelMixin, generics.ListAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id
    # queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):  # DetailView CreateView FormView
    lookup_field = 'pk'  # slug, id
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # def get_queryset(self):
    #     return BlogPost.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)

