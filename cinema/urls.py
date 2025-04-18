from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)

list_create_actions = {
    "get": "list",
    "post": "create"
}

urlpatterns = [
    path("", include(router.urls)),
    path(
        "genres/",
        GenreViewSet.as_view(actions=list_create_actions),
        name="genre-list"
    ),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(actions=list_create_actions),
        name="cinemahall-list"
    ),
    path(
        "actors/",
        ActorViewSet.as_view(actions=list_create_actions),
        name="actor-list"
    ),
    path(
        "movies/",
        MovieViewSet.as_view(actions=list_create_actions),
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        MovieViewSet.as_view(actions={"get": "retrieve"}),
        name="movie-detail"
    ),
    path(
        "orders/",
        OrderViewSet.as_view(actions=list_create_actions),
        name="order-list"
    )

]

app_name = "cinema"
