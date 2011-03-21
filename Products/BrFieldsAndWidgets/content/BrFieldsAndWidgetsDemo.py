""" demonstrates the use of BrFieldsAndWidgets """

from Products.Archetypes.public import *

from Products.BrFieldsAndWidgets import MessageFactory as _
from Products.BrFieldsAndWidgets.config import PROJECTNAME
from AccessControl import ClassSecurityInfo

from Products.BrFieldsAndWidgets.content.BrFieldsAndWidgets import *
from Products.BrFieldsAndWidgets.validators import ValidadorCNPJ
from Products.BrFieldsAndWidgets.validators import ValidadorCPF
from Products.BrFieldsAndWidgets.validators import ValidadorCEP
from Products.BrFieldsAndWidgets.validators import ValidadorBrPhone

schema = BaseSchema +  Schema((
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

class BrFieldsAndWidgetsDemo(BaseContent):
    """
    Demo for BrFieldsAndWidgets
    """
    meta_type = portal_type = archetype_name = 'BrFieldsAndWidgetsDemo'
    content_icon = "document_icon.gif"
    schema = schema
    security = ClassSecurityInfo()


registerType(BrFieldsAndWidgetsDemo,PROJECTNAME)
