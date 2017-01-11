from django.contrib import admin

# Register your models here.
from .models import Book,Author,Lease,Reservation

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Lease)
admin.site.register(Reservation)