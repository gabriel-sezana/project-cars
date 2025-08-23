# Projeto Django - Sistema de Carros

Sistema de cadastro e gerenciamento de carros desenvolvido em Django com interface administrativa.

## 📋 Funcionalidades

- Cadastro de carros com informações detalhadas
- Sistema de marcas para organização
- Upload e gerenciamento de imagens dos carros
- Interface administrativa completa
- Listagem e busca de carros
- Relacionamento entre carros e marcas

## 🚀 Tecnologias Utilizadas

- **Django** - Framework web Python
- **Django ORM** - Mapeamento objeto-relacional
- **SQLite** - Banco de dados (padrão do Django)
- **Pillow** - Processamento de imagens
- **Django Admin** - Interface administrativa

## 📁 Estrutura do Projeto

```
projeto_carros/
├── cars/
│   ├── models.py          # Modelos Car e Brand
│   ├── admin.py           # Configuração do Django Admin
│   ├── views.py           # Views da aplicação
│   └── ...
├── media/                 # Armazenamento de imagens
├── manage.py
└── settings.py
```

## 🛠️ Configuração e Instalação

### 1. Pré-requisitos

```bash
pip install django
pip install Pillow
```

### 2. Configuração dos Models

#### Model Car (cars/models.py)
```python
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.model
```

#### Model Brand (cars/models.py)
```python
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
```

### 3. Migrações do Banco de Dados

Sempre que alterar os models, execute:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Configuração do Django Admin

#### Registro dos Models (cars/admin.py)
```python
from django.contrib import admin
from .models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
```

### 5. Configuração de Imagens

#### No arquivo settings.py:
```python
import os

# Configuração de idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Configuração de mídia (no final do arquivo)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

#### No arquivo urls.py principal:
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # suas outras URLs aqui
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 📝 Como Usar

### 1. Criar Superusuário
```bash
python manage.py createsuperuser
```

### 2. Executar o Servidor
```bash
python manage.py runserver
```

### 3. Acessar o Admin
- Acesse: `http://127.0.0.1:8000/admin/`
- Faça login com as credenciais do superusuário
- Cadastre marcas em "Brands"
- Cadastre carros em "Cars"

## 🗃️ Funcionalidades do Django ORM

O Django ORM atua como intermediário entre os models e o banco de dados:

- **Models → Banco**: Converte classes Python em tabelas SQL
- **Banco → Models**: Recupera dados do banco e os transforma em objetos Python
- **Migrações**: Sincroniza mudanças nos models com o banco de dados

## 📷 Gerenciamento de Imagens

- As imagens são armazenadas no servidor (pasta `media/`)
- O banco de dados armazena apenas o caminho das imagens
- Isso evita sobrecarga no banco de dados
- Pillow é necessário para processamento de imagens

## 🔧 Comandos Importantes

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor de desenvolvimento
python manage.py runserver

# Shell interativo do Django
python manage.py shell
```

## 📚 Próximos Passos

- Implementar views personalizadas
- Criar templates para frontend
- Adicionar filtros no admin
- Implementar sistema de upload de múltiplas imagens
- Adicionar validações customizadas
- Criar API REST com Django REST Framework

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido com Django** 🚗✨
