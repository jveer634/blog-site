from django.urls import path

app_name="blog"

from .views import BlogList, BlogDetail, BlogCreate, BlogUpdate

urlpatterns = [
    path("", BlogList.as_view(), name="list"),
    path("new/", BlogCreate.as_view(), name="create"),
    path("<int:pk>/edit/", BlogUpdate.as_view(), name="update"),
    path("<int:pk>/", BlogDetail.as_view(), name="detail"),
]