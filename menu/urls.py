from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/restaurant/(?P<pk>[0-9]+)$',
        views.get_delete_update_restaurant,
        name='get_delete_update_restaurant'
    ),
    url(
        r'^api/v1/restaurant/$',
        views.get_post_restaurant,
        name='get_post_restaurant'
    ),
    url(
        r'^api/v1/employee/(?P<pk>[0-9]+)$',
        views.get_delete_update_employee,
        name='get_delete_update_employee'
    ),
    url(
        r'^api/v1/employee/$',
        views.get_post_employee,
        name='get_post_employee'
    ),
    url(
        r'^api/v1/vote/(?P<pk>[0-9]+)$',
        views.get_delete_update_vote,
        name='get_delete_update_vote'
    ),
    url(
        r'^api/v1/vote/$',
        views.get_post_vote,
        name='get_post_vote'
    ),
    url(
        r'^api/v1/get_votes_by_date/$',
        views.get_votes_by_date,
        name='get_votes_by_date'
    ),
    url(
        r'^api/v1/menu/(?P<pk>[0-9]+)$',
        views.get_delete_update_menu,
        name='get_delete_update_menu'
    ),
    url(
        r'^api/v1/menu/$',
        views.get_post_menu,
        name='get_post_menu'
    ),
    url(
        r'^api/v1/get_today_menu/$',
        views.get_today_menu,
        name='get_today_menu'
    ),
    url(
        r'^api/v1/get_menus_by_date/$',
        views.get_menus_by_date,
        name='get_menus_by_date'
    ),
    url(
        r'^ap1/v1/upload/$',
        views.FileView.as_view(),
        name='create_edit_menu'
    ),
    url(
        r'^ap1/v1/upload/(?P<pk>[0-9]+)$',
        views.FileView.as_view(),
        name='create_edit_menu'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
