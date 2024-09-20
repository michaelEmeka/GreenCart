from rest_framework import serializers
from rest_framework.request import Request
from .models import Item, ItemTag

class ListItemSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ["item_name", "item_price", "date_added", "tags"]
    
    def get_tags(self, obj):
        return [tag.tag_name for tag in obj.item_tags.all()]

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
        item_tags = validated_data.get("tags")
        
        item = Item.objects.create(item_name=item_name, item_price=item_price, item_description=item_description)

        for tag_name in item_tags:
            ItemTag.objects.get(tag_name=tag_name).items.add(item)
        
        return {
            "item_name": str(item_name),
            "item_description": str(item_description),
            "item_price": item_price,
            "item_tags": item_tags
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
        item_tags = [tag.tag_name for tag in obj.item_tags.all()]
        return item_tags

class UpdateItemSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)
    class Meta:
        model = Item
        fields = ["item_name", "item_description", "item_price", "tags"]
    
    def validate(self, attrs):
        item_name = attrs["item_name"]
        item_description = attrs.get("item_description")
        item_price = attrs.get("item_price")
        print(attrs)
        if not item_name:
            raise ValueError("This field can not be vacant")
        if not item_price:
            raise ValueError("This field can not be vacant")
        return attrs
    
    def update(self, instance, validated_data):
        #Update Item
        instance.item_name = validated_data["item_name"]
        instance.item_description = validated_data.get("item_description")
        instance.item_price = validated_data["item_price"]
        tags = validated_data.get("tags")
        
        #Remove unwanted tags
        for tag in instance.item_tags.all():
            if tag.tag_name not in tags:
                tag.items.remove(instance)
        #Add new tags
        for tag_name in tags:
            try:
                ItemTag.objects.get(tag_name=tag_name).items.add(instance)
            except (ItemTag.DoesNotExist, KeyError) as e:
                print(e)
                #return {"error": f"{tag_name} tag does not exist."}
        #instance.save()
        return instance
    
class DeleteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

class BaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTag
        fields = "__all__"