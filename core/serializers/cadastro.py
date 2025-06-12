from rest_framework.serializers import ModelSerializer

from core.models import Cadastro

class CadastroSerializer(ModelSerializer):
    class Meta:
        model = Cadastro
        fields = "__all__"