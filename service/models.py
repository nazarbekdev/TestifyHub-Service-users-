from django.db import models


class ServiceUser(models.Model):
    name = models.CharField(max_length=255)
    limit = models.IntegerField(default=50)
    status = models.BooleanField(default=False)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BotUser(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.BigIntegerField()
    referral_link = models.CharField(max_length=255, blank=True, null=True)
    invited_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    balans = models.IntegerField(default=3000)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DatabaseType(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubjectCategory(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject Category'
        verbose_name_plural = 'Subject Categories'


class Document(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    subject_category = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE)
    database_type = models.ForeignKey(DatabaseType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='document/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class TitulUpload(models.Model):
    document = models.FileField(upload_to='files')

    def __str__(self):
        return str(self.document)


class Question(models.Model):
    subject_id = models.IntegerField()
    subject_category_id = models.IntegerField()
    language_id = models.IntegerField()
    database_type_id = models.IntegerField()
    question = models.TextField()
    answers = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class GenerateTest(models.Model):
    database_type = models.ForeignKey(DatabaseType, on_delete=models.CASCADE)
    subject1 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_1')
    subject2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_2')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='language')
    number_books = models.IntegerField()
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, related_name='user_tests')

    def __str__(self):
        return self.user.name


class GenerateTestData(models.Model):
    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    number_books = models.IntegerField()
    user = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class TestControl(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE)
    question_limit = models.IntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject.name

    class Meta:
        unique_together = ('subject', 'category')
        verbose_name = 'Test Control'
        verbose_name_plural = 'Test Controls'


class AnswerTest(models.Model):
    book_code = models.IntegerField()
    answers = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book_code)


class UserFile(models.Model):
    user = models.IntegerField()
    file = models.FileField(upload_to='userfile/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CheckSheet(models.Model):
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=20, null=True, blank=True)
    file = models.FileField(upload_to='check_file/inputfile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class CheckSheetResult(models.Model):
    user = models.CharField(max_length=50)
    file = models.FileField(upload_to='check_file/outputfile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Key(models.Model):
    exam_type_choices = [
        ('AB', 'AB')
    ]
    exam_type = models.CharField(max_length=2, choices=exam_type_choices, default='AB')
    keys = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} Keys"


class Fanlar(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Fanlar'
        verbose_name_plural = 'Fanlar'


class OTM2025(models.Model):
    yonalish_kodi = models.IntegerField()
    yonalish_nomi = models.CharField(max_length=255)
    fan1 = models.ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='fan1_kodi')
    fan2 = models.ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='fan2_kodi')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.yonalish_nomi

    class Meta:
        verbose_name = 'OTM2025'
        verbose_name_plural = 'OTM2025'


class BlokTest(models.Model):
    telegram_id = models.BigIntegerField()
    ism_familiya = models.CharField(max_length=255)
    telefon_raqam = models.CharField(max_length=255)
    viloyat = models.CharField(max_length=255)
    fan1 = models.CharField(max_length=255)
    fan2 = models.CharField(max_length=255)
    rejalashtirilgan_vaqt = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[
            ('kutmoqda', '🟡 Kutmoqda'),
            ('yechmoqda', '🟠 Yechmoqda'),
            ('yakunlandi', '🟢 Yakunlandi'),
            ('topshirmadi', '🔴 Topshirmadi'),
        ],
        default='kutmoqda'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism_familiya


class Natijalar(models.Model):
    telegram_id = models.BigIntegerField()
    ism = models.CharField(max_length=255)
    viloyat = models.CharField(max_length=255)
    blok1 = models.CharField(max_length=255)
    blok2 = models.CharField(max_length=255)
    majburiy = models.IntegerField()
    fan1 = models.IntegerField()
    fan2 = models.IntegerField()
    ball = models.FloatField()
    javoblari = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Natijalar'
        verbose_name_plural = 'Natijalar'

    def __str__(self):
        return self.ism
