from django.shortcuts import render
from django.views.generic import ListView, CreateView
from CollegeAdmin.models import TopicReview
from Mentor.models import TopicInfo, MentorInfo
from Mentor.form import TopicInfoForm


# Create your views here.
class TopicListView(ListView):
    model = TopicReview
    template_name = 'TopicInfoList.html'
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        username = self.request.session.get('username')
        queryset = TopicReview.objects.filter(topic__mentor_id = username) if username else TopicReview.objects.none()
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context


class TopicInfoCreateView(CreateView):
    model = TopicInfo
    form_class = TopicInfoForm
    template_name = 'TopicCreateView.html'
    success_url = '/teacher/home'
    extra_context = {'title': '创建课题'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.mentor = MentorInfo.objects.get(id = self.request.session.get('username'))
        response = super().form_valid(form)
        TopicReview.objects.create(topic = self.object)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context
