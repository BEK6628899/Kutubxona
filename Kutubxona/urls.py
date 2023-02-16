from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bosh_sahifa),
    path('adminlar/',adminlar),
    path('Admin/<int:son>/',admin_ozgartir),
    path('talabalar/',hammatalabalar),
    path('talaba/<int:son>/',talaba_ozgartir),
    path('mualliflar/',mualliflar),
    path('muallif/<int:son>/',muallif_ozgartir),
    path('kitoblar/',barcha_kitoblar),
    path('kitob/<int:son>/',kitob_ozgartir),
    path('bitta_record/<int:son>/',record_ozgartir),
    path('record/',records),
    path('oxirgirecord/', record_oxirgi),
    path('bitiruvchirecord/', bitiruvchi_record),
    path('talaba_ochir/<int:son>/',talaba_ochir),
    path('kitob_ochir/<int:son>/',kitob_ochir),
    path('record_ochir/<int:son>/',record_ochir),
    path('muallif_ochir/<int:son>/',muallif_ochir),
    path('admin_ochir/<int:son>/',admin_ochir),
]




