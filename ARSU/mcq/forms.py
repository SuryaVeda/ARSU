from django.forms import ModelForm
from .models import Topic, Mcq, FlashCard, Fact

class McqForm(ModelForm):
    class Meta:
        model = Mcq
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'answer', 'q_image', 'a_image']

class FlashCardForm(ModelForm):

    class Meta:
        model = FlashCard
        fields = ['question', 'answer', 'q_image',  'a_image']

class FactForm(ModelForm):
    class Meta:
        model = Fact
        fields = ['answer', 'image']

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['heading']
