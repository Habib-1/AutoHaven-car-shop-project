from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,CreateView
from . import models
from .import forms
from django.urls import reverse
# Create your views here.

#simple render home page with all brand and all car
def home(request):
    brand=models.brand.objects.all()
    car=models.car.objects.all()
    count=models.car.objects.count()
    return render(request,'home.html',{'brands':brand, 'cars':car,'count':count})
 
#Brand Category wised View
def shop(request,slug=None):
    brand=models.brand.objects.all()
    
    if slug is not None:
        brand_name=models.brand.objects.get(slug=slug)
        car=models.car.objects.filter(brand=brand_name)
        count=models.car.objects.filter(brand=brand_name).count()
    else:
        car=models.car.objects.all()
        count=models.car.objects.count()
    return render(request,'shop.html',{'brands':brand, 'cars':car,'count':count})

#on click show delails , Details information
class product_details(DetailView):
    model =models.car
    template_name = "car_details.html"
    context_object_name='car'
   
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["comments"] =models.Comments.objects.filter(car=self.object)
        context["count"] =models.Comments.objects.filter(car=self.object).count()
        return context

#add Comments on any perticular car 
class add_comment(CreateView):
    model=models.Comments
    form_class=forms.comment_form
    template_name='comment.html'
   #comments er car fields e instance je car odject e achi oita assign kora
    def form_valid(self, form):
        car=get_object_or_404(models.car,id=self.kwargs['pk'])
        form.instance.car=car
        return super().form_valid(form)
    #kon object er details page e redirect hobe pk diye bole deoya
    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.kwargs['pk']})