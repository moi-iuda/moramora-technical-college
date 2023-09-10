from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django import forms


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
        self.fields['is_active'].widget.attrs.update(
            {'class': 'form-check-input', 'type': 'checkbox'})


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
        self.fields['is_active'].widget.attrs.update(
            {'class': 'form-check-input', 'type': 'checkbox'})
        self.fields['sem_one_reg_begins'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_one_reg_ends'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_one_cls_begins'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_one_cls_ends'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_one_brk_begins'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_one_brk_ends'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_two_reg_begins'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_two_reg_ends'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_two_cls_begins'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})
        self.fields['sem_two_cls_ends'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})

        # for name, field in self.fields.items():
        #     field.widget = forms.widgets.DateInput(
        #         {'class': 'form-control', 'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'})


class FeesForm(ModelForm):
    class Meta:
        model = FeeStructure
        fields = "__all__"
        labels = {
            'desc': 'Description',
            'hecas_resid': 'HECAS Residence',
            'hecas_non_resid': 'HECAS Non-Residence',
            'ss_resid': 'Self-Sponsor Residence',
            'ss_non_resid': 'Self-Sponsor Non-Residence',
            'is_active': 'Active',
        }

    def __init__(self, *args, **kwargs):
        super(FeesForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        labels = {
            'inst': 'Institution'
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'form-control'})

        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"
        labels = {
            "inst_name": "Institution",
            "is_active": "Is active"
        }

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widgets.attrs.update({'class': 'form-control'})


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
        super(LatestUpdateForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


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
        super(NoticeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


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
        super(ProgrammeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trade'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update(
            {'class': 'form-check-input', 'type': 'checkbox'})


class InstitutionForm(ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'

        labels = {
            'inst_name': 'Institution',
            'img': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})


class TradeImageLibraryForm(ModelForm):
    class Meta:
        model = ImageLibrary
        fields = "__all__"

        labels = {
            'img': 'Image',
            'desc': 'Description',
        }

    def __init__(self, *args, **kwargs):
        super(TradeImageLibraryForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'checkbox'})
