from django.db import models


class MedicalOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    short_name = models.CharField(max_length=255, verbose_name="Краткое название", default='-')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Организация'


class PlanType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", default='-')
    list_targets = models.TextField(verbose_name="Цели ОМС", default='-')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'План: тип'


class PlanSubtype(models.Model):
    name = models.CharField(max_length=100)
    plan_type = models.ForeignKey(PlanType, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Описание", default='-')
    list_targets = models.TextField(verbose_name="Цели ОМС", default='-')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'План: подтип'


class HospitalBuilding(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(MedicalOrganization, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=255, verbose_name="Краткое название", default='-')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Корпуса'


class Department(models.Model):
    name = models.CharField(max_length=255)
    building = models.ForeignKey(HospitalBuilding, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=255, verbose_name="Краткое название", default='-')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Отделения'


class Doctor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отделение')
    snils = models.CharField(max_length=20, verbose_name='СНИЛС')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic_name = models.CharField(max_length=100, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    start_date = models.DateField( verbose_name='Дата приема')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата увольнения')
    structural_subdivision = models.CharField(max_length=255, verbose_name='Подразделение')
    profile = models.CharField(max_length=255, verbose_name='Профиль')
    specialty = models.CharField(max_length=255, verbose_name='Специальность')
    branch_code = models.CharField(max_length=50, verbose_name='Код отделения')
    certificate_validity_date = models.DateField(null=True, blank=True, verbose_name='Сертификат действителен по:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Врачи'
