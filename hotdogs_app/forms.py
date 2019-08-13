from django import forms
from .models import Hotdog

class HotdogForm(forms.ModelForm):# The same functional as above but has more flexibility and has his own save method that better than mine
	class Meta:#bounding Form to Model
		model = Hotdog
		fields = ['title','description','image']
		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),#the same functional as above
			'slug':forms.TextInput(attrs={'class':'form-control'}),
			

		}