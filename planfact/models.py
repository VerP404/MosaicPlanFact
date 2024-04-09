from django.db import models


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


class MonthlyPlan(models.Model):
    year = models.PositiveIntegerField(verbose_name='Год')
    entity = models.ForeignKey(YourEntityModel, on_delete=models.CASCADE, verbose_name='Сущность')
    indicator_type = models.ForeignKey(IndicatorType, on_delete=models.CASCADE, verbose_name='Тип')
    indicator_subtype = models.ForeignKey(IndicatorSubtype, on_delete=models.CASCADE, verbose_name='Подтип')
    january = models.PositiveIntegerField(verbose_name='Январь', default=0)
    february = models.PositiveIntegerField(verbose_name='Февраль', default=0)
    march = models.PositiveIntegerField(verbose_name='Март', default=0)
    april = models.PositiveIntegerField(verbose_name='Апрель', default=0)
    may = models.PositiveIntegerField(verbose_name='Май', default=0)
    june = models.PositiveIntegerField(verbose_name='Июнь', default=0)
    july = models.PositiveIntegerField(verbose_name='Июль', default=0)
    august = models.PositiveIntegerField(verbose_name='Август', default=0)
    september = models.PositiveIntegerField(verbose_name='Сентябрь', default=0)
    october = models.PositiveIntegerField(verbose_name='Октябрь', default=0)
    november = models.PositiveIntegerField(verbose_name='Ноябрь', default=0)
    december = models.PositiveIntegerField(verbose_name='Декабрь', default=0)

    def __str__(self):
        return f"{self.year} {self.entity} {self.indicator_type} {self.indicator_subtype}"

    class Meta:
        verbose_name_plural = 'Планы по месяцам'
        unique_together = ('year', 'entity', 'indicator_type', 'indicator_subtype')

