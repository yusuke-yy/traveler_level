import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .forms import GuestDiagnosisForm,InquiryForm,PhotoCreateForm,DiagnosisForm
from .models import Photo,Diagnosis
from django.shortcuts import render
import random
from rest_framework import viewsets, filters
from .serializers import PhotoSerializer,DiagnosisSerializer

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('traveler:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by{}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class GuestDiagnosisView(generic.FormView):
    template_name = "guest_diagnosis.html"
    form_class = GuestDiagnosisForm
    l =['1','2','3']
    success_url = reverse_lazy('traveler:guest_diagnosis_result'+ random.choice(l))

class GuestDiagnosisResult1View(generic.TemplateView):
    template_name = "guest_diagnosis_result.htm1"

class GuestDiagnosisResult2View(generic.TemplateView):
    template_name = "guest_diagnosis_result2.html"

class GuestDiagnosisResult3View(generic.TemplateView):
    template_name = "guest_diagnosis_result3.html"

class PhotoListView(LoginRequiredMixin,generic.ListView):
    model = Photo
    template_name = 'photo_list.html'
    paginate_by = 4

    def get_queryset(self):
        photos = Photo.objects.filter(user=self.request.user).order_by('-created_at')
        return photos

class PhotoDetailView(LoginRequiredMixin,generic.DetailView):
    model = Photo
    template_name = 'photo_detail.html'

class PhotoCreateView(LoginRequiredMixin,generic.CreateView):
    model = Photo
    template_name = "photo_create.html"
    form_class = PhotoCreateForm
    success_url = reverse_lazy('traveler:photo_list')

    def form_valid(self,form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        messages.success(self.request,'写真を作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'写真の作成に失敗しました。')
        return super().form_invalid(form)

class DiagnosisView(LoginRequiredMixin,generic.CreateView):
    model = Diagnosis
    template_name = "diagnosis.html"
    form_class = DiagnosisForm
    success_url = reverse_lazy('traveler:my_page')

    def form_valid(self,form):
        diagnosis = form.save(commit=False)
        diagnosis.user = self.request.user
        diagnosis.save()
        messages.success(self.request,'旅人力を診断しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'旅人力診断に失敗しました。')
        return super().form_invalid(form)

class PhotoUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Photo
    template_name = "photo_update.html"
    form_class = PhotoCreateForm

    def get_success_url(self):
        return reverse_lazy('traveler:photo_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self,form):
        messages.success(self.request,'写真を作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'写真の作成に失敗しました。')
        return super().form_invalid(form)

class PhotoDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Photo
    template_name = "photo_delete.html"
    success_url = reverse_lazy('traveler:photo_list')

    def delete(self,request,*args,**kwargs):
        messages.success(self.request,'写真を削除しました。')
        return super().delete(request,*args,**kwargs)

class MyPageView(LoginRequiredMixin,generic.ListView):
    model = Diagnosis
    template_name = "my_page.html"

    def get_queryset(self):
        diagnoses = Diagnosis.objects.filter(user=self.request.user).order_by('-created_at')
        return diagnoses

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all() # 全てのデータを取得
    serializer_class = DiagnosisSerializer