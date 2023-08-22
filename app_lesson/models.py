from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()

class Advertisement(models.Model):
    title=models.CharField(
        max_length=100,
        verbose_name='Название',


    )

    description=models.TextField(
        verbose_name='Описание',
    )
    price=models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2
    )

    auction=models.BooleanField(
        verbose_name='Торг',
        default=False
    )

    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"

    )
    updated_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата редактирования'
    )
    user=models.ForeignKey(
        to=User,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )
    image=models.ImageField(
        upload_to='advertisements/',
        verbose_name='изображение'
    )
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time= self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='дата редактирования')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;">Обновлено в {}</span>', created_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Изображение')
    def image_g(self):
        if self.image:
            return format_html(
                '<img src="%s"  width=" 150" height="100"/>' % self.image.url
                )
        else:
            return format_html(
                '<img src="/static/img/img.png" width=" 150" height="100"/>'
            )


    class Admin:
        list_display = ["id", "title"]

    def __str__(self):
        return "%s    %s"%(self.id,self.title)

    class Meta:
        db_table='advertisement'
        verbose_name='Объявление'
        verbose_name_plural='Объявления'
