from rest_framework.viewsets import ModelViewSet

from core.models import Cadastro
from core.serializers import CadastroSerializer
from django.contrib.auth.hashers import make_password

class CadastroViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer

    def perform_create(self, serializer):
        senha_plana = self.request.data.get('senha')
        senha_hash = make_password(senha_plana)
        serializer.save(senha=senha_hash)