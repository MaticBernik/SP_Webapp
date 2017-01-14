from django.contrib import admin

# Register your models here.
from .models import Book,Author,Lease,Reservation,Message,Users_Messages

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Lease)
admin.site.register(Reservation)
admin.site.register(Message)
admin.site.register(Users_Messages)