from django.contrib import admin
from .models import Dog, Feeding, Toy

# Dog Admin
@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age')

# Feeding Admin
@admin.register(Feeding)
class FeedingAdmin(admin.ModelAdmin):
    list_display = ('dog', 'date', 'meal')

# Toy Admin
@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

# # Register models with custom admin
# admin.site.register(Dog, DogAdmin)
# admin.site.register(Feeding, FeedingAdmin)
# admin.site.register(Toy, ToyAdmin)