from django.contrib import admin

from .models import Category, Image, Product, Rating, RatingAnswer, Order

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(RatingAnswer)
admin.site.register(Order)
