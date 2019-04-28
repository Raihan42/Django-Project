from django.contrib import admin

from . models import QuoteCatagory
from .models import Quote
admin.site.register(QuoteCatagory)
admin.site.register(Quote)
