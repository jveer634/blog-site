from django.urls import path

app_name="blog"

from .views import BlogList, BlogDetail

urlpatterns = [
    path("", BlogList.as_view(), name="list"),
    path("<int:pk>/", BlogDetail.as_view(), name="detail")
]