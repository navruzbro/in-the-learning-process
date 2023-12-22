from rest_framework import serializers
from .models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','subtitle','author','isbn','price','content')


    def validate(self, data):
        title = data.get("title", None)
        author = data.get("author", None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"nom harflardan iborat bo'lsin"
                }
            )
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status":False,
                    "message":"bu kitob avvaldan mavjud"
                }
            )

        return data 
    
    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                    "status":False,
                    "message":"Narx noto'g'ri kiritilgan!"
                }
            )
        return price