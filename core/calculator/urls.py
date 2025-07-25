# from django.urls import path, include
# from calculator.views  import calculator_view
# urlpatterns = [
#     path("", calculator_view, name='calculator'),
# ]


from django.urls import path
from .views import calculator_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", calculator_view, name="calculator"),
]

