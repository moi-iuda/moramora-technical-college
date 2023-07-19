from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

        labels = {
            'dept': 'Department',
            'desc': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dept'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'department '})
        self.fields['desc'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'department description'})


class AcademicCalendarForm(ModelForm):
    class Meta:
        model = AcademicCalendar
        fields = "__all__"
        labels = {
            'desc': 'Description',
            'sem_one_reg_begins': 'Semester One Registration - Starting Date',
            'sem_one_reg_ends': 'Semester One Registration - Closing Date',
            'sem_one_cls_begins': 'Semester One Classes - Starting Date',
            'sem_one_cls_ends': 'Semester One Classes - Ending Date',
            'sem_one_brk_begins': 'Semester One Break - Starting Date',
            'sem_one_brk_ends': 'Semester One Break - Ending Date',
            'sem_two_reg_begins': 'Semester Two Registration - Starting Date',
            'sem_two_reg_ends': 'Semester Two Registration - Ending Date',
            'sem_two_cls_begins': 'Semester One Classes - Starting Date',
            'sem_two_cls_ends': 'Semester Two Classes - Ending Date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['note'].widget.attrs.update({'class': 'form-control'})
        self.fields['sem_one_reg_begins'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_one_reg_ends'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_one_cls_begins'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_one_cls_ends'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_one_brk_begins'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_one_brk_ends'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_two_reg_begins'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_two_reg_ends'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_two_cls_begins'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['sem_two_cls_ends'].widget.attrs.update(
            {'class': 'form-control'})


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"
        labels = {
            "inst_name": "Institution",
            "is_active": "Is active"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inst_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['about'].widget.attrs.update({'class': 'form-control'})
        self.fields['vision'].widget.attrs.update({'class': 'form-control'})
        self.fields['mission'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update(
            {'class': 'form-check-input'})


class LatestUpdateForm(ModelForm):
    class Meta:
        model = LatestUpdate
        fields = "__all__"
        labels = {
            'inst': 'Institution',
            'intro': 'Introduction',
            'img': 'Image',
            'main_body': 'Main Body',
            'outro': 'Outroduction',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inst'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['intro'].widget.attrs.update({'class': 'form-control'})
        self.fields['main_body'].widget.attrs.update({'class': 'form-control'})
        self.fields['outro'].widget.attrs.update({'class': 'form-control'})


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
        labels = {
            'prog': 'Programme',
            'intro': 'Introduction',
            'img': 'Image',
            'main_body': 'Main Body',
            'outro': 'Outroduction',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prog'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['intro'].widget.attrs.update({'class': 'form-control'})
        self.fields['main_body'].widget.attrs.update({'class': 'form-control'})
        self.fields['outro'].widget.attrs.update({'class': 'form-control'})


class ProgrammeForm(ModelForm):
    class Meta:
        model = Programme
        fields = "__all__"
        labels = {
            "dept": "Department",
            "inst": "Institution",
            "prog_name": "Programme Name",
            "nqf": "NQF Level",
            "prog_code": "Programme Code",
            "prog_duration": "Programme Duration",
            "prog_quota": "Programme Quota",
            "prog_description": "Programme Description",
            "is_active": "Is Active",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dept'].widget.attrs.update({'class': 'form-control'})
        self.fields['inst'].widget.attrs.update({'class': 'form-control'})
        self.fields['prog_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['nqf'].widget.attrs.update({'class': 'form-control'})
        self.fields['prog_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['prog_duration'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['prog_quota'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['prog_description'].widget.attrs.update(
            {'class': 'form-control'})


class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trade'].widget.attrs.update({'class': 'form-control'})
