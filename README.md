# Django Car Management System

Sistema de cadastro de carros com Django Admin.

## Tecnologias
- Django + Django ORM
- Pillow (imagens)
- SQLite

## Models

```python
class Brand(models.Model):
    name = models.CharField(max_length=200)

class Car(models.Model):
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.model
```

## Admin Configuration

```python
class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value')
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
```

## Setup

### 1. Instalação
```bash
pip install django pillow
```

### 2. Configuração (settings.py)
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

### 3. URLs (urls.py)
```python
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 4. Migrações
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Comandos Essenciais

```bash
# Migrações (após mudanças nos models)
python manage.py makemigrations && python manage.py migrate

# Servidor
python manage.py runserver

# Admin: http://127.0.0.1:8000/admin/
```
