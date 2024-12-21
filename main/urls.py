from . import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()

router.register('users', views.UserViewSet, basename='users')
router.register('books', views.BookViewSet, basename='books')

urlpatterns = router.urls