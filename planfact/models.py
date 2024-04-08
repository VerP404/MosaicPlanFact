from django.db import models


class MedicalOrganization(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Подразделения: Медицинские организации'


class Corpus(models.Model):
    medical_organization = models.ForeignKey(MedicalOrganization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.medical_organization}"

    class Meta:
        verbose_name_plural = 'Подразделения: Корпуса'


class Department(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.corpus}"

    class Meta:
        verbose_name_plural = 'Подразделения: Отделения'


class Doctor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.department}"

    class Meta:
        verbose_name_plural = 'Подразделения: Врачи'


class IndicatorType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Отчеты: типы'


class IndicatorSubtype(models.Model):
    type = models.ForeignKey(IndicatorType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.type}"

    class Meta:
        verbose_name_plural = 'Отчеты: подтипы'


class MonthlyPlan(models.Model):
    MONTH_CHOICES = [
        (1, 'январь'),
        (2, 'февраль'),
        (3, 'март'),
        (4, 'апрель'),
        (5, 'май'),
        (6, 'июнь'),
        (7, 'июль'),
        (8, 'август'),
        (9, 'сентябрь'),
        (10, 'октябрь'),
        (11, 'ноябрь'),
        (12, 'декабрь'),
    ]

    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES, unique=True, verbose_name='Месяц')
    talon = models.IntegerField(verbose_name='Количество талонов', default=0)
    finance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Финансы', default=0)

    class Meta:
        abstract = True


class OrganizationMonthlyPlan(MonthlyPlan):
    medical_organization = models.ForeignKey(MedicalOrganization, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'план: Медицинская организация'


class CorpusMonthlyPlan(MonthlyPlan):
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'план: Корпус'


class DepartmentMonthlyPlan(MonthlyPlan):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'план: Отделение'


class DoctorMonthlyPlan(MonthlyPlan):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'план: Врач'
