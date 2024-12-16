from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from Mentor.models import TopicInfo
from CollegeAdmin.models import TopicReview
from CollegeAdmin.form import TopicReviewForm


class TopicListView(ListView):
    template_name = 'TopicList.html'
    queryset = TopicReview.objects.exclude(status = 0).order_by('-id')
    paginate_by = 10
    context_object_name = 'review_lists'


class TopicReviewListView(ListView):
    template_name = 'TopicUndoList.html'
    queryset = TopicReview.objects.filter(status = 0).order_by('id')
    paginate_by = 10
    context_object_name = 'review_lists'


class ReviewUpdateView(UpdateView):
    template_name = 'ReviewDetail.html'
    model = TopicReview
    extra_context = {'title': '审核课题'}
    form_class = TopicReviewForm
    success_url = '/collegeadmin/undo-list'


def topicScore(request):
    return render(request, 'TopicScore.html')
