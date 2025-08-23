from django.db import models


#vamos criar a gestao de marcas, e uma nova tabela no banco de dados

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self): #faz aparecer a marca do carro em vez de object
        return self.name

class Car(models.Model):  # Nome da tabela no banco de dados
    id = models.AutoField(primary_key=True)  
    # Campo ID, chave primária, autoincrementado automaticamente pelo Django

    model = models.CharField(max_length=200)  
    # Campo de texto (string), aceita até 200 caracteres

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,related_name='car_brand')
    #Foreignkey ta dizendo pro django que esse campo vai ser uma ligacao com outra tabela, que a Brand que criamos acima
    #on_delete=models.CASCADE se o usuario clica em deletar a marca fiat por exemplo,vai apagar todos os carros da fiat do banco de dados.
    #on_delete=models.PROTECT = se o usuario deletar marca fiat vai aparecer uma mensagem dizendo que ele nao pode deletar.
    #related_name='car_brand' = existe uma relacao entre car e brand e o nome dessa relacao escolhi card_brand
    

    factory_year = models.IntegerField(blank=True, null=True)  
    # Ano de fabricação (inteiro), pode ser deixado em branco ou nulo

    model_year = models.IntegerField(blank=True, null=True)  
    # Ano do modelo (inteiro), pode ser deixado em branco ou nulo

    plate = models.CharField(max_length=10,blank=True,null=True)

    
    value = models.FloatField(blank=True, null=True)  
    # Valor do carro (número decimal), pode ser deixado em branco ou nulo

    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # as imagens vao ficar salvas na pasta principal cars

    def __str__(self): #faz aparecer o modelo do carro em vez de object
        return self.model

