from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def login_user(request):

    if request.user.is_authenticated:
        return redirect('departments')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Password or Username is incorrect!!')

    context = {}
    return render(request, 'main/admin/login_user_form.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_user')


def account(request):
    context = {}
    return render(request, 'main/account.html', context)


def home(request):
    institution = Institution.objects.all()[0]
    context = {'institution': institution}
    return render(request, 'main/home.html', context)


def departments(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'main/departments.html', context)


def department(request, pk):
    department = Department.objects.get(id=pk)
    context = {'department': department}
    return render(request, 'main/department.html', context)


def programmes(request):
    programmes = Programme.objects.all()
    context = {'programmes': programmes}
    return render(request, 'main/programmes.html', context)


def programme(request, pk):
    programme = Programme.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'main/programme.html', context)


def latest_updates(request):
    latest_updates = LatestUpdate.objects.all()
    context = {'latest_updates': latest_updates}
    return render(request, 'main/latest_updates.html', context)


def latest_update(request, pk):
    latest_update = LatestUpdate.objects.get(id=pk)
    context = {'latest_update': latest_update}
    return render(request, 'main/latest_update.html', context)


def notices(request):
    notices = Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'main/notices.html', context)


def notice(request, pk):
    notice = Notice.objects.get(id=pk)
    context = {'notice': notice}
    return render(request, 'main/notice.html', context)


def acadcalendar_fees_contact(request):
    acad_cal = AcademicCalendar.objects.all()[0]
    fees = FeeStructure.objects.all()[0]
    contacts = Contact.objects.all()
    context = {'acad_cal': acad_cal, 'fees': fees, 'contacts': contacts}
    return render(request, 'main/acadcalendar_fees_contact.html', context)


def trades(request):
    trades = Trade.objects.all()
    context = {'trades': trades}
    return render(request, 'main/trades.html', context)


def navbar_trades(request):
    trades = Trade.objects.all()
    context = {'trades': trades}
    return render(request, 'main/navbar.html', context)


def trade_images(request, pk):
    trade = Trade.objects.get(id=pk)
    images = trade.imagelibrary_set.all()
    context = {'trade': trade, 'images': images}
    return render(request, 'main/trade_images.html', context)


@login_required(login_url='login_user')
def add_academic_calendar(request):
    form = AcademicCalendarForm()
    if request.method == "POST":
        form = AcademicCalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_n_fees')
    context = {'form': form}
    return render(request, 'main/admin/academic_calendar_form.html', context)


@login_required(login_url='login_user')
def add_department(request):
    form = DepartmentForm()
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
    context = {'form': form}
    return render(request, 'main/admin/department_form.html', context)


@login_required(login_url='login_user')
def add_contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/admin/contact_form.html', context)


@login_required(login_url='login_user')
def add_institution(request):
    form = InstitutionForm()
    if request.method == "POST":
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/admin/institution_form.html', context)


@login_required(login_url='login_user')
def add_latest_update(request):
    form = LatestUpdateForm()
    if request.method == "POST":
        form = LatestUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('latest_updates')
    context = {'form': form}
    return render(request, 'main/admin/latest_update_form.html', context)


@login_required(login_url='login_user')
def add_notice(request):
    form = NoticeForm()
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notices')
    context = {'form': form}
    return render(request, 'main/admin/notice_form.html', context)


@login_required(login_url='login_user')
def add_programme(request):
    form = ProgrammeForm()
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('programmes')
    context = {'form': form}
    return render(request, 'main/admin/programme_form.html', context)


@login_required(login_url='login_user')
def add_trade(request):
    form = TradeForm()
    if request.method == "POST":
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trades')
    context = {'form': form}
    return render(request, 'main/admin/trade_form.html', context)


@login_required(login_url='login_user')
def update_academic_calendar(request, pk):
    academic_calendar = AcademicCalendar.objects.get(id=pk)
    form = AcademicCalendarForm(instance=academic_calendar)
    if request.method == "POST":
        form = AcademicCalendarForm(request.POST, instance=academic_calendar)
        if form.is_valid():
            form.save()
            return redirect('academic_calendar')
    context = {'form': form, "academic_calendar": academic_calendar}
    return render(request, 'main/admin/academic_calendar_form.html', context)


@login_required(login_url='login_user')
def update_department(request, pk):
    department = Department.objects.get(id=pk)
    form = DepartmentForm(instance=department)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('departments')
    context = {'form': form, 'department': department}
    return render(request, 'main/admin/department_form.html', context)


@login_required(login_url='login_user')
def update_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'contact': contact}
    return render(request, 'main/admin/contact_form.html', context)


@login_required(login_url='login_user')
def update_institution(request, pk):
    institution = Institution.object.get(id=pk)
    form = InstitutionForm(instance=institution)
    if request.method == "POST":
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'institution': institution}
    return render(request, 'main/admin/institution_form.html', context)


@login_required(login_url='login_user')
def update_latest_update(request, pk):
    latest_update = LatestUpdate.objects.get(id=pk)
    form = LatestUpdateForm(instance=latest_update)
    if request.method == "POST":
        form = LatestUpdateForm(request.POST, instance=latest_update)
        if form.is_valid():
            form.save()
            return redirect('latest_updates')
    context = {'form': form, 'latest_update': latest_update}
    return render(request, 'main/admin/latest_update_form.html', context)


@login_required(login_url='login_user')
def update_notice(request, pk):
    notice = Notice.objects.get(id=pk)
    form = NoticeForm(instance=notice)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notices')
    context = {'form': form, 'notice': notice}
    return render(request, 'main/admin/notice_form.html', context)


@login_required(login_url='login_user')
def update_programme(request, pk):
    programme = Programme.objects.get(id=pk)
    form = ProgrammeForm(instance=programme)
    if request.method == "POST":
        form = ProgrammeForm(request.POST, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('programmes')
    context = {'form': form, 'programme': programme}
    return render(request, 'main/admin/programme_form.html', context)


@login_required(login_url='login_user')
def update_trade(request, pk):
    trade = Trade.objects.get(id=pk)
    form = TradeForm()
    if request.method == "POST":
        form = TradeForm(request.POST, trade)
        if form.is_valid():
            form.save()
            return redirect('trades')
    context = {'form': form, 'trade': trade}
    return render(request, 'main/admin/trade_form.html', context)
