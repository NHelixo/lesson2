from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField("Course")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Типи полів
class MyModel(models.Model):

    # Текст з обмеженням по довжині
    short_text = models.CharField(max_length=100)

    # Текст любого розміру
    long_text = models.TextField()

    # Цілі числа
    number = models.IntegerField()

    # float числа
    float_num = models.DecimalField(decmal_places=2, max_digits=20)

    # Дата
    date = models.DateField()

    # Дата з часом
    # Додавання дати в момент створення об'єкту: auto_now_add=True
    date_time = models.DateTimeField(auto_now_add=True)

    # Зв'язок один до багатьох
    related = models.ForeignKey(Course, related_name="one_to_many", on_delete=models.DO_NOTHING)

    # Зв'язок багато до багатьох
    many_to_many = models.ManyToManyField(Course, related_name="many")

    # bool значення
    bool = models.BooleanField(default=False)

    # Файл
    file = models.FileField()

    # Картинка
    image = models.ImageField()
