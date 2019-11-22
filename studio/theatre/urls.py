from rest_framework.routers import SimpleRouter
from .views import MoviesViewSet, UserViewSet

simpleRouter = SimpleRouter()

simpleRouter.register('movie',MoviesViewSet)
simpleRouter.register('user',UserViewSet)

urlpatterns = simpleRouter.urls