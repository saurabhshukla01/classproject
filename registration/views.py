from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from .forms import userform
from django.contrib.auth import authenticate, login,logout

class Register(View):
    form_class = userform
    initial = {'key': 'value'}
    template_name = 'registration/register_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, self.template_name, {'form': form})

class LoginUser(View):
    template_name = 'registration/login_form.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('/myapp/addrestaurant/')
        else:
            return render(request, self.template_name,{'error':"Username or password is Incorrect."})
        