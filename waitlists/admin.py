from django.contrib import admin
from .models import WaitlistEntry

class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'created_at', 'updated_at')
    # list_filter = ('is_student', 'is_admin',)

    search_fields = ('fname','lname')


admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
