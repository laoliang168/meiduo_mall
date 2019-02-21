from django.shortcuts import render
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods
from goods.serializers import SKUSerializer, OrderInfoSerializer
# Create your views here.
from users.models import User


class UserInfoOrderView(ListAPIView):
    """个人订单"""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderInfoSerializer
    # queryset = OrderInfo.objects.all()

    def get_queryset(self):
        user = self.request.user
        orders = OrderInfo.objects.filter(user_id=user.id)
        for order in orders:
            order.create_time = order.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return orders

    # pagination_class = PageNumberPagination


# class UserInfoOrderView(APIView):
#     """个人订单"""
#     permission_classes = [IsAuthenticated]
#     # serializer_class = UserCenterOrderSerializer
#
#     def get(self, request):
#         user = request.user
#         orders = user.orderinfo_set.all()
#         order_id_list = []
#         skus = []
#         for order in orders:
#             order_id_list.append(order)
#             goods = order.skus.all()
#             for good in goods:
#                 skus.append(good.sku)
#         data = {'results': order_id_list}
#         # print(serializer.data)
#         return Response(data=data)

    # def get(self, request):
    #     user_id = request.user.id
    #
    #     orders = User.objects.get(id=user_id)
    #     serializer = UserCenterOrderSerializer({'orders': orders})
    #     return Response(serializer.data)


class SKUListView(ListAPIView):
    """
    sku列表数据
    """
    serializer_class = SKUSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('create_time', 'price', 'sales')

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SKU.objects.filter(category_id=category_id, is_launched=True)
