from django import forms



class Buy(forms.Form):

    def __init__(self,*args,**kwargs):
        quantity_m = kwargs.pop("quantity_m")
        PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range (1,quantity_m+1)]
        super(Buy, self).__init__(*args,**kwargs)
        self.fields['quantity'] = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)