from rest_framework import serializers
from api.models import CodeExplainer
from api.utils import send_code_to_api

class CodeExplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeExplainer
        fields = ("id","_input","_method","_output")
        extra_kwargs = {
            "_output":{"read_only":True}
        }
    
    def create(self, validated_data):
        ce = CodeExplainer(**validated_data)
        _output = send_code_to_api(validated_data["_input"], validated_data["_method"])
        ce._output = _output
        ce.save()
        return ce