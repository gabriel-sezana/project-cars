from django.contrib import admin
from cars.models import Car


class CarAdmin(admin.ModelAdmin): #classe pronta do django
    list_display = ('model','brand','factory_year','model_year','value')
    #lista de campos que vai aaparecer la na tabela do admin
    search_fields = ('model', 'brand') #na busca vai poder pesquisar pelo model do carro


admin.site.register(Car,CarAdmin)