from django.contrib import admin
from .models import Data

@admin.register(Data)
class DataDisplay(admin.ModelAdmin):
    list_display=('Candidate','Post','Status','URL','Designated')
    list_filter=('Status','Post')
    search_fields=('Account','Post')
    prepopulated_fields={'URL':('Post',)}
    #readonly_fields=('Candidate',)
    autocomplete_fields=('Candidate',)
    #raw_id_fields=('Candidate',)
    date_hierarchy='Designated'
    ordering=('Status','Designated',)
