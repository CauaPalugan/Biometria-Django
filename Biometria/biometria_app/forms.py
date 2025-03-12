from django import forms
from .models import Funcionario  

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'senha', 'cargo', 'chave']  
        widgets = {
            'senha': forms.PasswordInput(),
            'chave': forms.TextInput(attrs={'readonly': 'readonly'}),  
        }
