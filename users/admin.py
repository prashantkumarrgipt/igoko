from django.contrib import admin
from .models import *
# Register your models here.


class contactusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','subject','message')
admin.site.register(contactus,contactusAdmin)


class productAdmin(admin.ModelAdmin):
    list_display=('id','title','image')
admin.site.register(product,productAdmin)


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