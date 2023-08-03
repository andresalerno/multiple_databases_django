from django.contrib import admin

from .models import Green

class GreenAdmin(admin.ModelAdmin):
    using = 'green'
    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)
    def delete_model(self, request, obj):
        obj.delete(using=self.using)

admin.site.register(Green)