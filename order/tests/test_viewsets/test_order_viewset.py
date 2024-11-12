import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import ProductFactory, CategoryFactory
from product.models import Product

class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        # Criar categoria e produto
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        # Verifica se a listagem de pedidos está funcionando
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Valida os dados do pedido retornado
        order_data = json.loads(response.content)
        self.assertEqual(order_data[0]["product"][0]["title"], self.product.title)
        self.assertEqual(order_data[0]["product"][0]["price"], self.product.price)
        self.assertEqual(order_data[0]["product"][0]["active"], self.product.active)
        self.assertEqual(order_data[0]["product"][0]["category"][0]["title"], self.category.title)

    def test_create_order(self):
        user = UserFactory()  # Criação de um usuário
        product = ProductFactory()  # Criação de um produto
        data = json.dumps({"products_id": [product.id], "user": user.id})  # Dados de entrada

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),  # URL de criação do pedido
            data=data,
            content_type="application/json",
        )

        print(response.content)  # Imprime a resposta para diagnóstico

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Espera um código 201


        # Verifica se o pedido foi realmente criado no banco
        created_order = Order.objects.get(user=user)
        self.assertIn(product, created_order.product.all())  # Verifica se o produto está no pedido criado
