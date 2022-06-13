
from django.views.generic import CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import RegisterUserForm, AuthenticationUserForm, UpdateProfileForm
from .models import UserProfiles
from django.contrib.auth.models import User
from .service import export_to_csv, ai


class RegisterUser(CreateView):
    """Класс регистрации пользователя"""
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def user_login(request):
    """Метод аутентификации пользователя"""
    if request.method == 'POST':
        form = AuthenticationUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationUserForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    """Метод выхода пользователя из профиля"""
    logout(request)
    return redirect('login')


class UsersProfileCreateView(CreateView):
    """Класс создания профиля пользователя"""
    model = UserProfiles
    form_class = UpdateProfileForm
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            export_to_csv(request.user, form)
            return HttpResponseRedirect(reverse_lazy('main'))
        else:
            return render(request, 'profile.html', {'form': form})

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)
    

class UsersProfileDetailView(View):
    """Класс показа основной страницы"""
    model = UserProfiles
    template_name = 'main_page.html'

    def get(self, request):
        try:
            users = User.objects.get(username=self.request.user)
            try:
                profile = UserProfiles.objects.get(user=self.request.user)
                return render(request, 'main_page.html', {'objects': users, 'profile':profile})
            except:
                return render(request, 'main_page.html', {'objects': users})
        except:
            return redirect('login')


class UsersProfileUpdateView(UpdateView):
    """Класс обновления профиля пользователя"""
    model = UserProfiles
    form_class = UpdateProfileForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('main')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        super().post(request, *args, **kwargs)
        export_to_csv(request.user, self.object)
        return HttpResponseRedirect(reverse_lazy('main'))


    def get_object(self):
        return UserProfiles.objects.get(user=self.request.user)


def StartPrediction(request):
    """Функци вызова ИИ"""
    print(request.user)
    aui = ai()
    print(aui)
    try:
        users = UserProfiles.objects.get(user=request.user)
        profile = UserProfiles.objects.get(user=request.user)
        
        return render(request, 'main_page.html', {'objects': users,'profile':profile, 'ai': aui})
    except:
        return redirect('login')