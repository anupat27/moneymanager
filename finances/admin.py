from django.contrib import admin
from .models import Transaction

# Register your models here.
admin.site.register(Transaction)

# Optional: You can create a custom Admin class to improve display
# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('date', 'amount', 'transaction_type', 'user', 'category')
#     list_filter = ('transaction_type', 'category', 'date')
#     search_fields = ('description', 'user__username')
    
# admin.site.register(Transaction, TransactionAdmin)

