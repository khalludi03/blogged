from django.forms import ModelForm
from .models import Comment 

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'w-full py-4 px-6 bg-gray-100',})
        self.fields['content'].widget.attrs.update({'class': 'w-full py-4 px-6 bg-gray-100',})
    class Meta:
        model = Comment
        fields = ('name', 'content',)
