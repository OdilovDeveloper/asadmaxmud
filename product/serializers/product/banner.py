from rest_framework import serializers
from product.models.product import BannerModel, ProductModel  
from .product import ProductListSerializer  # qisqa mahsulot serializer


class BannerSerializers(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = BannerModel
        fields = ['id', 'name', 'image', 'category', 'products']

    def get_products(self, obj):
        request = self.context.get('request')
        products = ProductModel.objects.filter(category=obj.category)
        return ProductListSerializer(products, many=True, context={'request': request}).data
