<<<<<<< HEAD
from order.models.order import Order
from rest_framework import serializers
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, many=True)  # Este campo é de leitura
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)  # Campo de escrita
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ['product', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}  # Campo 'product' não é obrigatório na criação

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')  # Remove o campo 'products_id' dos dados validados
        user_data = validated_data.pop('user')  # Remove o campo 'user' dos dados validados

        # Cria o pedido com o usuário
        order = Order.objects.create(user=user_data)

        # Adiciona os produtos ao pedido
        for product in product_data:
            order.product.add(product)

        return order
=======
from order.models.order import Order
from rest_framework import serializers
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, many=True)  # Este campo é de leitura
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)  # Campo de escrita
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ['product', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}  # Campo 'product' não é obrigatório na criação

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')  # Remove o campo 'products_id' dos dados validados
        user_data = validated_data.pop('user')  # Remove o campo 'user' dos dados validados

        # Cria o pedido com o usuário
        order = Order.objects.create(user=user_data)

        # Adiciona os produtos ao pedido
        for product in product_data:
            order.product.add(product)

        return order
>>>>>>> pagination
