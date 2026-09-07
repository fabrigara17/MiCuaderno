"""
Referencia: https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
El parámetro authentication_form de LoginView acepta cualquier subclase de
AuthenticationForm, es el mecanismo oficial para personalizar el form de login.
"""
from django.contrib.auth.forms import AuthenticationForm

INPUT_CLASSES = (
    'w-full rounded-md border border-slate-300 px-3 py-2 text-slate-900 '
    'focus:outline-none focus:ring-2 focus:ring-indigo-500'
)


class LibretaLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': INPUT_CLASSES})
        self.fields['password'].widget.attrs.update({'class': INPUT_CLASSES})
