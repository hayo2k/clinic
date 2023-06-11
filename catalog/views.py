from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import *
from .models import *
from .utils import *
from users.models import User
from django.shortcuts import HttpResponseRedirect, render, redirect


class UsersHome(DataMixin, ListView):
    model = Users
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Панель управления')
        return dict(list(context.items()) + list(c_def.items()))


class UsersAbout(DataMixin, ListView):
    model = Users
    template_name = 'catalog/about.html'
    context_object_name = 'forms'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Специалисты')
        return dict(list(context.items()) + list(c_def.items()))


class AddUser(DataMixin, CreateView):
    form_class = AddUserForm
    template_name = 'catalog/add_user.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Специалисты')
        return dict(list(context.items()) + list(c_def.items()))


class AnalysisListView(DataMixin, ListView):
    model = Product
    template_name = 'catalog/analysis.html'
    paginate_by = 3
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(AnalysisListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnalysisListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        c_def = self.get_user_context(title='Анализы')
        return dict(list(context.items()) + list(c_def.items()))

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def add_user(request):
#     if request.method == 'POST':
#         form = AddUserForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('index')
#             except:
#                 form.add_error(None, 'Ошибка добавления пользователя')
#     else:
#         form = AddUserForm()
#     return render(request, 'catalog/add_user.html', {'form': form})











