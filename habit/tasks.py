from celery import shared_task
from django.utils import timezone
from .models import Habit

@shared_task
def send_habit_reminders():
    from habit.utils import send_telegram_message

    now = timezone.now()
    today = now.date()
    time_now = now.time()

    habits = Habit.objects.filter(
        time__lte=time_now,
        periodicity=1,
    ).select_related("user")

    for habit in habits:
        chat_id = getattr(habit.user, "telegram_chat_id", None)
        if chat_id:
            message = f"Напоминание: {habit.action} в {habit.place} в {habit.time.strftime('%H:%M')}"
            send_telegram_message(chat_id, message)
