import logging
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

logger = logging.getLogger(__name__)

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("books_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        group, _ = Group.objects.get_or_create(name="Customers")
        self.object.groups.add(group)
        login(self.request, self.object)
        logger.info("Зарегистрирован пользователь %s", self.object.username)
        return response