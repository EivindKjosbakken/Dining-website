from django.urls import path
from .views import dinner_detail_view, dinner_create_view, feed_view, dinner_edit_view, dinner_delete_view


app_name = 'dinners'
urlpatterns = [
    path('', feed_view, name='dinner-list'),
    path('create/', dinner_create_view, name='dinner-create'),
    path('<int:my_id>/', dinner_detail_view, name='dinner-detail'),
    path('edit/<int:my_id>/', dinner_edit_view, name='dinner-edit'),
    path('delete/<int:my_id>/', dinner_delete_view, name='dinner-delete'),
]
