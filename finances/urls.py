# finances/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Change this line
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    
    # And this line for the delete link
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
]
    # Add other paths for edit, delete, etc.
