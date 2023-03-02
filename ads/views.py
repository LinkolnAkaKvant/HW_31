import json

from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from HW_27.settings import TOTAL_ON_PAGE
from ads.models import Category, Ad, Selection
from ads.permissions import IsOwner, IsStaff
from ads.serializers import AdSerializer, AdDetailSerializer, AdListSerializer, SelectionSerializer, \
    SelectionCreateSerializer
from users.models import User


def main_page(request):
    return JsonResponse({"status": "ok"})


class AdViewSet(ModelViewSet):
    default_serializer = AdSerializer
    queryset = Ad.objects.order_by("-price")
    serializer = {"retrieve": AdDetailSerializer,
                  "list": AdListSerializer
                  }

    default_permission = [AllowAny]
    permissions = {
        "retrieve": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwner | IsStaff],
        "partial_update": [IsAuthenticated, IsOwner | IsStaff],
        "destroy": [IsAuthenticated, IsOwner | IsStaff]
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializer.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist("cat")
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get("price_from")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get("price_to")
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ['name', 'image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "image": self.object.image.url if self.object.image else None
        })


#
class AuthorAdDetailView(View):
    def get(self, request):
        author_qs = User.objects.annotate(ads=Count('ad'))

        paginator = Paginator(author_qs, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        authors = []
        for author in page_obj:
            authors.append({
                "id": author.id,
                "username": author.username,
                "ads": author.ads
            })

        response = {
            "items": authors,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
            "avg": author_qs.aggregate(avg=Avg('ads'))['avg']
        }

        return JsonResponse(response)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        categories = []
        for cat in page_obj:
            categories.append({
                "id": cat.id,
                "name": cat.name,
            })

        response = {
            "items": categories,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"],
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated],
        "update": [IsAuthenticated, IsOwner],
        "partial_update": [IsAuthenticated, IsOwner],
        "destroy": [IsAuthenticated, IsOwner]
    }

    default_serializer = SelectionSerializer
    serializers = {
        "create": SelectionCreateSerializer,
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
