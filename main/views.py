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


def home(request):
    """ 
    This view will act as the home. It extracts data from the Institution model
    """
    institution = Institution.objects.first()
    context = {'institution': institution}
    return render(request, 'main/home.html', context)


def departments(request):
    """ 
    Retrieves all the departments in the Department model
    """
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'main/departments.html', context)


def department(request, pk):
    """ 
    This displays the department based when the user click on the view button
    """
    department = Department.objects.get(id=pk)
    context = {'department': department}
    return render(request, 'main/department.html', context)


def programmes(request):
    """ 
    Retrieves all the programmes from the programme model
    """
    programmes = Programme.objects.all()[:10]
    context = {'programmes': programmes}
    return render(request, 'main/programmes.html', context)


def programme(request, pk):
    """ 
    Displays the programme if the user click on the view button
    """
    programme = Programme.objects.get(id=pk)
    context = {'programme': programme}
    return render(request, 'main/programme.html', context)


def latest_updates(request):
    """
    Lists all the new update from the college
    """
    latest_updates = LatestUpdate.objects.all()[:10]
    context = {'latest_updates': latest_updates}
    return render(request, 'main/latest_updates.html', context)


def latest_update(request, pk):
    """ 
    Displays single update if user presses the view button
    """
    latest_update = LatestUpdate.objects.get(id=pk)
    context = {'latest_update': latest_update}
    return render(request, 'main/latest_update.html', context)


def notices(request):
    notices = Notice.objects.all()[:10]
    context = {'notices': notices}
    return render(request, 'main/notices.html', context)


def notice(request, pk):
    notice = Notice.objects.get(id=pk)
    context = {'notice': notice}
    return render(request, 'main/notice.html', context)


def acadcalendar_fees_contact(request):
    acad_cal = AcademicCalendar.objects.first()
    fee = FeeStructure.objects.first()
    contacts = Contact.objects.all()
    context = {'acad_cal': acad_cal, 'fee': fee, 'contacts': contacts}
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
    """ 
    Adds a new department
    """
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
    """ 
    Adds a new contact
    """
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
    """ 
    Adds a new institution
    """
    form = InstitutionForm()
    if request.method == "POST":
        form = InstitutionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/admin/institution_form.html', context)


@login_required(login_url='login_user')
def add_latest_update(request):
    """ 
    Adds a new latest update
    """
    form = LatestUpdateForm()
    if request.method == "POST":
        form = LatestUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('latest_updates')
    context = {'form': form}
    return render(request, 'main/admin/latest_update_form.html', context)


@login_required(login_url='login_user')
def add_notice(request):
    """ 
    Adds a new notice
    """
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
    """ 
    Adds a new programme
    """
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
    """ 
    Adds a new trade
    """
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
    """ 
    Updates the existing information in academic calendar model
    """
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
    """ 
    Updates the existing information of a department
    """
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
    """ 
    Updates the existing information of a contact
    """
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
    """ 
    Updates the existing information of an institution
    """
    institution = Institution.objects.get(id=pk)
    form = InstitutionForm(instance=institution)
    if request.method == "POST":
        form = InstitutionForm(
            request.POST, request.FILES, instance=institution)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'institution': institution}
    return render(request, 'main/admin/institution_form.html', context)


@login_required(login_url='login_user')
def update_latest_update(request, pk):
    """ 
    Updates the existing information of a latest update
    """
    latest_update = LatestUpdate.objects.get(id=pk)
    form = LatestUpdateForm(instance=latest_update)
    if request.method == "POST":
        form = LatestUpdateForm(
            request.POST, request.FILES, instance=latest_update)
        if form.is_valid():
            form.save()
            return redirect('latest_updates')
    context = {'form': form, 'latest_update': latest_update}
    return render(request, 'main/admin/latest_update_form.html', context)


@login_required(login_url='login_user')
def update_notice(request, pk):
    """ 
    Updates the existing information of a notice
    """
    notice = Notice.objects.get(id=pk)
    form = NoticeForm(instance=notice)
    if request.method == "POST":
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notices')
    context = {'form': form, 'notice': notice}
    return render(request, 'main/admin/notice_form.html', context)


@login_required(login_url='login_user')
def update_programme(request, pk):
    """ 
    Updates the existing information of a programme
    """
    programme = Programme.objects.get(id=pk)
    form = ProgrammeForm(instance=programme)
    if request.method == "POST":
        form = ProgrammeForm(request.POST, request.FILES, instance=programme)
        if form.is_valid():
            form.save()
            return redirect('programmes')
    context = {'form': form, 'programme': programme}
    return render(request, 'main/admin/programme_form.html', context)


@login_required(login_url='login_user')
def update_trade(request, pk):
    """ 
    Updates the existing information of a trade
    """
    trade = Trade.objects.get(id=pk)
    form = TradeForm(instance=trade)
    if request.method == "POST":
        form = TradeForm(request.POST, request.FILES, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('trades')
    context = {'form': form, 'trade': trade}
    return render(request, 'main/admin/trade_form.html', context)
