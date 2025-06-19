import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lesson2.settings")
django.setup()

from lesson.models import User, Category, Product, Student, Course

# Додати данні до таблиці
#User(name="Oleksandr",
#             bio="",
#             email="email@gmail.com",
#             birthday="2022-02-23"
#).save()

#Фільтрація
#user = User.objects.filter(id=1).all()
#print(user[0].email)

#Дістати конкретні данні
#user = User.objects.get(id=1)
#print(user)

# Видалення обє'кту
#not_needed_user = User.objects.get(id=1)
#not_needed_user.delete()

# Редагування об'єкту
#user_to_update = User.objects.get(id=2)
#user_to_update.name = "First"
#user_to_update.bio = "Hello World"
#user_to_update.email = "test@gmail.com"
#user_to_update.save()

#
#new_category = Category(name = "Fruits")
#new_category.save()
#
#new_product = Product(name = "apple", 
#                      price = 50, 
#                      description = "apple",
#                      category = new_category
#).save()

#product = Product.objects.filter(id=1).first()
#print(product.category.name)

#category = Category.objects.get(id=2)
#print(category.products.all())

# Додавання курсу студенту
#student = Student.objects.get(id=1)
#course = Course.objects.get(id=1)
#student.courses.add(course)

student = Student.objects.get(id=1)
print(student.courses.all())
