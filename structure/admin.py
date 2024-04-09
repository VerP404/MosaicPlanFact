from django.contrib import admin
from .models import MedicalOrganization, PlanType, PlanSubtype, HospitalBuilding, Department, Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic_name', 'department', 'department_building', 'department_organization')

    def department_building(self, obj):
        return obj.department.building.name

    def department_organization(self, obj):
        return obj.department.building.organization.name


class PlanSubtypeInline(admin.TabularInline):
    model = PlanSubtype


class PlanTypeAdmin(admin.ModelAdmin):
    inlines = [PlanSubtypeInline]
    list_display = ('name', 'description', 'list_targets')


class MedicalOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)


class HospitalBuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'building')


# Регистрация административных классов
admin.site.register(MedicalOrganization, MedicalOrganizationAdmin)
admin.site.register(PlanType, PlanTypeAdmin)
admin.site.register(HospitalBuilding, HospitalBuildingAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)

admin.site.site_header = 'Управление медицинскими организациями'  # Заголовок сайта администратора
admin.site.site_title = 'Администрирование Медицинских организаций'  # Название сайта администратора
admin.site.index_title = 'Управление данными'