from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actor"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinemahalls/", CinemaHallList.as_view(
        actions={"get": "list",
                 "post": "create"}), name="cinemahall"),
    path("cinemahalls/<int:pk>/", CinemaHallDetail.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }), name="cinemalall_detail"),
    path("", include(router.urls), name="movie"),
]

app_name = "cinema"
