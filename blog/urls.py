from django.urls import path
from blog.views import home, blogs, resume
from django.conf import settings
from django.conf.urls.static import static
from demo.views import books_page


urlpatterns = [
    path('', home, name='home_page'),
    path('blogs/', blogs, name='blogs_page'),
    path('resume/', resume, name='resume_page'),
    path('books/', books_page, name='books_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
