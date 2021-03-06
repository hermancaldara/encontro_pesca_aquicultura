# -*- coding: utf-8 -*-

from django.db import models


class Inscricao(models.Model):

    class Meta:        
    
        verbose_name_plural = 'Inscrições'

    nome = models.CharField(verbose_name='Nome', max_length=200)
    instituicao = models.CharField(
        verbose_name='Instituição/Departamento', 
        max_length=200
    )
    nucleo = models.CharField(
        verbose_name='Núcleo de Pesquisa Aplicada à Pesca (NUPA)',
        max_length=200
    )
    pais = models.CharField(verbose_name='País', max_length=30)
    endereco = models.CharField(verbose_name='Endereço', max_length=200)
    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=10,
        help_text="Exemplo:2299991111",
    )
    fax = models.CharField(
        verbose_name='Fax',
        max_length=10,
        help_text="Exemplo:2299991111",
        blank=True,
    )
    celular = models.CharField(
        verbose_name='Celular',
        max_length=10,
        blank=True,
    )
    email = models.EmailField(verbose_name='E-mail')
    categoria = models.CharField(
        verbose_name='Categoria do participante', 
        max_length=12,
        choices=(
            ('estudante', 'Estudante'), 
            ('professor', 'Professor'), 
            ('profissional', 'Profissional'),
        ),
    )
    apresenta_trabalho = models.CharField(
        max_length=3,
        choices=(
            ('nao', 'Não'),
            ('sim', 'Sim'),
        ),
        default = None,
    )
    titulo_trabalho = models.CharField(
        verbose_name="Título do trabalho (Preencha apenas se for apresentar algum trabalho)", 
        max_length=100,
        blank=True,
    )
    anexo = models.FileField(
        verbose_name='Anexar trabalho', 
        upload_to='docs/', 
        blank=True,
    )
    poster = models.FileField(
        verbose_name='Anexar pôster', 
        upload_to='posters/', 
        blank=True,
    )
    
    def __unicode__(self):
        return self.nome
