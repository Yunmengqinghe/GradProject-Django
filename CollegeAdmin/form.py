from django import forms
from django.forms import ModelForm
from CollegeAdmin.models import TopicReview, CollegeAdminInfo


class AdminInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = CollegeAdminInfo
        fields = '__all__'
        widgets = {
            'college': forms.Select(attrs = {'class': 'form-control non-editable'}),
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control-plaintext'})
        self.fields['name'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control-plaintext'})
        self.fields['password'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control-plaintext'})


class ReviewUpdateForm(ModelForm):
    topic_display = forms.CharField(
        widget = forms.Textarea(attrs = {
            'readonly': 'readonly',
            'class': 'form-control-plaintext',
            'rows': 5,
            'style': 'white-space: pre-wrap;resize: none;'
        }),
        required = False,
        label = '课题信息'
    )
    collegeAdmin_display = forms.CharField(
        widget = forms.TextInput(attrs = {
            'readonly': 'readonly',
            'class': 'form-control-plaintext'
        }),
        required = False,
        label = '管理员信息'
    )

    class Meta:
        model = TopicReview
        fields = ['review_date', 'status']
        widgets = {
            'review_date': forms.DateTimeInput(attrs = {'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs = {'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super(ReviewUpdateForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = TopicReview.STATUS_CHOICES

        topic_info = self.instance.topic
        college_admin_info = self.instance.collegeAdmin

        self.fields['topic_display'].initial = (
            f"课题编号: {topic_info.id}\n"
            f"课题名称: {topic_info.name}\n"
            f"研究方向: {topic_info.research_area}\n"
            f"最大人数: {topic_info.max_len}\n"
            f"课题要求: {topic_info.requirements}"
        )

        self.fields['collegeAdmin_display'].initial = f"姓名: {college_admin_info.name}"
