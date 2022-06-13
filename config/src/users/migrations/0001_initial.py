# Generated by Django 4.0.3 on 2022-03-29 18:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(choices=[('GP', 'Габриэль Перейра'), ('MS', 'Мусиньо да Силвейра')], max_length=5, verbose_name='Школа')),
                ('sex', models.CharField(choices=[('F', 'Женщина'), ('M', 'Мужчина')], max_length=5, verbose_name='Пол')),
                ('age', models.IntegerField(help_text='От 15 до 22 лет', validators=[django.core.validators.MaxValueValidator(22), django.core.validators.MinValueValidator(15)], verbose_name='Возраст')),
                ('address', models.CharField(choices=[('U', 'Городской'), ('R', 'Сельский')], max_length=5, verbose_name='Тип адреса')),
                ('famsize', models.CharField(choices=[('LE3', 'Меньше или равно 3'), ('GT3', 'Больше 3')], max_length=5, verbose_name='Размер семьи')),
                ('pstatus', models.CharField(choices=[('T', 'совместное проживание'), ('A', 'Отдельное')], max_length=5, verbose_name='Статус совмесного проживания семьи')),
                ('medu', models.IntegerField(verbose_name='Образование матери')),
                ('fedu', models.IntegerField(verbose_name='Образование отца')),
                ('mjob', models.CharField(choices=[('Учитель', 'Учитель'), ('Медицинское обслуживание', 'Медицинское обслуживание'), ('На дому', 'На дому'), ('Другое', 'Другое')], max_length=50, verbose_name='Работа матери')),
                ('fjob', models.CharField(choices=[('Учитель', 'Учитель'), ('Медицинское обслуживание', 'Медицинское обслуживание'), ('На дому', 'На дому'), ('Другое', 'Другое')], max_length=50, verbose_name='Работа отца')),
                ('reason', models.CharField(max_length=50, verbose_name='Причина выбора этой школы')),
                ('guardian', models.CharField(max_length=30, verbose_name='Опекун учащегося')),
                ('traveltime', models.IntegerField(verbose_name='Время пути от дома до школы')),
                ('studytime', models.IntegerField(verbose_name='Еженедельное учебное время')),
                ('failures', models.IntegerField(verbose_name='Количество прошлых сбоев класса')),
                ('schoolsup', models.BooleanField(verbose_name='Дополнительная образовательная поддержка')),
                ('famsup', models.BooleanField(verbose_name='Семейная образовательная поддержка')),
                ('paid', models.BooleanField(verbose_name='Дополнительные оплаиваемые занятия по предмету курса')),
                ('activities', models.BooleanField(verbose_name='Внеклассные занятия')),
                ('nursery', models.BooleanField(verbose_name='Детский сад')),
                ('higher', models.BooleanField(verbose_name='Хочет получить высшее образование')),
                ('romantic', models.BooleanField(verbose_name='В отношениях')),
                ('famrel', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Качество семейных отношений')),
                ('freetime', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Свободное время после школы')),
                ('goout', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Выход с друзьями')),
                ('dalc', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Потребление алкоголя в рабочий день')),
                ('walc', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Потребление алкоголя в выходные дни')),
                ('healh', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Текущее состояние здоровья')),
                ('absences', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Количество пропусков занятий в школе')),
                ('g1', models.IntegerField(help_text='От 0 до 20', validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)], verbose_name='Оценка за первый период')),
                ('g2', models.IntegerField(help_text='От 0 до 20', validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)], verbose_name='Оценка за второй период')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]