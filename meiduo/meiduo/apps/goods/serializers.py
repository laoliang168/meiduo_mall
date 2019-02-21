from rest_framework import serializers

from .models import SKU
from orders.models import OrderInfo, OrderGoods


class SKUInfoSerializer(serializers.ModelSerializer):
    """订单商品详情"""
    class Meta:
        model = SKU
        fields = ['id', 'name', 'default_image_url']


class OrderGoodsSerializer(serializers.ModelSerializer):
    """订单商品数据序列化器"""
    sku = SKUInfoSerializer()

    class Meta:
        model = OrderGoods
        fields = ['count', 'sku', 'price']


class OrderInfoSerializer(serializers.ModelSerializer):
    """订单信息数据序列化器"""
    skus = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = ['status', 'pay_method', 'total_amount', 'freight', 'create_time', 'order_id', 'skus']


class SKUSerializer(serializers.ModelSerializer):
    """商品列表界面"""
    class Meta:
        model = SKU
        fields = ['id', 'name', 'price', 'default_image_url', 'comments']