from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


class User(AbstractUser):
    username = models.CharField(
        max_length=64,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_('Username'),
    )

    first_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('First Name'),
    )

    last_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Last Name'),
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list

    email = models.EmailField(max_length=70,)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Product(models.Model):
    availability = models.BooleanField(verbose_name='Availability', default=False)
    name_ru = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Product In Russian'),
    )

    name_en = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Product In English'),
    )

    name_ua = models.CharField(
        max_length=64,
        verbose_name=_('Product In Ukraine'),
    )

    slug = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        verbose_name=_('Slug'),
        help_text="Don't touch it!"
    )

    description_ru = models.CharField(
        max_length=1000,
        verbose_name=_('Description In Russian'),
        blank=True,
    )

    description_en = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name=_('Description In English')
    )

    description_ua = models.CharField(
        max_length=1000,
        verbose_name=_('Description In Ukraine'),
        blank=True,
    )

    product_group = models.ForeignKey(
        to='ProductGroup',
        related_name='products',
        on_delete=models.PROTECT,
        verbose_name=_('Group'),
        blank=False
    )

    product_type = models.ForeignKey(
        to='ProductType',
        related_name='products',
        on_delete=models.PROTECT,
        verbose_name=_('Type'),
        blank=False
    )

    old_price = models.IntegerField(verbose_name=_('Old Price'), blank=True, null=True)

    price = models.IntegerField(verbose_name=_('Price'))

    weight = models.ForeignKey(
        to='ProductWeight',
        related_name='products',
        on_delete=models.PROTECT,
        verbose_name=_('Weight'),
        blank=False
    )

    ingredients_ru = models.CharField(
        max_length=512,
        verbose_name=_('Ingredients In Russian'),
        blank=True,
    )

    ingredients_ua = models.CharField(
        max_length=512,
        verbose_name=_('Ingredients In Ukraine'),
        blank=True,
    )

    ingredients_en = models.CharField(
        max_length=512,
        verbose_name=_('Ingredients In English'),
        blank=True,
    )

    main_product = models.BooleanField(default=False, verbose_name=_('Main'))

    image_main = models.ImageField(verbose_name=_('Image Main'))

    image_2 = models.ImageField(verbose_name=_('Image 2'))

    image_3 = models.ImageField(verbose_name=_('Image 3'), blank=True, null=True)

    def __str__(self):
        return self.name_ru


class ProductGroup(models.Model):
    name_ru = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Group In Russian'),
    )

    name_en = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Group In English'),
    )

    name_ua = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Group In Ukraine'),
    )

    slug = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        verbose_name=_('Slug'),
        help_text="Don't touch it!"
    )

    image = models.ImageField(verbose_name=_('Image'))

    image_ru = models.ImageField(verbose_name=_('Image Ru'), blank=True, null=True)

    def __str__(self):
        return self.name_ru


class Cooperation(models.Model):
    created = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Created at'),
        null=True
    )

    name = models.CharField(
        max_length=64,
        verbose_name=_('Name'),
    )

    email = models.EmailField(
        max_length=70,
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'")

    phone = models.CharField(validators=[phone_regex], max_length=17)

    type = models.ForeignKey(
        to='CooperationType',
        on_delete=models.PROTECT,
        verbose_name=_('Type'),
        blank=False,
    )

    form = models.ForeignKey(
        to='CooperationForm',
        on_delete=models.PROTECT,
        verbose_name=_('Form'),
        blank=False,
    )

    def __str__(self):
        return self.name


class CooperationType(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name


class CooperationForm(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name


class ReviewNew(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=_('Name'),
    )

    description = models.CharField(
        max_length=200,
        verbose_name=_('Description')
    )

    RATING_NUMBER = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )

    rating = models.IntegerField(choices=RATING_NUMBER, default='5')

    check_by_moderator = models.BooleanField(default=False)

    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        blank=False,
    )

    def save(self, *args, **kwargs):
        if self.check_by_moderator == True:
            review = Review.objects.create(name=self.name,
                                           description=self.description,
                                           rating=self.rating,
                                           product=self.product,
                                           )
            review.save()
            self.delete()
        else:
            super(ReviewNew, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name=_('Name'),
    )

    description = models.CharField(
        max_length=200,
        verbose_name=_('Description')
    )

    RATING_NUMBER = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )

    rating = models.IntegerField(choices=RATING_NUMBER, default='5')

    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        blank=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
        null=True
    )
    def __str__(self):
        return self.name


class ProductType(models.Model):
    name_ru = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Name In Russian'),
    )

    name_en = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Name In English'),
    )

    name_ua = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Name In Ukraine'),
    )

    slug = models.CharField(
        max_length=150,
        unique=True,
        blank=True,

        verbose_name=_('Slug'),
        help_text="Don't touch it!"
    )

    group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.PROTECT,
        verbose_name=_('group'),
        blank=False,
    )

    def __str__(self):
        return self.name_ru


class ProductWeight(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Name'),
    )

    weight = models.IntegerField(verbose_name=_('Weight'))

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Name'),
    )

    price = models.FileField(
        verbose_name=_('File')
    )

    first_price = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MainPhoto(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    photo = models.ImageField(verbose_name="Photo")
    active = models.BooleanField(verbose_name="Active", default=False)
    ru_version = models.BooleanField(verbose_name="Ru version", default=False)

    def __str__(self):
        return self.name


class AboutCompanyPhoto(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    photo_one = models.ImageField(verbose_name="Photo One", blank=True, null=True)
    photo_two = models.ImageField(verbose_name="Photo One", blank=True, null=True)
    active = models.BooleanField(verbose_name="Active", default=False)

    def __str__(self):
        return self.name
