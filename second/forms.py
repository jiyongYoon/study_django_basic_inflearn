# from django import forms
#
# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=200)
#     content = forms.CharField(label='내용', widget=forms.Textarea)


from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _ # Text를 래핑 해줄때 사용

# ModelForm은 Model과 Form 2가지의 역할을 한번에 할 수 있도록 하는 장고의 기능
# Model과 Form을 따로 쓰면, Model에 컬럼에 변동사항이 생기면 Form에도 동일하게 추가해줘야 한다.
# ModelForm은 Model을 선언함과 동시에 Form으로 사용이 가능하도록 해준다.


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }
        help_texts = {
            'title': _('제목을 입력하세요.'),
            'content': _('내용을 입력하세요.'),
        }
        error_messages = {
            'name': {
                'max_length': _('제목이 너무 깁니다. 30자 이하로 해주세요.')
            }
        }