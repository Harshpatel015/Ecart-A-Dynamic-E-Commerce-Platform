from django import forms
from Ecart.models import shipping_address


class shipping_forms_from_model(forms.ModelForm):
    
    class Meta:
        model = shipping_address
        fields = ["Contact_Person_Name","Contact_Person_phone_number","Contact_Person_Email","Street_Address","City","State"]