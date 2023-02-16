from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *



#______________________________________________________________________________________________________________________#



def bosh_sahifa(request):
    return render(request,"bosh_sahifa.html")





def adminlar(request):
    if request.method == "POST":
        forma = Admin_form(request.POST)
        if forma.is_valid():
            forma.save()
            # Admin.objects.create(
            #     ism = forma.cleaned_data.get("name"),
            #     ish_vaqti = forma.cleaned_data.get("work_time")
            # )
        return redirect("/adminlar/")
    a = request.GET.get("Search🔎")
    if a is None or a == "":
        ad = Admin.objects.all()
    else:
        ad = Admin.objects.filter(ism__contains=a)
    data = {"Adminlar":ad,"forma":Admin_form()}
    return render(request,"adminlar.html",data)


def admin_ozgartir(request,son):
    if request.method == "POST":
        Admin.objects.filter(id=son).update(
            ism = request.POST.get("i"),
            ish_vaqti = request.POST.get("ish")
        )
        return redirect("/adminlar/")
    data = {"Admin":Admin.objects.get(id=son)}
    return render(request,"bita_admin.html",data)


def admin_ochir(request,son):
    Admin.objects.get(id=son).delete()
    return redirect("/adminlar/")





def hammatalabalar(request):
    if request.method == "POST":
        forma = talaba_form(request.POST)
        if forma.is_valid():
            talaba.objects.create(
                ism = forma.cleaned_data.get("name"),
                kursi = forma.cleaned_data.get("course"),
                kitoblar_soni = forma.cleaned_data.get("books"),
                bitiruvchi = forma.cleaned_data.get("gradute")
            )
        return redirect("/talabalar/")
    a = request.GET.get("Search🔎")
    if a is None or a=="":
       st = talaba.objects.all()
    else:
        st = talaba.objects.filter(ism__contains=a)
    talabalar = {"Talabalar":st,
                 "forma":talaba_form()}
    return render(request,"talabalar.html",talabalar)


def talaba_ozgartir(request,son):
    if request.method=="POST":
        if request.POST.get("b") == "on":
            bitiruvchi_qiymati = "ha"
        else:
            bitiruvchi_qiymati = "yo`q"
        talaba.objects.filter(id=son).update(
            ism = request.POST.get("i"),
            kursi = request.POST.get("k"),
            kitoblar_soni = request.POST.get("k_s"),
            bitiruvchi = bitiruvchi_qiymati
        )
        return redirect("/talabalar/")
    data = {"talaba":talaba.objects.get(id=son)}
    return render(request,"bita_talaba.html",data)


def talaba_ochir(request,son):
    talaba.objects.get(id=son).delete()
    return redirect("/talabalar/")





def mualliflar(request):
    if request.method=="POST":
        muallif.objects.create(
            ism = request.POST.get("i"),
            kitob_soni = request.POST.get("k"),
            tugilgan_sanasi = request.POST.get("t"),
            jinsi = request.POST.get("j")
        )
        return redirect("/mualliflar/")
    m = request.GET.get("Search🔎")
    if m is None or m=="":
        mi=muallif.objects.all()
    else:
        mi=muallif.objects.filter(ism__contains=m)
    data = {"Mualliflar":mi}
    return render(request,"muallif.html",data)


def muallif_ozgartir(request,son):
    if request.method == "POST":
        if request.POST.get("t") == "on":
            muallifning_trikligi = "ha"
        else:
            muallifning_trikligi = "yo`q"
        muallif.objects.filter(id=son).update(
            ism = request.POST.get("i"),
            kitob_soni = request.POST.get("k_s"),
            jinsi = request.POST.get("j"),
            tugilgan_sanasi = request.POST.get("t_s"),
            yosh = request.POST.get("y"),
            trik = muallifning_trikligi
        )
        return redirect("/mualliflar/")
    data = {"muallif":muallif.objects.get(id=son)}
    return render(request,"bitta_muallif.html",data)


def muallif_ochir(request,son):
    muallif.objects.get(id=son).delete()
    return redirect("/mualliflar/")





def barcha_kitoblar(request):
    if request.method == "POST":
        froma = kitob_form(request.POST)
        if froma.is_valid():
            froma.save()
        # kitob.objects.create(
        #     nom = request.POST.get("n"),
        #     sahifa = request.POST.get("s"),
        #     janr = request.POST.get("j"),
        #     muallif = muallif.objects.get(id = request.POST.get("m"))
        # )
        return redirect("/kitoblar/")
    k = request.GET.get("Search🔎")
    if k is None or k=="":
        ki=kitob.objects.all()
    else:
        ki=kitob.objects.filter(nom__contains=k)
    data = {"barcha_kitob":ki,
            "Mualliflar":muallif.objects.all(),"forma":kitob_form()}
    return render(request,"Barcha_kitoblar.html",data)


def kitob_ozgartir(request,son):
    if request.method=="POST":
        kitob.objects.filter(id=son).update(
            nom = request.POST.get("n"),
            sahifa = request.POST.get("s"),
            janr = request.POST.get("j"),
            muallif = muallif.objects.get(id = request.POST.get("m"))
        )
        return redirect("rejalar/")
    data = {"kitob":kitob.objects.get(id=son),"Mualliflar":muallif.objects.all()}
    return render(request,"Kitob_id.html",data)


def kitob_ochir(request,son):
    kitob.objects.get(id=son).delete()
    return redirect("/kitoblar/")





def records(request):
    if request.method == "POST":
        # forma = record_form(request.POST)
        # if forma.is_valid():
        #     forma.save()
        record.objects.create(
            talaba = talaba.objects.get(id=request.POST.get("t")),
            kitob = kitob.objects.get(id=request.POST.get("k")),
            Admin = Admin.objects.get(id=request.POST.get("a")),
            olingan_sana = request.POST.get("o"),
            qaytarish_sanasi = request.POST.get("qs"),
            qaytardi = request.POST.get("q")
        )
        return redirect("/record/")
    r = request.GET.get("Search🔎")
    if r is None or r=="":
        re=record.objects.all()
    else:
        re=record.objects.filter(talaba__ism__contains=r)
    data = {"recordlar":re,"Talabalar":talaba.objects.all(),
            "Kitoblar":kitob.objects.all(),"adminlar":Admin.objects.all(),
            "forma":record_form()}
    return render(request,"record.html",data)


def record_ozgartir(request,son):
    if request.method == "POST":
        if request.POST.get("q") == "on":
            qaytar = "ha"
        else:
            qaytar = "yo`q"
        record.objects.filter(id=son).update(
        qaytarish_sanasi=request.POST.get("q_s"),
        qaytardi=qaytar
        )
        return redirect("/record/")
    data = {"record":record.objects.get(id=son)}
    return render(request,"bitta_record.html",data)


def record_oxirgi(request):
    data = {"oxirgi_3_tasi":record.objects.order_by("-olingan_sana")[:3]}
    return render(request,"oxirgi_record.html",data)


def bitiruvchi_record(request):
    data = {"bitiruvchilar":record.objects.filter(talaba__bitiruvchi="ha")}
    return render(request,"record_bitiruvchi.html",data)


def record_ochir(request,son):
    record.objects.get(id=son).delete()
    return redirect("/record/")


#______________________________________________________________________________________________________________________#


































