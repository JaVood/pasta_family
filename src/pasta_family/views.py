from core.views import BaseView
from django.shortcuts import render
from .models import Product, ProductGroup, Review, Price, CooperationForm as Forms, CooperationType, MainPhoto, AboutCompanyPhoto
from .forms import CooperationForm, ReviewNewForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from cart.forms import CartAddProductForm
from cart.cart import Cart
from orders.models import Order


class IndexView(BaseView):
    template_name = 'pasta_family/index.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.all()

        cart = Cart(request)

        main_photo = MainPhoto.objects.get(active=True, ru_version=False)

        context.update({
            'tops': Review.objects.all()[:3],
            'reviews': Review.objects.all()[3:],
            'products': products,
            'cart': cart,
            'main_photo': main_photo
        })
        return self.render_to_response(context)


class AboutView(BaseView):
    template_name = 'pasta_family/about.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        about_photo = AboutCompanyPhoto.objects.get(active=True)
        context.update({
            'cart': cart,
            'photo': about_photo,
        })
        return self.render_to_response(context)


class OfertView(BaseView):
    template_name = 'pasta_family/ofert.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class OfertRuView(BaseView):
    template_name = 'pasta_family/ofert_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class ReturnView(BaseView):
    template_name = 'pasta_family/return.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class ReturnRuView(BaseView):
    template_name = 'pasta_family/return_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class DeliveryView(BaseView):
    template_name = 'pasta_family/delivery.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class SportView(BaseView):
    template_name = 'pasta_family/for_sportmens.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class ContactView(BaseView):
    template_name = 'pasta_family/contacts.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


def cooperation_new(request):
    cart = Cart(request)
    price1 = Price.objects.filter(first_price=True)
    price2 = Price.objects.filter(first_price=False)
    types = CooperationType.objects.all()
    forms = Forms.objects.all()
    if request.method == "POST":
        form = CooperationForm(request.POST)
        if form.is_valid():
            cooperation = form.save(commit=False)
            cooperation.save()
            return redirect('/form_send/')
    else:
        form = CooperationForm()
    return render(request, 'pasta_family/cooperation.html', {'form': form, 'cart': cart,
                                                             'price1': price1,
                                                             'price2': price2,
                                                             'types': types,
                                                             'forms': forms,
                                                             })


def product_group(request):
    cart = Cart(request)
    product_group_list = ProductGroup.objects.all()
    return render(request, 'pasta_family/product_group.html', {'categories': product_group_list,
                                                               'cart': cart,
                                                               })


class FormSendView(BaseView):
    template_name = 'pasta_family/form_send.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


def review_new(request):
    cart = Cart(request)
    products = Product.objects.all()
    if request.method == "POST":
        form = ReviewNewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('/form_send/')
    else:
        form = ReviewNewForm()
    return render(request, 'pasta_family/review.html', {'form': form, 'cart': cart, 'products': products,})


class ProductsView(BaseView):
    template_name = 'pasta_family/products.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        group = ProductGroup.objects.get(slug=kwargs.get('productgroup_slug'))

        product_list = Product.objects.filter(product_group_id=group.id).order_by('-id')

        cart = Cart(request)

       	context.update({
            'products': product_list,
            'product_group': group,
            'cart': cart,
        })
        return self.render_to_response(context)


class ProductView(BaseView):
    template_name = 'pasta_family/product.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        group = ProductGroup.objects.get(slug=kwargs.get('productgroup_slug'))

        product = get_object_or_404(Product, slug=kwargs.get('product_slug'))

        products = Product.objects.filter(product_group_id=group.id)

        product_weights = Product.objects.filter(product_type_id=product.product_type_id)

        product_types = Product.objects.filter(main_product=True)

        cart_product_form = CartAddProductForm()

        cart = Cart(request)

        context.update({
            'product': product,
            'products': products,
            'product_group': group,
            'product_weights': product_weights,
            'product_types': product_types,
            'cart_product_form': cart_product_form,
            'cart': cart,
        })
        return self.render_to_response(context)


