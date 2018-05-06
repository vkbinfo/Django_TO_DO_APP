from django import forms


class TodoForm(forms.Form):
    text_input = forms.CharField(max_length=40,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': "Enter your todo Item. ex: Learn something, Watch yourself",
                                            'arial-label': 'Todo',
                                            'aria-describedby': 'add-btn'})
                                 )
