from django.urls import path
from .views import views


urlpatterns = [
    path('order-management/', views.order_management, name='order_management'),
    path('inventory-tracking/', views.inventory_tracking, name='inventory_tracking'),
    path('update-inventory/<int:item_id>/', views.update_inventory, name='update_inventory'),
    path('delete-item/<int:item_id>/', views.delete_inventory, name='delete_item'),
    path('warehouse-management/', views.add_warehouse_movement, name='warehouse_management'),  # URL for warehouse management
    path('update-warehouse/<int:movement_id>/', views.update_warehouse_movement, name='update_warehouse_movement'),  # URL for updating a warehouse movement
    path('delete-warehouse/<int:movement_id>/', views.delete_warehouse_movement, name='delete_warehouse_movement'),
    path('show_barcode_page/<int:item_id>/', views.show_barcode_page, name='show_barcode_page'),

]