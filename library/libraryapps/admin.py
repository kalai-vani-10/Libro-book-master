from django.contrib import admin
from .models import Books,LibraryMember,Issuedbooks,Availablebooks,DeletedBooks
admin.site.register(Books)
admin.site.register(LibraryMember)
admin.site.register(Issuedbooks)
admin.site.register(Availablebooks)
admin.site.register(DeletedBooks)
# Register your models here.
