from django.urls import path

from . import views

app_name = 'traveler'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('guest_diagnosis/',views.GuestDiagnosisView.as_view(),name="guest_diagnosis"),
    path('guest_diagnosis_result1/',views.GuestDiagnosisResult1View.as_view(),name="guest_diagnosis_result1"),
    path('guest_diagnosis_result2/',views.GuestDiagnosisResult2View.as_view(),name="guest_diagnosis_result2"),
    path('guest_diagnosis_result33/',views.GuestDiagnosisResult3View.as_view(),name="guest_diagnosis_result3"),
    path('photo-list/',views.PhotoListView.as_view(),name="photo_list"),
    path('photo-detail/,<int:pk>/',views.PhotoDetailView.as_view(),name="photo_detail"),
    path('photo-create/',views.PhotoCreateView.as_view(),name="photo_create"),
    path('photo-update/<int:pk>/',views.PhotoUpdateView.as_view(),name="photo_update"),
    path('photo-delete/<int:pk>/',views.PhotoDeleteView.as_view(),name="photo_delete"),
    path('diagnosis/',views.DiagnosisView.as_view(),name="diagnosis"),
    path('my-page/',views.MyPageView.as_view(),name="my_page"),
]