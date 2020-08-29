# Домашнее задание модуля

## Текст задания

Книги издают разные издательские дома. Издательства следят за качеством переводов и издаваемой продукции. Добавим в нашу библиотеку новую модель и отсортируем книги по издательству.

Вам нужно сделать вот что:

- Добавить новую модель — Издательства. Для каждого издательства необходимо создать связь с Книгой. [x]
- Создать несколько Издательств, связать их с Книгами и вывести в отдельном Django-шаблоне в виде списка `<ul><li><>/li</ul>` с подключенным bootstrap. Шаблон должен открываться в отличном от созданных нами URL'е. [x]

Добавление издательства и связи Книга-Издательство нужно сделать в отдельной панели в админке. [x]

## Внес следующие исправления в проект

В models.py добавил класс

```python
class Publisher(models.Model):
    title = models.TextField()
    year_of_foundation = models.SmallIntegerField()
    address = models.TextField()
    books = models.ForeignKey("p_library.Book", on_delete=models.CASCADE, verbose_name=_("Книги"), related_name="publisher_book", null=True)

    def __str__(self):
        return self.title
```

В класс Book добавил еще один внешний ключ `publisher = models.ForeignKey("p_library.Publisher", on_delete=models.CASCADE, verbose_name=_("Издатель"), related_name="book_publisher")`
Теперь создадим файл миграции: `python3 manage.py makemigrations`
Применим миграции: `python3 manage.py migrate`
Импорт данных из фикстуры `python3 manage.py loaddata data_1.xml`
Добавил в admin.py новую панель

```python
from p_library.models import Book, Author, Publisher

@admin.register(Publisher)
class BookAdmin(admin.ModelAdmin):
    pass
```

Миграцию выполнил штатно, но получил ошибку при импорте фикстуры `Problem installing fixture '/home/greenfrog/Документы/webdev/jobfiles/D4/my_site/data_1.xml': Could not load p_library.Book(pk=1): NOT NULL constraint failed: p_library_book.publisher_id`
В классе Book, вот сюда `publisher = models.ForeignKey("p_library.Publisher", on_delete=models.CASCADE, verbose_name=_("Издатель"), related_name="book_publisher", null=True)` добавил `null=True`. Помогло.

В admin.py разрешил показ поля `publisher` `fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher')`

С помощью админки добавил четыре издательства, к каждой книге добавил издательство. Издательство добавляется в панеле Publishers. Это отдельная панель для добавления издатетельства и его книг.

Создал новый шаблон publisher.html  Подключаем в него Bootstrap CSS, jQuery, Bootstrap JS
В файл views.py добавил новое представление

```python
def publisher(request):
    template = loader.get_template('publisher.html')
    publishers = Publisher.objects.all()
    biblio_data = {
        "publishers": publishers,
    }
    return HttpResponse(template.render(biblio_data, request))
```

Добавим новый urlpattern в файл urls.py. `path('publisher/', views.publisher),`
Шаблон открывается по новому адресу `publisher/`

## Полезные команды

Создаем виртуальное окружение для проекта, находящегося в соответствующей папке `$ python3 -m venv D4_prj_env`. D4_prj_envn - название виртуального окружения.
Активация виртуального окружения `$ source D4_prj_env/bin/activate`. где env — это имя вашего окружения разработки.
`deactivate` - деактивация виртуального окружения
`python manage.py runserver` - запускаем Джанго (из  папки D4)
`pip3 freeze > requirements.txt` - сохраняем зависимости
`pip3 install -r requirements.txt` - устанавливаем зависимости
`python manage.py createsuperuser` - Для входа в админку создаем суперпользователя

## Что делать?

1. Скачиваем проект
2. Создаем виртуальное окружение в папке D2
3. Устанавливаем зависимости
4. Создаем суперпользователя
5. Запускаем Джанго
6. Проверяем ДЗ. С вопросами обращаться в личку в слаке. Я там под своим именем - Павел Гвоздев.
7. Хорошего дня!
