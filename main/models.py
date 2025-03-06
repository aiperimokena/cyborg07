from django.contrib.auth import get_user_model
from tkinter.constants import CASCADE

from django.db import models
from django.db.models import PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()

class Category(models.Model):
    title = models.CharField(
        max_length=123,
        verbose_name='Title')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title




class Image(models.Model):
    file = models.ImageField(
        upload_to='media/image_file',
        verbose_name='File')

    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def __str__(self):
        return str(self.file)

#TODO: create user
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='Product')

    title = models.CharField(
        max_length=123,
        verbose_name='Title'
    )
    main_image = models.ImageField(
        upload_to='medai/main_image',
        verbose_name='Main photo',
        help_text= ' Picture that will be the cover page no webcite'
    )
    images = models.ManyToManyField(
        Image,
        verbose_name='Image')

    description = models.TextField(
        verbose_name='Description')

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Price'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Active'
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Quantity'
    )


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

#TODO create user
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    count = models.PositiveSmallIntegerField(
       validators=[MinValueValidator(1), MaxValueValidator(5)] ,
       verbose_name='Rate'
    )

    comment = models.TextField(
        verbose_name='Comment',
        max_length=200
    )

    created_at = models.DateTimeField(
        verbose_name='Created date',
        auto_now_add=True
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

   #TODO: create user
class RatingAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
        verbose_name='Rating reply'
    )
    comment = models.TextField(
        verbose_name='Comment',
        max_length=200
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date created'
    )

    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Date change'
    )

    time_limit = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Time limit'
    )

    class Meta:
        verbose_name = 'Reply to the comment'
        verbose_name_plural = 'Replies to the comments'

    # def __str__

class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name='Order'
    )

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Created at')

    title = models.TextField(
        verbose_name='Text'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    def __str__(self):
        return self.title

