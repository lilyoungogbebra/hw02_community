from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group

# class PostAdmin(admin.ModelAdmin):
# Перечисляем поля, которые должны отображаться в админке
# list_display = ('text', 'pub_date', 'author')
# Добавляем интерфейс для поиска по тексту постов
# search_fields = ('text',)
# Добавляем возможность фильтрации по дате
# list_filter = ('pub_date',)


class PostAdmin(admin.ModelAdmin):
    list_display = ( 
        'pk',
        'text',
        'pub_date', 
        'author',
        'group',)
    list_editable = ('group',)
    search_fields = ('text',) 
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Group)




