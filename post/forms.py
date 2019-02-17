from django.forms import ModelForm
from post.models import Post,Comment

class CreatePostForm(ModelForm):
    class Meta:
         model = Post
         fields = ['group', 'title','content']


class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('post', 'comment_auther', 'comment_text')
