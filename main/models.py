from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Institution(models.Model):
    """
    This stores information about the college
    """
    inst_name = models.CharField(max_length=255)
    about = RichTextField(max_length=700)
    img = models.ImageField(upload_to='inst/', default='default.png')
    vision = RichTextField(max_length=350)
    mission = RichTextField(max_length=350)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.inst_name

    class Meta:
        ordering = ['-created']


class Contact(models.Model):
    """
    This stores information about the contact person for the college
    """
    inst = models.ForeignKey(Institution, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    email = models.EmailField(default='youremail@example.com', max_length=255)
    landline = models.IntegerField()
    digicel = models.IntegerField()
    telikom = models.IntegerField()
    vodaphone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_person

    class Meta:
        ordering = ['-created']


class PngNqf(models.Model):
    """ 
    This lists all the levels of PNG National Qualification Framework
    """
    nqf_level = models.CharField(max_length=10)
    qualification = models.CharField(max_length=255)

    def __str__(self):
        return self.qualification

    class Meta:
        verbose_name = 'PNG NQF'


class Department(models.Model):
    """ 
    This stores information about the respective departments in the college
    """
    dept = models.CharField(
        max_length=255, default='Department of ', unique=True)
    desc = RichTextField(max_length=1500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.dept


class Programme(models.Model):
    """ 
    This stores information on the programmes offered by the college
    """
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    inst = models.ForeignKey(Institution, on_delete=models.CASCADE)
    prog_name = models.CharField(
        max_length=255, default='National Certificate in ', unique=True)
    nqf = models.ForeignKey(PngNqf, on_delete=models.CASCADE)
    prog_code = models.CharField(max_length=10, unique=True)
    prog_duration = models.IntegerField()
    prog_quota = models.IntegerField()
    prog_description = RichTextField(max_length=2500)
    prog_requirement = RichTextField(
        max_length=1000, default='LL grade greate than B')
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prog_name

    class Meta:
        ordering = ['-prog_name']


class Notice(models.Model):
    """ 
    This provides a space for the college to post Notices for the students and public
    This is based on programmes
    """
    prog = models.ForeignKey(Programme, on_delete=models.CASCADE)
    title = models.CharField(max_length=700, unique=True)
    intro = RichTextField(max_length=700)
    img = models.ImageField(null=True, blank=True,
                            upload_to='notices/', unique=True)
    main_body = RichTextField(max_length=5000)
    outro = RichTextField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class LatestUpdate(models.Model):
    """ 
    Provides the latest news/update/development in the college
    """
    inst = models.ForeignKey(Institution, on_delete=models.CASCADE)
    title = models.CharField(max_length=700, unique=True)
    intro = RichTextField(max_length=700)
    img = models.ImageField(null=True, blank=True,
                            upload_to='updates/', default="default.png", unique=True)
    main_body = RichTextField(max_length=5000)
    outro = RichTextField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class FeeStructure(models.Model):
    """ 
    This section provides/stores information on the fee structure of the college
    """
    year = models.IntegerField(unique=True)
    desc = RichTextField(max_length=700)
    hecas_resid = models.FloatField()
    hecas_non_resid = models.FloatField()
    ss_resid = models.FloatField()
    ss_non_resid = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (f"Fee Structure for the year {self.year}")

    class Meta:
        ordering = ['-created']


class AcademicCalendar(models.Model):
    """
    This section will store information on the academic calendar of the college
    """
    year = models.IntegerField()
    note = RichTextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    sem_one_reg_begins = models.DateField()
    sem_one_reg_ends = models.DateField()
    sem_one_cls_begins = models.DateField()
    sem_one_cls_ends = models.DateField()
    sem_one_brk_begins = models.DateField()
    sem_one_brk_ends = models.DateField()
    sem_two_reg_begins = models.DateField()
    sem_two_reg_ends = models.DateField()
    sem_two_cls_begins = models.DateField()
    sem_two_cls_ends = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (f"Academic Calendar for the year {self.year}")

    class Meta:
        ordering = ['-created']


class Trade(models.Model):
    trade = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.trade


class ImageLibrary(models.Model):
    """
    This will stores images of the college
    """
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img_lib/',
                            default='default.png', unique=True)
    desc = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
