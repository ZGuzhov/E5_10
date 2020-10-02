from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Марка")
    model = models.CharField(max_length=50, verbose_name="Модель")
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")
    GEAR_CHOICES = [(1, 'Механика'), (2, 'Автомат'), (3, 'Робот')]
    gearbox = models.PositiveSmallIntegerField(choices=GEAR_CHOICES, default='1', verbose_name="Коробка передач")
    color = models.CharField(max_length=30, verbose_name="Цвет")

    def __str__(self):
        return "{} {} (коробка: {}, год выпуска: {}, цвет: {})".format(self.brand, self.model, self.get_gearbox_display(), self.year, self.color)