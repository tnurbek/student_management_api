from django.contrib import admin
from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    # list_filter = ('is_student', 'is_admin',)

    search_fields = ('name',)

admin.site.register(Certificate, CertificateAdmin)
