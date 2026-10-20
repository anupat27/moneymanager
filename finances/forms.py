from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction

class TransactionForm(forms.ModelForm):
    """
    A form for creating and updating Transaction objects with custom validation.
    """
    class Meta:
        model = Transaction
        fields = ['amount', 'transaction_type', 'category', 'date', 'description']
        widgets = {
            # Use 'date' type for better browser date picker support
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_amount(self):
        """
        Ensures the transaction amount is a positive value.
        """
        # Retrieve the cleaned amount data
        amount = self.cleaned_data.get('amount')
        
        # Check if the amount is provided and is less than or equal to zero
        if amount is not None and amount <= 0:
            # Raise a validation error if the condition is met
            raise ValidationError("The amount must be a positive value greater than zero.")
            
        # Always return the cleaned data, whether valid or not
        return amount
