from django.contrib import admin
from cars.models import Car
from cars.models import Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin): #classe pronta do django
    list_display = ('model','brand','factory_year','model_year','value')
    #lista de campos que vai aaparecer la na tabela do admin
    search_fields = ('model', 'brand') #na busca vai poder pesquisar pelo model do carro


admin.site.register(Car,CarAdmin)
admin.site.register(Brand,BrandAdmin)