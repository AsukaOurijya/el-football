from django.urls import path, include
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product, show_product, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('add_product/', add_product, name='add_product'),
    path("product/<uuid:id>/", show_product, name="show_product"),
    path('register', register, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
]