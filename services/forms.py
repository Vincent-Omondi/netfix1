# services/forms.py


from django import forms
from users.models import Company
from .models import Service

class CreateNewService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price_hour', 'field']

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super(CreateNewService, self).__init__(*args, **kwargs)

        # adding placeholders to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'
        self.fields['name'].widget.attrs['autocomplete'] = 'off'

        # Set choices for the 'field' based on the company's selected service
        if company:
            if company.field == 'All in One':
                # If 'All in One', show all choices
                self.fields['field'].choices = Service._meta.get_field('field').choices
            else:
                # Otherwise, only show the company's selected service
                self.fields['field'].choices = [(company.field, company.field)]