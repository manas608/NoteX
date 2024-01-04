from django.urls import path
from .views import SignUpView, UserLoginAPIView, NoteListCreateView, NoteRetrieveUpdateDestroyView, NoteShareView, NoteSearchView

urlpatterns = [
    path('api/auth/signup', SignUpView.as_view(), name='signup'),
    path('api/auth/login', UserLoginAPIView.as_view(), name='login'),
    path('api/notes', NoteListCreateView.as_view(), name='notes'),
    path('api/notes/<int:pk>', NoteRetrieveUpdateDestroyView.as_view(), name='note'),
    path('api/notes/<int:pk>/share', NoteShareView.as_view(), name='share'),
    path('api/search', NoteSearchView.as_view(), name='search'),
]