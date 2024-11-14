from django.test import TestCase
from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_1 = ProductFactory(title="Product 1")
        self.product_2 = ProductFactory(title="Product 2")

        self.order = OrderFactory(product=(self.product_1, self.product_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        print(serializer_data)  # Adicione esta linha para verificar a estrutura

        # Testa se os títulos dos produtos estão corretos
        self.assertEqual(serializer_data["product"][0]["title"], self.product_1.title)
        self.assertEqual(serializer_data["product"][1]["title"], self.product_2.title)
