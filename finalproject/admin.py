from django.contrib import admin

from .models import Account,Accounts,images,Image

admin.site.register(Account)
admin.site.register(Accounts)


admin.site.register(images)
admin.site.register(Image)