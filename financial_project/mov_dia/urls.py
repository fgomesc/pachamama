from django.urls import path
from .views import MovDiaList, MovDiaEdit, MovDiaDelete, MovDiaCreate

urlpatterns = [
    path('', MovDiaList.as_view(), name='list_mov_dia'),
    path('editar/<int:pk>/', MovDiaEdit.as_view(), name='edit_mov_dia'),
    path('delete/<int:pk>/', MovDiaDelete.as_view(), name='delete_mov_dia'),
    path('novo/', MovDiaCreate.as_view(), name='create_mov_dia'),
]