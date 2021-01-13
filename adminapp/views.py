from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# Users

class UserCreateView(CreateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("adminapp:users")
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     if request.method == "POST":
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse("admin:users"))
#
#     user_form = ShopUserRegisterForm()
#     content = {
#         "update_form": user_form
#     }
#     return render(request, "adminapp/user_update.html", content)


class UsersListView(ListView):
    model = ShopUser
    template_name = "adminapp/users.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def users(requset):
#     users_list = ShopUser.objects.all().order_by("-is_active")
#     content = {
#         "objects": users_list,
#     }
#     return render(requset, "adminapp/users.html", content)

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy("adminapp:users")
    form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Категории и редактирование"
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == "POST":
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse("admin:user_update", args=[edit_user.pk]))
#     edit_form = ShopUserAdminEditForm(instance=edit_user)
#     content = {
#         "update_form": edit_form
#     }
#     return render(request, "adminapp/user_update.html", content)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = "adminapp/user_delete.html"
    success_url = reverse_lazy("adminapp:users")
    form_class = ShopUserAdminEditForm

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category_pk = self.kwargs["pk"]
        category_item = get_object_or_404(Product, pk=category_pk)
        context_data["category"] = category_item
        return context_data

# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     user_item = get_object_or_404(ShopUser, pk=pk)
#     if request.method == "POST":
#         if user_item.is_active:
#             user_item.is_active = False
#         else:
#             user_item.is_active = True
#         user_item.save()
#         return HttpResponseRedirect(reverse("admin:users"))
#     content = {
#         "user_to_delete": user_item
#     }
#     return render(request, "adminapp/user_delete.html", content)


# Category

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("adminapp:categories")
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     if request.method == "POST":
#         category_form = ProductCategoryEditForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse("admin:categories"))
#
#     category_form = ProductCategoryEditForm()
#     content = {
#         "update_form": category_form
#     }
#     return render(request, "adminapp/category_update.html", content)


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "adminapp/categories.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


@user_passes_test(lambda u: u.is_superuser)
def categories(requset):
    categories_list = ProductCategory.objects.all().order_by("-is_active")
    content = {
        "objects": categories_list
    }

    return render(requset, "adminapp/categories.html", content)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("adminapp:categories")
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Категории и редактирование"
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == "POST":
#         edit_form = ProductCategoryEditForm(request.POST, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse("admin:categories"))
#     edit_form = ProductCategoryEditForm(instance=edit_category)
#     content = {
#         "update_form": edit_form
#     }
#     return render(request, "adminapp/category_update.html", content)

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy("adminapp:categories")
    form_class = ProductCategoryEditForm

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Категории и редактирование"
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == "POST":
#         if category_item.is_active:
#             category_item.is_active = False
#         else:
#             category_item.is_active = True
#         category_item.save()
#         return HttpResponseRedirect(reverse("admin:categories"))
#     content = {
#         "category_to_delete": category_item
#     }
#     return render(request, "adminapp/category_delete.html", content)


# Products

class ProductCreateView(CreateView):
    model = Product
    template_name = "adminapp/product_update.html"
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_pk = self.kwargs["pk"]
        category_item = get_object_or_404(ProductCategory, pk=category_pk)
        context_data["category"] = category_item
        return context_data

    def get_success_url(self):
        category_pk = self.kwargs["pk"]
        success_url = reverse("adminapp:products", args=[category_pk])
        return success_url


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == "POST":
#         update_form = ProductEditForm(request.POST, request.FILES)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse("admin:product_read", args=[pk]))
#     update_form = ProductEditForm()
#     content = {
#         "update_form": update_form,
#         "category": category_item
#     }
#     return render(request, "adminapp/product_update.html", content)


class ProductListView(ListView):
    model = Product
    template_name = "adminapp/products.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_pk = self.kwargs["pk"]
        return queryset.filter(category__pk=category_pk)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_pk = self.kwargs["pk"]
        category_item = get_object_or_404(ProductCategory, pk=category_pk)
        context_data["category"] = category_item
        return context_data


# @user_passes_test(lambda u: u.is_superuser)
# def products(requset, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     product_list = Product.objects.filter(category=category_item)
#     content = {
#         "object_list": product_list,
#         "category": category_item
#     }
#     return render(requset, "adminapp/products.html/", content)


class ProductDetailView(DetailView):
    model = Product
    template_name = "adminapp/product_read.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(requset, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     content = {
#         "object": product_item
#     }
#
#     return render(requset, "adminapp/product_read.html", content)



class ProductUpdateView(UpdateView):
    model = Product
    template_name = "adminapp/product_update.html"
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        category_pk = self.kwargs["pk"]
        category_item = get_object_or_404(Product, pk=category_pk)
        context_data["category"] = category_item
        return context_data

    def get_success_url(self):
        pk = self.kwargs["pk"]
        product_item = Product.objects.get(pk=pk)
        return reverse("adminapp:products", args=[product_item.category.pk])

# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if request.method == "POST":
#         update_form = ProductEditForm(request.POST, request.FILES, instance=product_item)
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse("admin:product_read", args=[pk]))
#     update_form = ProductEditForm(instance=product_item)
#     content = {
#         "update_form": update_form,
#         "category": product_item
#     }
#     return render(request, "adminapp/product_update.html", content)

class ProdoctDeleteView(DeleteView):
    model = Product
    template_name = "adminapp/product_delete.html"

    def delete(self, *args, **kwargs):
        object = self.get_object()
        if object.is_active:
            object.is_active = False
        else:
            object.is_active = True
        object.save()
        return HttpResponseRedirect(reverse("adminapp:products", args=[object.category_id]))

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if request.method == "POST":
#         if product_item.is_active:
#             product_item.is_active = False
#         else:
#             product_item.is_active = True
#         product_item.save()
#         return HttpResponseRedirect(reverse("admin:products", args=[product_item.category.pk]))
#     content = {
#         "product_to_delete": product_item
#     }
#     return render(request, "adminapp/product_delete.html", content)
