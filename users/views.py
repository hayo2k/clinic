from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponseRedirect

from catalog.models import Basket, Product
from users.models import User

from catalog.utils import DataMixin, menu
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from users.forms import SignUpUserForm, LoginUserForm, UserProfileForm


class RegisterUser(DataMixin, CreateView):
    model = User
    form_class = SignUpUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


# class ProfileUser(DataMixin, UpdateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'users/profile.html'
#     title = 'Профиль'
#     context = {'baskets': Basket.objects.all(),}
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Профиль')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('users:profile', args=(self.object.id,))

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)

    context = {
        'title': 'Профиль',
        'form': form,
        'baskets': baskets,
        'menu': menu,
        'total_sum': total_sum,
        'total_quantity': total_quantity,

    }
    return render(request, 'users/profile.html', context)