from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from CollegeAdmin.models import TopicReview, CollegeAdminInfo
from CollegeAdmin.form import ReviewUpdateForm, AdminInfoUpdateForm


class TopicListView(ListView):
    template_name = 'TopicListView.html'
    queryset = TopicReview.objects.exclude(status = 0).order_by('-id')
    paginate_by = 10
    context_object_name = 'review_lists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context


class TopicReviewListView(ListView):
    template_name = 'TopicUndoList.html'
    queryset = TopicReview.objects.filter(status = 0).order_by('id')
    paginate_by = 10
    context_object_name = 'review_lists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context


class ReviewUpdateView(UpdateView):
    template_name = 'ReviewDetailView.html'
    model = TopicReview
    form_class = ReviewUpdateForm
    success_url = '/collegeadmin/undo-list'
    extra_context = {'title': '审核课题'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context


class TopicDetailView(DetailView):
    template_name = 'TopicDetailView.html'
    extra_context = {'title': '课题信息详情'}
    model = TopicReview
    context_object_name = 'topic_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context


class AdminInfoUpdateView(UpdateView):
    template_name = 'AdminInfo.html'
    model = CollegeAdminInfo
    form_class = AdminInfoUpdateForm
    extra_context = {'title': '修改个人信息'}
    success_url = '/collegeadmin/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username', None)
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return CollegeAdminInfo.objects.get(pk=pk)

def topicScore(request):
    return render(request, 'TopicScore.html')
