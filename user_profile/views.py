from django.shortcuts import redirect,get_object_or_404
from .forms import registration,update_form
from django.contrib.auth.models import User
from django.views.generic import CreateView,TemplateView,UpdateView
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import purchase
from product.models import car
from django.contrib.auth.decorators import login_required
# Create your views here.

#register user
class register(CreateView):
    model=User
    form_class=registration
    template_name='form.html'
    success_url=reverse_lazy('login')
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Registration "
        return context
    
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request,"Account Created Successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Something Went Wrong")
        return self.render_to_response(self.get_context_data(form=form))

#user login 
class login(LoginView):
    template_name='form.html'
    success_url=reverse_lazy('home')
    def get_success_url(self):
        return self.success_url
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context
    
    def form_valid(self, form):
        messages.success(self.request,"Logged in Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,"Something Went Wrong")
        return super().form_invalid(form)

#logout user
def logout(request):
    auth.logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('login')
    
#view profile
class profile(LoginRequiredMixin,TemplateView):
    template_name='profile.html'
    login_url='/login/'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["user"] =self.request.user
        context['products']=purchase.objects.filter(user=self.request.user)
        context['count']=purchase.objects.filter(user=self.request.user).count()
        return context
    
#edit user profile
class edit_profile(LoginRequiredMixin,UpdateView):
    model=User
    form_class=update_form
    template_name='form.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('profile')
    login_url='/login/'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Update Profile"
        return context
    def form_valid(self,form):
        messages.success(self.request,"Profile Updated Successfully")
        return super().form_valid(form)

  #change user password  
class change_pass(LoginRequiredMixin,PasswordChangeView):
    template_name='form.html'
    success_url = reverse_lazy('profile')
    login_url='/login/'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Password Change"
        return context
    def form_valid(self,form):
        messages.success(self.request,"Password Updated Done")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Something Went Wrong")
        return super().form_invalid(form)
    
#buy product 
@login_required(login_url='/login/')
def buy_now(request,pk):
    product=get_object_or_404(car,pk=pk)
    product.quantity-=1
    product.save()
    purchase.objects.create(user=request.user,product=product)
    messages.success(request,"Thank You For Purchase!")
    return redirect('profile')