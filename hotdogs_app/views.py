from django.shortcuts import render,get_object_or_404,redirect
from .models import Hotdog
from django.views.generic import View
from .forms import HotdogForm

# Create your views here.
def hotdogs_list(request):
	hot_dogs = Hotdog.objects.all()
	context = {'hot_dogs':hot_dogs}
	return render(request,'hotdogs_app/hotdogs_list.html',context=context)

class hotdog_detail(View):
	def get(self,request,id):
		hotdog = get_object_or_404(Hotdog,id__iexact=id)
		return render(request,'hotdogs_app/hotdog_detail.html',context={'hotdog':hotdog})	

# class hotdog_create(View):
# 	def get(self,request):
# 		form = HotdogForm()
# 		return render(request,'hotdogs_app/hotdog_create.html',context={'form':form})
# 	def post(self,request):
# 		bound_form = HotdogForm(request.POST)
# 		if bound_form.is_valid():
# 			new_hotdog = bound_form.save()
# 			return redirect(new_hotdog)
# 		return render(request, 'hotdogs_app/hotdog_create.html',context={'form':bound_form})

def hotdog_create(request):
    if request.method == 'POST':
        form =HotdogForm(request.POST, request.FILES)
        if form.is_valid():
            new_hotdog=form.save()
            return redirect(new_hotdog)
    else:
        form = HotdogForm()
    return render(request, 'hotdogs_app/hotdog_create.html', {
        'form': form
    })

class hotdog_update(View):
	def get(self,request,id):
		hotdog = Hotdog.objects.get(id__iexact=id)
		bound_form = HotdogForm(instance=hotdog)#TagForm can apply Tag object as instance param
		return render(request,'hotdogs_app/hotdog_update.html',context={'form':bound_form,'hotdog':hotdog})

	def post(self,request,id):
		hotdog = Hotdog.objects.get(id__iexact=id)
		bound_form = HotdogForm(request.POST,request.FILES,instance=hotdog)

		if bound_form.is_valid():
			new_hotdog = bound_form.save()
			return redirect(new_hotdog)
		return render(request,'hotdogs_app/hotdog_update.html',context={'form':bound_form,'tag':hotdog})


class hotdog_delete(View):
	def get(self,request,id):
		hotdog = get_object_or_404(Hotdog,id__iexact=id)
		return render(request,'hotdogs_app/hotdog_delete.html',context={'hotdog':hotdog})
	def post(self,request,id):
		hotdog = get_object_or_404(Hotdog,id__iexact=id)
		hotdog.delete()
		return redirect('hot_dogs_list')

# def hotdog_delete(request,id):
# 	# if request.method == 'POST':
# 	# 	hotdog = get_object_or_404(Hotdog,id__iexact=id)
# 	# 	hotdog.delete()
# 	hotdog = get_object_or_404(Hotdog,id__iexact=id)
# 	context = {'hotdog':hotdog}
# 	return render(request,'hotdogs_app/hotdog_delete.html',context=context)


		