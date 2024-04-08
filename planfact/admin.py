from django.contrib import admin
from .models import MedicalOrganization, Department, Corpus, Doctor, IndicatorType, IndicatorSubtype, MonthlyPlan, \
    OrganizationMonthlyPlan, CorpusMonthlyPlan, DepartmentMonthlyPlan, DoctorMonthlyPlan, CorpusPlan, \
    DepartmentPlan, DoctorPlan, OrganizationPlan


class MedicalOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Определяем, какие поля отображать в списке
    search_fields = ('name',)  # Определяем поля для поиска


admin.site.register(MedicalOrganization)
admin.site.register(Corpus)
admin.site.register(Department)
admin.site.register(Doctor)

admin.site.register(IndicatorType)
admin.site.register(IndicatorSubtype)

admin.site.register(OrganizationMonthlyPlan)
admin.site.register(CorpusMonthlyPlan)
admin.site.register(DepartmentMonthlyPlan)
admin.site.register(DoctorMonthlyPlan)

admin.site.register(OrganizationPlan)
admin.site.register(CorpusPlan)
admin.site.register(DepartmentPlan)
admin.site.register(DoctorPlan)





admin.site.site_header = 'Управление медицинскими организациями'  # Заголовок сайта администратора
admin.site.site_title = 'Администрирование Медицинских организаций'  # Название сайта администратора
admin.site.index_title = 'Управление данными'