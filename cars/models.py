from django.db import models

class Car(models.Model):  # Nome da tabela no banco de dados
    id = models.AutoField(primary_key=True)  
    # Campo ID, chave primária, autoincrementado automaticamente pelo Django

    model = models.CharField(max_length=200)  
    # Campo de texto (string), aceita até 200 caracteres

    brand = models.CharField(max_length=200)  
    # Marca do carro, também um campo de texto

    factory_year = models.IntegerField(blank=True, null=True)  
    # Ano de fabricação (inteiro), pode ser deixado em branco ou nulo

    model_year = models.IntegerField(blank=True, null=True)  
    # Ano do modelo (inteiro), pode ser deixado em branco ou nulo

    value = models.FloatField(blank=True, null=True)  
    # Valor do carro (número decimal), pode ser deixado em branco ou nulo


