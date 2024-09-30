from django import forms  # Importa o módulo de formulários do Django
from django.contrib.auth import forms  # Importa os formulários de autenticação do Django
from .models import Users  # Importa o modelo de usuário personalizado que você criou

# Aqui estamos criando um formulário que sobrescreve o "UserChangeForm" padrão do Django.
# O "UserChangeForm" é usado quando queremos permitir que o administrador ou o próprio usuário
# edite informações do perfil.
class UserChangeForm(forms.UserChangeForm):  
    class Meta(forms.UserChangeForm.Meta):
        model = Users  # Definimos que o modelo usado é o nosso modelo "Users"

# Este é um formulário para a criação de novos usuários.
# Estamos sobrescrevendo o "UserCreationForm" padrão do Django, que é utilizado para criar um novo usuário.
# Vamos usar o nosso modelo "Users" personalizado no lugar do modelo de usuário padrão do Django.
class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users  # Aqui indicamos que o modelo é "Users", o nosso modelo de usuário customizado.
