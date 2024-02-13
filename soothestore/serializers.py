from rest_framework import serializers
from .models import MassageChair, Brand, ChairFeature, Color_Options

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name', 'authorized_in']

class ChairFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChairFeature
        fields = ['id', 'called']

class ColorOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color_Options
        fields = ['id', 'color_name', 'color_code', 'image']

class MassageChairSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    available_colors = ColorOptionsSerializer(many=True)
    features = ChairFeatureSerializer(many=True)
    color_options = serializers.SerializerMethodField()
    chair_features = serializers.SerializerMethodField()
    
    class Meta:
        model = MassageChair
        fields = ['id', 'title', 'brand', 'price', 'description', 'available_colors', 'features', 'purchased', 'rating', 'posted', 'color_options', 'chair_features']

    def get_color_options(self, obj):
        return [[color.color_name, color.color_code, color.image.url] for color in obj.available_colors.all()]

    def get_chair_features(self, obj):
        return [feature.called for feature in obj.features.all()]