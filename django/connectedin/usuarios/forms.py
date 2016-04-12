from django import forms
from django.contrib.auth.models import User

class RegistrarusuarioForm(forms.Form):

    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarusuarioForm, self).is_valid():
            self.adiciona_erro('Por favor verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome'].exists())

        if user_exists:
            self.adiciona_erro('Usuário já existe')
            valid = False
            
        return valid

    def adiciona_erro(self, message):
        erros = self._erros.setdefault(forms.forms.NON_FIELD_ERRORS, forms.util.ErrorDict)
        error.append(message)