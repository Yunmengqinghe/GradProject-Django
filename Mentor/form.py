from django import forms
from Mentor.models import MentorInfo, TopicInfo


class TopicInfoForm(forms.ModelForm):
    class Meta:
        model = TopicInfo
        fields = ['mentor', 'name', 'research_area', 'max_len', 'requirements']
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': '输入课题名称'}),
            'research_area': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': '输入研究方向'}),
            'max_len': forms.NumberInput(attrs = {'class': 'form-control', 'min': 1}),
            'requirements': forms.Textarea(attrs = {'class': 'form-control', 'rows': 3, 'placeholder': '输入课题要求'}),
            'mentor': forms.Select(attrs = {'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if self.request:
            self.fields['mentor'].queryset = MentorInfo.objects.filter(id = self.request.session.get('username'))
