from rest_framework import serializers
from aluno.serializers import AlunoSerializer
from professor.models import Professor
from aluno.models import Aluno


class ProfessorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    alunos = AlunoSerializer(
        many=True
        ,
        read_only=True
    )

    def create(self, validated_data):
        professor = Professor.objects.create(**validated_data)
        return professor

    def update(self, instance, validated_data):
        instance.name = validated_data.get('nome')
        instance.idade - validated_data.get('idade')
        instance.save()
        return instance

