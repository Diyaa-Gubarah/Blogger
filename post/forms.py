from django.forms import ModelForm
from post.models import Post

class CreatePostForm(ModelForm):
    class Meta:
         model = Post
         fields = ['group', 'title','content']
