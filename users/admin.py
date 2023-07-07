from django.contrib import admin
from .models import *
# Register your models here.


class contactusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','subject','message')
admin.site.register(contactus,contactusAdmin)


class productItemAdmin(admin.ModelAdmin):
    list_display=('id','title','image','price','productInclude')
admin.site.register(productItem,productItemAdmin)


class loveFromClientAdmin(admin.ModelAdmin):
    list_display=('id','clientName','clientProfession','clientMessage','clientImage')
admin.site.register(loveFromClient,loveFromClientAdmin)


class requestQuoteAdmin(admin.ModelAdmin):
    list_display=('id','Name','Email','SelectedService','Message')
admin.site.register(requestQuote,requestQuoteAdmin)



class blogSiteBackendAdmin(admin.ModelAdmin):
    list_display=('id','blogRelatedTitle','blogImage','writterName','publishDate','blogTitle','blogDetail')
admin.site.register(blogSiteBackend,blogSiteBackendAdmin)

# newsletter

class newsletterAdmin(admin.ModelAdmin):
    list_display=('id','name','email','specialNotes')
admin.site.register(newsletter,newsletterAdmin)


class jointeamAdmin(admin.ModelAdmin):
    list_display=('full_name','gender','phone_number','qualification')
admin.site.register(JoinTeam,jointeamAdmin)