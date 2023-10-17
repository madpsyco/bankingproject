from django.contrib import admin

# Register your models here.
from .models import Formdata
from .models import Branch
from .models import District

# Register your models here.
admin.site.register(Formdata)
admin.site.register(District)
admin.site.register(Branch)
