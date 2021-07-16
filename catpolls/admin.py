from django.contrib import admin
from .models import Catuestion, Cachoice


class CachoiceInline(admin.TabularInline):
    model = Cachoice
    extra = 3


class CatuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Date information', {'fields': ['publication_date'],
                                  'classes': ['collapse']}),
            (None, {'fields': ['catuestion_text']})]
    inlines = [CachoiceInline]
    list_display = ('catuestion_text',
                    'publication_date',
                    'catuestion_image',
                    'was_published_recently')
    list_filter = ['publication_date']
    search_fileds = ['catuestion_text']


admin.site.register(Catuestion, CatuestionAdmin)
