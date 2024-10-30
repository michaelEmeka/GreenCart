from rest_framework import serializers

class defaultNull(serializers.Serializer):
    class Meta:
        ref_name = 'BinDefaultNull'
    pass