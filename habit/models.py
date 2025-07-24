from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='habits'
    ) # имя пользователя
    title = models.CharField(max_length=100)  # Название привычки
    description = models.TextField(blank=True)  # Описание (необязательное)
    start_date = models.DateField()  # Дата начала привычки
    end_date = models.DateField(null=True, blank=True)  # Дата окончания (может быть пустой)
    frequency = models.PositiveIntegerField(default=1)  # Частота выполнения (раз в X дней)
    is_good = models.BooleanField(default=True)  # Полезная (True) или вредная (False) привычка
    reward = models.CharField(max_length=255, blank=True)  # Вознаграждение (может быть пустой)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания записи
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления

    def clean(self):
        # Только одно из двух: reward или related_habit
        if self.reward and self.related_habit:
            raise ValidationError(_('Нельзя указывать и награду, и связанную привычку одновременно.'))

        # Приятная привычка не может иметь награду или связанную привычку
        if self.is_pleasant:
            if self.reward or self.related_habit:
                raise ValidationError(_('Приятная привычка не может иметь награду или связанную привычку.'))

        # Время выполнения <= 120 сек
        if self.execution_time > 120:
            raise ValidationError(_('Время выполнения не должно превышать 120 секунд.'))

        # Только приятные привычки могут быть связаны
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError(_('Связанной может быть только приятная привычка.'))

        # Периодичность должна быть от 1 до 7
        if self.periodicity < 1 or self.periodicity > 7:
            raise ValidationError(_('Периодичность должна быть от 1 до 7 дней.'))

    def __str__(self):
        return f"{self.action} в {self.time.strftime('%H:%M')} ({self.user.username})"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ['-created_at']

