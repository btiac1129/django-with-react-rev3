from django.import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"