class IndexRuView(BaseView):
    template_name = 'pasta_family/index_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        products = Product.objects.all()

        cart = Cart(request)

        main_photo = MainPhoto.objects.get(active=True, ru_version=True)

        context.update({
            'tops': Review.objects.all()[:3],
            'reviews': Review.objects.all()[3:],
            'products': products,
            'cart': cart,
            'main_photo': main_photo
        })
        return self.render_to_response(context)


class AboutRuView(BaseView):
    template_name = 'pasta_family/about_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        about_photo = AboutCompanyPhoto.objects.get(active=True)
        context.update({
            'cart': cart,
            'photo': about_photo,
        })
        return self.render_to_response(context)


class DeliveryRuView(BaseView):
    template_name = 'pasta_family/delivery_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class SportRuView(BaseView):
    template_name = 'pasta_family/for_sportmens_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


class ContactRuView(BaseView):
    template_name = 'pasta_family/contacts_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


def cooperation_new_ru(request):
    cart = Cart(request)
    price1 = Price.objects.filter(first_price=True)
    price2 = Price.objects.filter(first_price=False)
    types = CooperationType.objects.all()
    forms = Forms.objects.all()
    if request.method == "POST":
        form = CooperationForm(request.POST)
        if form.is_valid():
            cooperation = form.save(commit=False)
            cooperation.save()
            return redirect('/form_send/')
    else:
        form = CooperationForm()
    return render(request, 'pasta_family/cooperation_ru.html', {'form': form, 'cart': cart,
                                                                'price1': price1,
                                                                'price2': price2,
                                                                'types': types,
                                                                'forms': forms,
                                                                })


def product_group_ru(request):
    cart = Cart(request)
    product_group_list = ProductGroup.objects.all()
    return render(request, 'pasta_family/product_group_ru.html', {'categories': product_group_list,
                                                                  'cart': cart,
                                                                  })


class FormSendRuView(BaseView):
    template_name = 'pasta_family/form_send_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(request)
        context.update({
            'cart': cart,
        })
        return self.render_to_response(context)


def review_new_ru(request):
    cart = Cart(request)
    products = Product.objects.all()
    if request.method == "POST":
        form = ReviewNewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('/ru/form_send/')
    else:
        form = ReviewNewForm()
    return render(request, 'pasta_family/review_ru.html', {'form': form, 'cart': cart, 'products': products,})


class ProductsRuView(BaseView):
    template_name = 'pasta_family/products_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        group = ProductGroup.objects.get(slug=kwargs.get('productgroup_slug'))

        product_list = Product.objects.filter(product_group_id=group.id).order_by('-id')

        cart = Cart(request)

        context.update({
            'products': product_list,
            'product_group': group,
            'cart': cart,
        })
        return self.render_to_response(context)


class ProductRuView(BaseView):
    template_name = 'pasta_family/product_ru.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        group = ProductGroup.objects.get(slug=kwargs.get('productgroup_slug'))

        product = get_object_or_404(Product, slug=kwargs.get('product_slug'))

        products = Product.objects.filter(product_group_id=group.id)

        product_weights = Product.objects.filter(product_type_id=product.product_type_id)

        product_types = Product.objects.filter(main_product=True)

        cart_product_form = CartAddProductForm()

        cart = Cart(request)

        context.update({
            'product': product,
            'products': products,
            'product_group': group,
            'product_weights': product_weights,
            'product_types': product_types,
            'cart_product_form': cart_product_form,
            'cart': cart,
        })
        return self.render_to_response(context)


def order_check(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_id = request.POST.get("id","")
        return order_detail(request, order=order_id)
    return render(request, 'pasta_family/order_check.html', {'cart': cart})


def order_detail(request, order):
    cart = Cart(request)
    try:
        id = Order.objects.get(id=order)
    except Order.DoesNotExist:
        id = None
    return render(request, 'pasta_family/order_detail.html', {'cart': cart, 'order': id})


def order_check_ru(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_id = request.POST.get("id","")
        return order_detail_ru(request, order=order_id)
    return render(request, 'pasta_family/order_check_ru.html', {'cart': cart})


def order_detail_ru(request, order):
    cart = Cart(request)
    try:
        id = Order.objects.get(id=order)
    except Order.DoesNotExist:
        id = None
    return render(request, 'pasta_family/order_detail_ru.html', {'cart': cart, 'order': id})

