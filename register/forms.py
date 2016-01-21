from django import forms
from register.models import User


class CategoryForm(forms.ModelForm):
    salutation = forms.CharField(max_length=20, help_text="Salutation", required=True)
    first_name = forms.CharField(max_length=40, help_text="First Name", required=True)
    last_name = forms.CharField(max_length=40, help_text="Last Name", required=True)
    organisation = forms.CharField(max_length=100, help_text="Organisation", required=True)
    address = forms.CharField(max_length=100, help_text="Address", required=True)
    city = forms.CharField(max_length=40, help_text="City", required=True)
    postcode = forms.CharField(max_length=10, help_text="Postcode", required=True)
    country = forms.CharField(max_length=60, help_text="Country", required=True)
    telephone = forms.CharField(max_length=15, help_text="Telephone", required=True)
    email = forms.EmailField(max_length=60, help_text="Email Address", required=True)
    #feeNormal = forms.CharField(max_length=60, help_text="I wish to register for the conference at the normal price of " +
     #                                                    chr(156) + "450", required=True)

    class Meta:
        model = User
        fields = ('salutation', 'first_name', 'last_name', 'organisation', 'address', 'city', 'postcode', 'country',
                  'telephone', 'email')
