# """Defines URL patterns for learning_logs."""
# from django.urls import path
# from . import views
# urlpatterns = [
#  # Home page
#   path('', views.index, name='index'),

#   # Show all topics.
#   path('topics/', views.topics, name='topics'),
#   path('topics/<int:topic_id>/', views.topic, name='topic'),
#   path('new_topic/', views.new_topic, name='new_topic'),
#   path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
# ]

"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # New topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # New entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    #for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]