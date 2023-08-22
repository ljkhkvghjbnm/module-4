from django.urls import path
from .views import index, top_sellers, advertisement_post
# from .views import lesson

urlpatterns = [
    path("",index, name="main-page"),
    path('top-sellers/',top_sellers,name="top-sellers"),
    # path('lesson_4/',lesson)
    path('advertisement-post/',advertisement_post, name='adv-post')
]
