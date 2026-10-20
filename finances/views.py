from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm # Ensure forms.py exists with TransactionForm
import datetime

# -----------------------------------------------------------------------------

@login_required
def dashboard(request):
    """
    Displays the user's dashboard with transaction history and summaries.
    """
    # Order by date descending to show the latest transactions first
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')

    # Calculate summary statistics for the current month
    today = datetime.date.today()
    current_month = today.month
    current_year = today.year
    
    # Define the common filter for monthly summaries
    monthly_filter = {
        'user': request.user, 
        'date__year': current_year, 
        'date__month': current_month
    }
    
    # Calculate Monthly Income
    monthly_income = Transaction.objects.filter(
        transaction_type='INCOME', 
        **monthly_filter
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate Monthly Expenses
    monthly_expenses = Transaction.objects.filter(
        transaction_type='EXPENSE', 
        **monthly_filter
    ).aggregate(Sum('amount'))['amount__sum'] or 0
    
    context = {
        'transactions': transactions,
        'monthly_income': monthly_income,
        'monthly_expenses': monthly_expenses,
        # Calculate the net balance for the month
        'balance': monthly_income - monthly_expenses,
    }
    # Using 'finances/dashboard.html' path for consistency
    return render(request, 'finances/dashboard.html', context)

# -----------------------------------------------------------------------------

@login_required
def add_transaction(request):
    """
    Handles displaying the transaction form and saving the new transaction data,
    attaching the logged-in user to the object.
    """
    if request.method == 'POST':
        form = TransactionForm(request.POST) 

        if form.is_valid():
            # 1. Temporarily save the form data without hitting the database
            transaction = form.save(commit=False) 
            
            # 2. Assign the currently logged-in user to the transaction object
            transaction.user = request.user 
            
            # 3. Save the object to the database
            transaction.save() 
            
            return redirect('dashboard') 
        
    else:
        # For GET requests, create a blank form
        form = TransactionForm() 

    # Using 'finances/add_transaction.html' path for consistency
    return render(request, 'finances/add_transaction.html', {'form': form})

# -----------------------------------------------------------------------------

@login_required
def edit_transaction(request, transaction_id):
    """
    Handles editing an existing transaction.
    """
    # Fetch the transaction, ensuring it belongs to the current user
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == 'POST':
        # Pass the POST data AND the existing instance for update
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            # form.save() updates the existing 'transaction' instance
            form.save()
            return redirect('dashboard')
    else:
        # For GET, populate the form with the existing instance data
        form = TransactionForm(instance=transaction)
    
    # Using 'finances/edit_transaction.html' path for consistency
    return render(request, 'finances/edit_transaction.html', {'form': form, 'transaction_id': transaction_id})

# -----------------------------------------------------------------------------

@login_required
def delete_transaction(request, transaction_id):
    """
    Handles deleting an existing transaction.
    """
    # Fetch the transaction, ensuring it belongs to the current user
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == 'POST':
        # transaction.delete() performs the database deletion
        transaction.delete()
        return redirect('dashboard')
        
    # Using 'finances/delete_transaction.html' path for consistency
    return render(request, 'finances/delete_transaction.html', {'transaction': transaction})



