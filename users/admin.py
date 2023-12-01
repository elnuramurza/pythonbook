from django.contrib import admin
# from .models import Mentor
# from .models.mentors import Mentor
from users.models.mentors import Mentor


# Register your models here.

admin.site.register(Mentor)