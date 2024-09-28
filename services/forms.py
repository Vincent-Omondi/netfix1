# services/forms.py
from django import forms
from users.models import Company
from .models import Service, ServiceHistory

class CreateNewService(forms.ModelForm):
    """
    Form for creating a new service.
    """
    class Meta:
        model = Service
        fields = ['name', 'description', 'price_hour', 'field']

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom fields and attributes.

        :param company: Company instance to determine field choices
        """
        company = kwargs.pop('company', None)
        super(CreateNewService, self).__init__(*args, **kwargs)

        # Adding placeholders and attributes to form fields
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter Service Name',
            'autocomplete': 'off'
        })
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        # Set choices for the 'field' based on the company's selected service
        if company:
            if company.field == 'All in One':
                # If 'All in One', show all choices
                self.fields['field'].choices = Service._meta.get_field('field').choices
            else:
                # Otherwise, only show the company's selected service
                self.fields['field'].choices = [(company.field, company.field)]

class RequestServiceForm(forms.ModelForm):
    """
    Form for requesting a service.
    """
    address = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter service address'})
    )
    service_time = forms.IntegerField(
        min_value=1, 
        widget=forms.NumberInput(attrs={'placeholder': 'Enter service time in hours'})
    )

    class Meta:
        model = ServiceHistory
        fields = ['address', 'service_time']

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom attributes if needed.
        """
        super(RequestServiceForm, self).__init__(*args, **kwargs)
