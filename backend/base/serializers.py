from rest_framework import serializers
from rest_framework.request import Request
from .models import Item, ItemTag

class ListCreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["item_name", "item_price", "date_added"]

class CreateItemSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = Item
        fields = ["item_name", "item_price", "item_description", "date_added", "tags"]
    
    def validate(self, attrs):
        item_name = attrs["item_name"]
        item_price = attrs["item_price"]
        tags = attrs.get("tags")
        print(tags)
        
        if not item_name:
            raise ValueError("This field can not be vacant")
        if item_price:
            if isinstance(item_price, str):
                raise TypeError("This field is a integer/float field")
        else:
            raise ValueError("This field can not be vacant")
        
        return attrs
    
    def create(self, validated_data):
        item_name = validated_data["item_name"]
        item_price = validated_data["item_price"]
        item_description=validated_data.get("item_description")
        tags = validated_data.get("tags")
        
        item = Item.objects.create(item_name=item_name, item_price=item_price, item_description=item_description)

        for tag_name in tags:
            ItemTag.objects.get(tag_name=tag_name).items.add(item)
        
        return {
            "item_name": str(item_name),
            "item_description": str(item_description),
            "item_price": item_price,
            "tags": tags
        }

class GetItemSerializer(serializers.ModelSerializer):
    #tags = serializers.SerializerListField()
    tags_list = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Item
        fields=[
            "item_name", "item_description", "item_price", "tags_list"
        ]
    def get_tags_list(self, obj):
        id = self.context.get("id")
        #item = Item.objects.get(id=id)
        
        item_tags = [tag.tag_name for tag in obj.item_tags.all()]
        return item_tags