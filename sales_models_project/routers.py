"""
Terms of Service App, Marcin Roszczyk 2020

"""

__author__ = "Marcin Roszczyk,"
__copyright__ = "Copyright 2020, Marcin Roszczyk"
__license__ = "GPL"
__version__ = "0.0.1-pre-beta"
__maintainer__ = "Marcin Roszczyk"
__email__ = "mr@marcinros.net"
__status__ = "DEV"


from rest_framework import routers
from rsm import views as api_views

router = routers.DefaultRouter()
router.register(r'user_profile', api_views.UserProfileViewSet, basename='user_profile')
router.register(r'sales_model', api_views.SalesModelViewSet , basename='sales_model')
router.register(r'parameters_group', api_views.ParametersGroupViewSet , basename='parameters_group')
router.register(r'parameter', api_views.ParameterViewSet , basename='parameter')
