from django.urls import path, include
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product, show_product, register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax, update_product_entry_ajax, product_detail_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('add_product/', add_product, name='add_product'),
    path("product/<uuid:id>/", show_product, name="show_product"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('add-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('api/product/<uuid:pk>/', product_detail_json, name='product_detail_json'),
    path('update-product-ajax/<uuid:pk>/', update_product_entry_ajax, name='update_product_ajax'),
]