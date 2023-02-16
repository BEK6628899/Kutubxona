from django.contrib import admin
from .models import *

# admin.site.register(talaba)
@admin.register(talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ("id","ism","bitiruvchi","kitoblar_soni","kursi")
    list_display_links = ("id","ism")
    list_editable = ("bitiruvchi","kitoblar_soni","kursi")
    list_filter = ("bitiruvchi",)
    list_per_page = 6
    search_fields = ("id","ism")
    search_help_text = "Id va Ism bo`yicha qidiruv bering"






# admin.site.register(muallif)
@admin.register(muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ("id","ism","trik","kitob_soni","jinsi","tugilgan_sanasi","yosh")
    list_display_links = ("id","ism")
    list_editable = ("kitob_soni","trik")
    search_fields = ("ism",)
    search_help_text = "Ism bo`yicha qidiruv bering "
    list_filter = ("trik",)






# admin.site.register(kitob)
@admin.register(kitob)
class KitobAdmin(admin.ModelAdmin):
    autocomplete_fields = ("muallif",)
    search_fields = ("nom",)






# admin.site.register(Admin)
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ("ism","ish_vaqti")
    list_filter = ("ish_vaqti",)
    search_fields = ("ism",)
    search_help_text = "Ism bo`yicha qidiruv bering "





# admin.site.register(record)
@admin.register(record)
class RecordAdmin(admin.ModelAdmin):
    autocomplete_fields = ("talaba","kitob","Admin")




