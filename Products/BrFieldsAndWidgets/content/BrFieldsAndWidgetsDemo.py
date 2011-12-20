# -*- coding:utf-8 -*-
""" demonstrates the use of BrFieldsAndWidgets """
from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi

from Products.BrFieldsAndWidgets.config import PROJECTNAME

from Products.BrFieldsAndWidgets.content.BrFieldsAndWidgets import CPFField
from Products.BrFieldsAndWidgets.content.BrFieldsAndWidgets import CEPField
from Products.BrFieldsAndWidgets.content.BrFieldsAndWidgets import CNPJField
from Products.BrFieldsAndWidgets.content.BrFieldsAndWidgets import BrPhoneField


schema = atapi.BaseSchema + atapi.Schema((
    CPFField('cpf',
                searchable=1,
                ),
    CEPField('cep',
                searchable=1,
                ),
    CNPJField('cnpj',
                searchable=1,
                ),
    BrPhoneField('phone',
                searchable=1,
                ),
))


class BrFieldsAndWidgetsDemo(atapi.BaseContent):
    """
    Demo for BrFieldsAndWidgets
    """
    meta_type = portal_type = archetype_name = 'BrFieldsAndWidgetsDemo'
    content_icon = "document_icon.gif"
    schema = schema
    security = ClassSecurityInfo()


atapi.registerType(BrFieldsAndWidgetsDemo, PROJECTNAME)
