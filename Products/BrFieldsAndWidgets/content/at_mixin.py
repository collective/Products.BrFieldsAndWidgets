# -*- coding: utf-8 -*-
__author__ = """Simples Consultoria <contato@simplesconsultoria.com.br>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *

from Products.BrFieldsAndWidgets.content.BrFieldsAndWidgets import *

from Products.BrFieldsAndWidgets import MessageFactory as _


schema = Schema((
    StringField(
        name='logradouro',
        widget=StringWidget(
            size="30",
            visible={'view': 'invisible', 'edit': 'visible'},
            label=_(u'Logradouro'),
            description=_(u'Exemplo: Rua Mourato Coelho'),
        ),
        required=True,
        schemata="Address"
    ),

    StringField(
        name='numero',
        widget=StringWidget(
            size="7",
            visible={'view': 'invisible', 'edit': 'visible'},
            label=_(u'Número'),
            description=_(u'Exemplo: 12'),
        ),
        required=True,
        schemata="Address"
    ),

    StringField(
        name='complemento',
        widget=StringWidget(
            visible={'view': 'invisible', 'edit': 'visible'},
            label=_(u'Complemento'),
        ),
        schemata="Address"
    ),

    StringField(
        name='bairro',
        widget=StringWidget(
            visible={'view': 'invisible', 'edit': 'visible'},
            size="30",
            label=_(u'Bairro'),
            description=_(u'Exemplo: Pinheiros'),
        ),
        required=False,
        schemata="Address",
    ),

    CEPField(
        name='cep',
        required=1,
        widget=CEPWidget(
                        visible={'view': 'invisible', 'edit': 'visible'},
                        label=_(u'CEP'),
                        description=_(u'Informe o CEP.'),
                        ),
        schemata="Address"
    ),

    StringField(
        name='cidade',
        widget=StringWidget(
            visible={'view': 'invisible', 'edit': 'visible'},
            label=_(u'Cidade'),
            description=_(u'Informe sua cidade.'),
        ),
        required=True,
        schemata="Address"
    ),

    StringField(
        name='uf',
        widget=SelectionWidget
        (
            visible={'view': 'invisible', 'edit': 'visible'},
            size=1,
            label=_(u'UF'),
            description=_(u'Informe o seu estado.'),
        ),
        required=True,
        schemata="Address",
        vocabulary_factory='brasil.estados',
        enforceVocabulary=True,
    ),

    ComputedField(
        name='Endereco',
        expression='context.fmt_endereco()',
        widget=ComputedWidget(
            visible={'view': 'visible', 'edit': 'invisible'},
            label=_(u'Endereço'),
        ),
        default_output_type='text/x-html-safe',
        schemata="Address",
        searchable=True
    ),

    TextField(
        name='referencia',
        allowable_content_types=('text/html', ),
        widget=RichWidget
        (
            visible={'view': 'invisible', 'edit': 'invisible'},
            label=_(u'Referência'),
            description=_(u'Informe pontos de referência.'),
        ),
        required=False,
        schemata="Address",
        searchable=True,
        default_output_type='text/x-html-safe'
    ),

),
)


br_endereco_schema = BaseSchema.copy() + schema.copy()


class br_endereco:
    """Classe basica de endereco
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'br_endereco'

    meta_type = 'br_endereco'
    portal_type = 'br_endereco'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'br_endereco.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "br_endereco"
    typeDescMsgId = 'description_edit_br_endereco'

    _at_rename_after_creation = True

    schema = br_endereco_schema

    security.declarePrivate('fmt_endereco')

    def fmt_endereco(self):
        """Retorna um endereco formatado para o atributo Endereco
        """
        template = "%s,%s %s<br/>%s<br/>%s<br/>%s - %s"
        logradouro = self.getLogradouro()
        numero = self.getNumero()
        complemento = self.getComplemento()
        bairro = self.getBairro()
        cep = self.getCep()
        if cep:
            cep = "%s-%s" % (cep[:5], cep[-3:])
        cidade = self.getCidade()
        uf= self.getUf()

        return template % (logradouro,
                           numero,
                           complemento,
                           bairro,
                           cep,
                           cidade,
                           uf)
