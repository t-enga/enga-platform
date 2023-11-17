"""
URL configuration for platfinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from services import views
from supplies.views import supplies, supplie_data, supplie_create, status_supplie, status_table, supplie_excel, create_assignment, assignment_table, supplie_traffic, supplies_finished, supplie_billing, supplie_delete, supplie_editinit, supplies_drivers, guardar_folio, search_folio, status_excel
from androidapp.views import authenticate_user
from boardmci.views import board_mci,get_mdps

urlpatterns = [
    #URL´s SERVICES
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('principal/', views.principal, name='principal'),
    path('map/', views.map, name='map'),
    path('trips/', views.trips, name='trips'),
    path('trips/drivers/', views.trips_drivers, name='trips_drivers'),
    path('drivers/trip/<int:id_service>/', views.drivers_trip, name='drivers_trip'),
    path('drivers/trip/cargo/<int:id_service>/', views.drivers_cargo, name='drivers_cargo'),
    path('expenses/table/', views.expenses_table, name='expenses_table'),
    path('filter_expenses/', views.filter_expenses, name='filter_expenses'),
    path('logout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('trip/create/', views.trip_create, name='trip_create'),
    path('trip/travel/', views.trip_travel, name='trip_travel'),
    path('trip/edit/<int:id_service>/', views.trip_edit, name='trip_edit'),
    path('trip/billing/<int:id_service>/', views.trip_billing, name='trip_billing'),
    path('trip/trafic/<int:id_service>/', views.trip_trafic, name='trip_trafic'),
    path('trip/expences/<int:id_service>/', views.trip_expences, name='trip_expences'),
    path('trip/<int:id_service>/', views.trip_detail, name='trip_detail'),
    path('trip/<int:id_service>/delete', views.trip_delete, name='trip_delete'),
    path('trip/finished/', views.trip_finished, name='trip_finished'),
    path('trip/status/', views.trip_status, name='trip_status'),
    path('export/excel/', views.export_to_excel, name='export_excel'),
    path('get_coordinates/', views.get_coordinates, name='get_coordinates'),
    path('table/ganade/', views.table_ganade, name='table_ganade'),
    path('boardcig/',views.board_cig, name='board_cig'),
    path('get/infogps/',views.get_info_gps, name='get_info_gps'),
    path('routes/trip/assign/<int:id_service>/', views.routes_assign, name='routes_assign'),

    #ROUTES
    path('create/route/',views.create_route, name='create_route'),
    path('create/route/save/route/',views.save_route, name='save_route'),
    path('routes/assign/<int:id_route>/', views.routes_assign, name='routes_assign_detail'),
    path('get/route/points/<int:id_route>/',views.get_route_points, name='get_route_points'),
    
    #URL´s SUPPLIES
    path('supplies/', supplies, name='supplies'),
    path('supplie/<int:id_serv>/', supplie_data, name='supplie_data'),
    path('supplie/traffic/<int:id_serv>/', supplie_traffic, name='supplie_traffic'),
    path('supplie/create/', supplie_create, name='supplie_create'),
    path('status/table/', status_table, name='status_table'),
    path('supplie/excel/', supplie_excel, name='supplie_excel'),
    path('status/excel/', status_excel, name='status_excel'),
    path('supplie/assignment/', create_assignment, name='create_assignment'),
    path('supplie/table/', assignment_table, name='assignment_table'),   
    path('supplies/finished/', supplies_finished, name='supplies_finished'),   
    path('supplie/billing/<int:id_serv>/', supplie_billing, name='supplie_billing'),   
    path('supplie/delete/<int:id_serv>/', supplie_delete, name='supplie_delete'),   
    path('supplie/edit/<int:id_serv>/', supplie_editinit, name='supplie_editinit'),   
    path('supplies/drivers/', supplies_drivers, name='supplies_drivers'),   
    path('status/supplie/<int:id_serv>/', status_supplie, name='status_supplie'),
    path('guardar_folio/<int:id_serv>/', guardar_folio, name='guardar_folio'),
    path('search/folio/', search_folio, name='search_folio'),
    
    #URL´s APP Android
    path('api/authenticate/', authenticate_user, name='authenticate_user'),

    #URL´s MSI Board
    path('boardmci/',board_mci, name='board_mci'),
    path('get/mdps/',get_mdps, name='get_mdps'),
    
]
    
