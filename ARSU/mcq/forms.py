from django.forms import ModelForm
from .models import Topic, Mcq

class McqForm(ModelForm):
    class Meta:
        model = Mcq
        fields = ['subject', 'topic', 'question', 'answer', 'image']
class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['user', 'subject', 'heading']
