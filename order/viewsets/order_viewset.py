<<<<<<< HEAD

from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
=======

from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
>>>>>>> pagination
    queryset = Order.objects.all()