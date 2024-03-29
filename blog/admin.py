from django.contrib import admin
from .models import Post, Comment, Caption

class TinyMCEAdmin(admin.ModelAdmin):
	class Media: 
		js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)

admin.site.register(Post, TinyMCEAdmin)
admin.site.register(Comment)
admin.site.register(Caption)