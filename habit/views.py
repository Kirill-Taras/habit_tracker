from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer

class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
