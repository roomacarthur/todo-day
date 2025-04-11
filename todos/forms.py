from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        label="New Category",
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-gray-700 text-gray-200 border border-gray-600 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Add a new category (optional)'
        })
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_completed', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({
            'class': 'w-full bg-gray-700 text-gray-200 border border-gray-600 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
        })

    def save(self, commit=True):
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            self.instance.category = category
        return super().save(commit)