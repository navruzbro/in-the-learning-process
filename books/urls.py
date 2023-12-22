from django.urls import path
#from rest_framework.routers import SimpleRouter
from .views import BookDeleteApiView, BookUpdateApiView
from .views import( 
    BookListApiView, 
    BookCreateApiView,
    BookListCreateApiView,
    BookUpdateDeleteView,
    BookDetailApiView,
    #BookViewset,
)

# router = SimpleRouter()
# router.register('books','BookViewset', basename="books")


urlpatterns = [
    path('', BookListApiView.as_view()),
    path('book/', BookListCreateApiView.as_view()),
    path('book/<int:pk>/', BookDetailApiView.as_view()),
    path('book/<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('book/<int:pk>/edit/', BookUpdateApiView.as_view()),
    path('book/create/', BookCreateApiView.as_view()),
]

#urlpatterns = urlpatterns + router