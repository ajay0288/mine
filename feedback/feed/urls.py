from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import (
    RegisterView,
    StudentFeedbackCreateVeiw,
    FeedBackDetailVeiw,
    FacultyFeedbackCreateVeiw,
    designation,
    AdminStudentDetails,
    AdminFacultyDetails,
    AdminFacultyFilterDetails,
    AdminStudentFilterDetails,
)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='feed/index.html')),

    url(r'^feed/register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(template_name='feed/registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^student/create', StudentFeedbackCreateVeiw.as_view(), name="studentfeedbackcreate"),
    url(r'^faculty/create', FacultyFeedbackCreateVeiw.as_view(), name="facultyfeedbackcreate"),

    url(r'^feedback/detail', FeedBackDetailVeiw, name="feedbackdetail"),

    url(r'designation/', designation, name='designation'),

    url(r'^adminstudentdetails$', AdminStudentDetails, name='adminstudents'),
    url(r'^adminfacultydetails$', AdminFacultyDetails, name='adminfaculty'),

    url(r'^adminstudentdetailsfilter', AdminStudentFilterDetails, name='adminstudentfilter'),
    url(r'^adminfacultydetailsfilter', AdminFacultyFilterDetails, name='adminfacultyfilter'),

]
