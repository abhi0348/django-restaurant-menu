from rest_framework import serializers
from .models import dish, Category

class DishSerializer(serializers.ModelSerializer):
    class meta:
        model = dish
        fields =  ['id', 'name', 'price', 'description', 'category']  

class CategorySerializer(serializers.ModelSerializer):
    dish_set = DishSerializer(many=True, read_only=True)

    class meta:
        model = Category
        fields = ['id', 'name', 'dish_set'] 
    
