from django.contrib import admin
from social.models import *



class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info', 'city', 'phone', 'website')

	def user_info(self, obj):
		return obj.description

	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('-phone', 'user')
		return queryset

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
	



