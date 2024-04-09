from django.contrib import admin
from .models import IndicatorType, IndicatorSubtype


class MedicalOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Определяем, какие поля отображать в списке
    search_fields = ('name',)  # Определяем поля для поиска


admin.site.register(IndicatorType)
admin.site.register(IndicatorSubtype)

admin.site.site_header = 'Управление медицинскими организациями'  # Заголовок сайта администратора
admin.site.site_title = 'Администрирование Медицинских организаций'  # Название сайта администратора
admin.site.index_title = 'Управление данными'
