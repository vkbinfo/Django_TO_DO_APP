from django import forms
from .models import Todo

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': "Enter your todo Item. ex: Learn something, Watch yourself",
                                            'arial-label': 'Todo',
                                            'aria-describedby': 'add-btn'})
                                 )

# the awesome model(table) based form
class NewToDoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': "Enter your todo Item. ex: Learn something, Watch yourself",
                                            'arial-label': 'Todo',
                                            'aria-describedby': 'add-btn'})
        }
