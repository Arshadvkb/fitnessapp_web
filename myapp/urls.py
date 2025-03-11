
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.login),
    path('loginpost',views.loginpost),
    path('admin_add_expert',views.admin_add_expert),
    path('admin_add_expert_post',views.admin_add_expert_post),
    path('admin_ad_trainer',views.admin_ad_trainer),
    path('admin_batch_allocation',views.admin_batch_allocation),
    path('admin_batch_allocation_post',views.admin_batch_allocation_post),
    path('admin_events',views.admin_events),
    path('admin_events_post',views.admin_events_post),
    path('admin_view_expert',views.admin_view_expert),
    path('admin_edit_expert/<id>',views.admin_edit_expert),
    path('admin_edit_expert_post',views.admin_edit_expert_post),
    path('admin_delete_expert/<id>',views.admin_delete_expert),
    path('admin_view_events',views.admin_view_events),
    path('admin_home',views.admin_home),
    path('trainer_home',views.trainer_home),
    path('admin_view_trainer',views.admin_view_trainer),
    path('admin_view_user',views.admin_view_user),
    path('admin_work_allocation/<id>',views.admin_work_allocation),
    path('admin_work_allocation_post',views.admin_work_allocation_post),
    path('trainer_online_training_video',views.trainer_online_training_video),
    path('trainer_view_video',views.trainer_view_video),
    path('Trainer_Edit_video/<id>',views.Trainer_Edit_video),
    path('Trainer_Edit_video_Post',views.Trainer_Edit_video_Post),
    path('Trainer_Delete_video/<id>',views.Trainer_Delete_video),
    path('trainer_online_training_video_post',views.trainer_online_training_video_post),
    path('trainer_view_attendance',views.trainer_view_attendance),
    path('trainer_view_times_schedule',views.trainer_view_times_schedule),
    path('admin_ad_trainer_post',views.admin_ad_trainer_post),
    path('admin_edit_trainer_post',views.admin_edit_trainer_post),
    path('admin_edit_events/<id>',views.admin_edit_events),
    path('admin_edit_events_post',views.admin_edit_events_post),
    path('delete_trainer/<id>',views.delete_trainer),
    path('admin_delete_event/<id>',views.admin_delete_event),
    path('admin_auto_delete_event/<id>',views.admin_auto_delete_event),
    path('admin_edit_trainer/<int:id>',views.admin_edit_trainer),
    path('Trainer_Manage_work',views.Trainer_Manage_work),
    path('Trainer_accept_Work/<id>',views.Trainer_accept_Work),
    path('Trainer_reject_Work/<id>',views.Trainer_reject_Work),
    path('Triner_View_Attandance',views.Triner_View_Attandance),
    path('Admin_view_work_status',views.Admin_view_work_status),
    path('Trainer_view_accepted_work',views.Trainer_view_accepted_work),
    path('Admin_fee_pending',views.Admin_fee_pending),
    path('Trainer_completed_work/<id>',views.Trainer_completed_work),
    path('admin_view_complaints',views.admin_view_complaints),

# ==============================================================================================================
                                        #    FLUTTER
# ===========================================================================================================
                    #   login
     path('androiod_login_POST',views.androiod_login_POST),





# =========================================================================================================
                        #  user
    path('user_viewvideo',views.user_viewvideo),
    path('user_register',views.user_register),
    path('user_view_time',views.user_view_time),
    path('user_home',views.user_home),
    path('user_add_diet',views.user_add_diet),
    path('user_add_workout',views.user_add_workout),
    path('user_sent_complaint',views.user_sent_complaint),



# ===========================================================================================================
                    #   expert


    path('expert_helth_tips',views.expert_helth_tips),



]
