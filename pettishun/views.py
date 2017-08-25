from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

class HomeView(TemplateView):
    template_name = 'pettishun/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sigs'] = User.objects.filter(emailaddress__verified=True)
        return context
