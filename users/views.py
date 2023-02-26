import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from HW_27.settings import TOTAL_ON_PAGE
from users.models import User, Location
from users.serializers import UserSerializer, UserListSerializer, UserDetailSerialize, LocationSerializer


class UserPagination(PageNumberPagination):
    page_size = 4

class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination
    # model = User
    #
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     self.object_list = self.object_list.order_by("username")
    #
    #     paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
    #     page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #
    #     users = []
    #     for user in page_obj:
    #         users.append({
    #             "id": user.id,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "username": user.username,
    #             "password": user.password,
    #             "role": user.role,
    #             "age": user.age,
    #             "location": str(user.location),
    #         })
    #
    #     response = {
    #         "items": users,
    #         "num_pages": paginator.num_pages,
    #         "total": paginator.count
    #     }
    #
    #     return JsonResponse(response, safe=False)


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerialize
    queryset = User.objects.all()
    # model = User
    #
    # def get(self, request, *args, **kwargs):
    #     user = self.get_object()
    #
    #     return JsonResponse({
    #         "id": user.id,
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "username": user.username,
    #         "password": user.password,
    #         "role": user.role,
    #         "age": user.age,
    #         "location": str(user.location),
    #     })


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # model = User
    # fields = ["first_name", "last_name", "username", "password", "role", "age", "location"]
    #
    # def post(self, request, *args, **kwargs):
    #     user_data = json.loads(request.body)
    #
    #     user = User.objects.create(
    #         first_name=user_data["first_name"],
    #         last_name=user_data["last_name"],
    #         username=user_data["username"],
    #         password=user_data["password"],
    #         role=user_data["role"],
    #         age=user_data["age"],
    #     )
    #
    #     if user_data["location"]:
    #         loc_obj, created = Location.objects.get_or_create(
    #             name=user_data["location"],
    #             defaults={
    #                 "is_active": True
    #             }
    #         )
    #         user.location.add(loc_obj)
    #
    #     user.save()
    #
    #     return JsonResponse({
    #         "id": user.id,
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "username": user.username,
    #         "password": user.password,
    #         "role": user.role,
    #         "age": user.age,
    #         "location": str(user.location),
    #     })


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # model = User
    # fields = ["first_name", "last_name", "username", "password", "age", "location"]
    #
    # def patch(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #
    #     user_data = json.loads(request.body)
    #
    #     self.object.first_name = user_data["first_name"]
    #     self.object.last_name = user_data["last_name"]
    #     self.object.username = user_data["username"]
    #     self.object.password = user_data["password"]
    #     self.object.age = user_data["age"]
    #
    #     if user_data["location"]:
    #         loc_obj, created = Location.objects.get_or_create(
    #             name=user_data["location"],
    #             defaults={
    #                 "is_active": True
    #             }
    #         )
    #         self.object.location.add(loc_obj)
    #
    #     self.object.save()
    #
    #     return JsonResponse({
    #         "id": self.object.id,
    #         "first_name": self.object.first_name,
    #         "last_name": self.object.last_name,
    #         "username": self.object.username,
    #         "password": self.object.password,
    #         "role": self.object.role,
    #         "age": self.object.age,
    #         "location_id": str(self.object.location),
    #     })


class UserDeleteView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # model = User
    # success_url = "/"
    #
    # def delete(self, request, *args, **kwargs):
    #     super().delete(request, *args, **kwargs)
    #
    #     return JsonResponse({"status": "ok"}, status=200)


class LocationViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

# @method_decorator(csrf_exempt, name='dispatch')
# class LocationListView(ListView):
#     model = Location
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         self.object_list = self.object_list.order_by("name")
#
#         paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#
#         locations = []
#         for location in page_obj:
#             locations.append({
#                 "id": location.id,
#                 "name": location.name,
#                 "lat": location.lat,
#                 "lng": location.lng
#             })
#
#         response = {
#             "items": locations,
#             "num_pages": paginator.num_pages,
#             "total": paginator.count
#         }
#
#         return JsonResponse(response, safe=False)
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class LocationCreateView(CreateView):
#     model = Location
#     fields = ["name", "lat", "lng"]
#
#     def post(self, request, *args, **kwargs):
#         location_data = json.loads(request.body)
#
#         location = Location.objects.create(
#             name=location_data["name"],
#             lat=location_data["lat"],
#             lng=location_data["lng"],
#         )
#
#         return JsonResponse({
#             "id": location.id,
#             "name": location.name,
#             "lat": location.lat,
#             "lng": location.lng
#         })
#
#
# class LocationDetailView(DetailView):
#     model = Location
#
#     def get(self, request, *args, **kwargs):
#         location = self.get_object()
#
#         return JsonResponse({
#             "id": location.id,
#             "name": location.name,
#             "lat": location.lat,
#             "lng": location.lng
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class LocationDeleteView(DeleteView):
#     model = Location
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({"status": "ok"}, status=200)
