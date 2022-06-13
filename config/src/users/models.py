from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class DataChoicer:
    status_choicer = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    edu_choicer = (
        (0, 'Нет'),
        (1, 'Начальное'),
        (2, '5-9 классы'),
        (3, 'Среднее образование'),
        (4, 'Высшее образование')
    )

    reason_choicer = (
        ('Близость к дому', 'Близость к дому'),
        ('Репутация школы', 'Репутация школы'),
        ('Предпочтения курса', 'Предпочтения курса'),
        ('Другое', 'Другое'),
    )

    guardan_choicer = (
        ('Отец', 'Отец'),
        ('Мать', 'Мать'),
        ('Другой', 'Другой')
    )

    traver_choicer = (
        (1, '<15 мин.'),
        (2, 'От 15 до 30 мин.'),
        (3, '>1 часа')
    )

    studytime_choicer = (
        (1, '<2 часов'),
        (2, 'От 2 до 5 часов'),
        (3, 'От 5 до 10 часов'),
        (4, '>10 часов')
    )



class UserProfiles(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    school = models.CharField(verbose_name='Школа', max_length=5, choices=(('GP', 'Габриэль Перейра'),('MS', 'Мусиньо да Силвейра')))
    sex = models.CharField(verbose_name='Пол', max_length=5, choices=(('F', 'Женщина'), ('M', 'Мужчина')))
    age = models.IntegerField(verbose_name='Возраст', help_text='От 15 до 22 лет', validators= [
        MaxValueValidator(22),
        MinValueValidator(15)
    ])
    address = models.CharField(max_length=5, verbose_name='Тип адреса', choices=(('U', 'Городской'), ('R', 'Сельский')))
    famsize = models.CharField(max_length=5, verbose_name='Размер семьи', choices=(('LE3', 'Меньше или равно 3'),('GT3', 'Больше 3')))
    pstatus = models.CharField(max_length=5, verbose_name='Статус совмесного проживания семьи', choices=(('T', 'Совместное проживание'),('A', 'Отдельное')))
    medu = models.IntegerField(verbose_name='Образование матери', choices=DataChoicer.edu_choicer)
    fedu = models.IntegerField(verbose_name='Образование отца', choices=DataChoicer.edu_choicer)
    mjob = models.CharField(max_length=50, verbose_name='Работа матери', 
                            choices=(('Учитель', 'Учитель'),
                                    ('Медицинское обслуживание', 'Медицинское обслуживание'),
                                    ('На дому', 'На дому'),
                                    ('Другое','Другое')))
    fjob = models.CharField(max_length=50, verbose_name='Работа отца', 
                            choices=(('Учитель', 'Учитель'),
                                    ('Медицинское обслуживание', 'Медицинское обслуживание'),
                                    ('На дому', 'На дому'),
                                    ('Другое','Другое')))
    reason = models.CharField(max_length=50, verbose_name='Причина выбора этой школы', choices=DataChoicer.reason_choicer)
    guardian = models.CharField(max_length=30, verbose_name='Опекун учащегося', choices=DataChoicer.guardan_choicer)
    traveltime = models.IntegerField(verbose_name='Время пути от дома до школы', choices=DataChoicer.traver_choicer)
    studytime = models.IntegerField(verbose_name='Еженедельное учебное время', choices=DataChoicer.studytime_choicer)
    failures = models.IntegerField(verbose_name='Количество прошлых сбоев класса')
    schoolsup = models.BooleanField(verbose_name='Дополнительная образовательная поддержка')
    famsup = models.BooleanField(verbose_name='Семейная образовательная поддержка')
    paid = models.BooleanField(verbose_name='Дополнительные оплачиваемые занятия по предмету курса')
    activities = models.BooleanField(verbose_name='Внеклассные занятия')
    nursery = models.BooleanField(verbose_name='Детский сад')
    higher = models.BooleanField(verbose_name='Хочет получить высшее образование')
    romantic = models.BooleanField(verbose_name='В отношениях')
    famrel = models.IntegerField(verbose_name='Качество семейных отношений', choices=DataChoicer.status_choicer)
    freetime = models.IntegerField(verbose_name='Свободное время после школы', choices=DataChoicer.status_choicer)
    goout = models.IntegerField(verbose_name='Выход с друзьями', choices=DataChoicer.status_choicer)
    dalc = models.IntegerField(verbose_name='Потребление алкоголя в рабочий день', choices=DataChoicer.status_choicer)
    walc = models.IntegerField(verbose_name='Потребление алкоголя в выходные дни', choices=DataChoicer.status_choicer)
    healh = models.IntegerField(verbose_name='Текущее состояние здоровья', choices=DataChoicer.status_choicer)
    absences = models.IntegerField(verbose_name='Количество пропусков занятий в школе', choices=DataChoicer.status_choicer)
    g1 = models.IntegerField(verbose_name='Оценка за первый период',help_text='От 0 до 20',  validators= [
        MaxValueValidator(20),
        MinValueValidator(0)
    ])
    g2 = models.IntegerField(verbose_name='Оценка за второй период',help_text='От 0 до 20', validators= [
        MaxValueValidator(20),
        MinValueValidator(0)
    ])

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


    def __str__(self) -> str:
        return str(self.user)

    def save(self, force_insert: bool = False, force_update: bool = False, using = None) -> None:
        print(self.failures)
        if self.failures >= 1 and self.failures < 3:
            self.failures = 10
        else:
            self.failures = 4
        return super().save(force_insert, force_update, using)