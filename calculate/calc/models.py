from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from django.utils import timezone
from .validators import validate_height_weight_age
from .mixins import ProfileCaloriesMixin


class Profile(ProfileCaloriesMixin, models.Model):
    TARGETS = (
        ("1", 'Похудеть'),
        ("2", 'Баланс'),
        ("3", 'Набрать массу'),
    )
    ACTIVITY = (
        ("1.2", 'Небольшая'),
        ("1.375", 'Средняя'),
        ("1.5", 'Выше среденей'),
        ("1.725", 'Высокая'),
    )
    SEX = (
        ("woman", 'Женский'),
        ("man", 'Мужской'),
    )
    name = models.CharField('Имя', max_length=50)
    slug = models.SlugField('URL', unique=True, max_length=50, blank=True)
    target = models.CharField('Цель', choices=TARGETS, default=1, max_length=10)
    sex = models.CharField('Пол', choices=SEX, default="woman", max_length=10)
    photo = models.ImageField('Фото', upload_to='profile', blank=True, null=True, default='no_person.jpg')
    height = models.PositiveSmallIntegerField('Рост', null=True, validators=[validate_height_weight_age])
    weight = models.PositiveSmallIntegerField('Вес', null=True, validators=[validate_height_weight_age])
    age = models.PositiveSmallIntegerField('Возраст', validators=[validate_height_weight_age])
    activity = models.CharField('Активность', choices=ACTIVITY, default=1.25, max_length=10)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}{str(timezone.now())[10:]}')
        super().save(*args, **kwargs)
