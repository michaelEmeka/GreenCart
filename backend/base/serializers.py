from rest_framework import serializers
from rest_framework.request import Request
from .models import Item, ItemTag
from users.models import User

class ListItemSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ["item_name", "item_price", "date_added", "tags"]
    
    def get_tags(self, obj):
        return [tag.tag_name for tag in obj.item_tags.all()]

class CreateItemSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = Item
        fields = ["item_name", "item_price", "item_description", "date_added", "tags", "quantity"]

    def validate(self, attrs):
        item_name = attrs["item_name"]
        item_price = attrs["item_price"]
        tags = attrs.get("tags")
        quantity = attrs["quantity"]
        print(tags)

        if not item_name:
            raise ValueError("This field can not be vacant")
        if item_price:
            if isinstance(item_price, str):
                raise TypeError("This field is a integer/float field")
        else:
            raise ValueError("This field can not be vacant")
        if not quantity:
            raise ValueError("This field can not be vacant")
        return attrs

    def create(self, validated_data):
        item_name = validated_data["item_name"]
        item_price = validated_data["item_price"]
        item_description=validated_data.get("item_description")
        tags = validated_data.get("tags")
        quantity = validated_data.get("quantity")
        user = User.objects.get(id=self.context.get("request").user.id)

        item = Item.objects.create(user=user, item_name=item_name, item_price=item_price, item_description=item_description, quantity=quantity)

        for tag_name in tags:
            print(tag_name)
            ItemTag.objects.get(tag_name=tag_name).items.add(item)

        return {
            "item_name": str(item_name),
            "item_description": str(item_description),
            "item_price": item_price,
            "item_tags": tags
        }

class GetItemSerializer(serializers.ModelSerializer):
    #tags = serializers.SerializerListField()
    tags_list = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Item
        fields=[
            "item_name", "item_description", "item_price", "tags_list", "quantity"
        ]
    def get_tags_list(self, obj):
        item_tags = [tag.tag_name for tag in obj.item_tags.all()]
        return item_tags

class UpdateItemSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)
    class Meta:
        model = Item
        fields = ["item_name", "item_description", "item_price", "tags", "quantity"]

    def validate(self, attrs):
        item_name = attrs["item_name"]
        item_description = attrs.get("item_description")
        item_price = attrs.get("item_price")
        print(attrs)
        if not item_name:
            raise ValueError("This field can not be vacant")
        if not item_price:
            raise ValueError("This field can not be vacant")
        if not quantity:
            raise serializers.ValidationError("This field can not be vacant")
        return attrs

    def update(self, instance, validated_data):
        # Update Item
        instance.item_name = validated_data["item_name"]
        instance.item_description = validated_data.get("item_description")
        instance.item_price = validated_data["item_price"]
        instance.quantity = validated_data.get("quantity")
        tags = validated_data.get("tags")

        # Remove unwanted tags
        for tag in instance.item_tags.all():
            if tag.tag_name not in tags:
                tag.items.remove(instance)
        # Add new tags
        for tag_name in tags:
            try:
                ItemTag.objects.get(tag_name=tag_name).items.add(instance)
            except (ItemTag.DoesNotExist, KeyError) as e:
                print(e)
                # return {"error": f"{tag_name} tag does not exist."}
        instance.save()
        return instance

class DeleteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item

class BaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTag
        fields = "__all__"
