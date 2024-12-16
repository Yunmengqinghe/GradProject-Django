from django import forms
from django.forms import ModelForm
from CollegeAdmin.models import TopicReview


class TopicReviewForm(ModelForm):
    class Meta:
        model = TopicReview
        fields = '__all__'
        widgets = {
            'topic': forms.Select(attrs = {'class': 'disable'}),
            'collegeAdmin': forms.Select(attrs = {'class': 'disable'}),
            'review_date': forms.DateTimeInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'datetime-local',
                }
            ),
            'status': forms.Select(attrs = {'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super(TopicReviewForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = TopicReview.STATUS_CHOICES
        readonly_fields = ['topic', 'collegeAdmin']
        for field in readonly_fields:
            if field in self.fields:
                self.fields[field].disabled = True
