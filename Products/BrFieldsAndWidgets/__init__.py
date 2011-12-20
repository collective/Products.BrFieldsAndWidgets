# -*- coding: utf-8 -*-

from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from Products.Archetypes.public import process_types, listTypes

from Products.BrFieldsAndWidgets.config import ADD_CONTENT_PERMISSION
from Products.BrFieldsAndWidgets.config import GLOBALS
from Products.BrFieldsAndWidgets.config import PROJECTNAME
from Products.BrFieldsAndWidgets.config import SKINS_DIR

registerDirectory(SKINS_DIR, GLOBALS)

from zope.i18nmessageid import MessageFactory as BaseMessageFactory
MessageFactory = BaseMessageFactory('Products.BrFieldsAndWidgets')

from Products.BrFieldsAndWidgets import validators
from Products.BrFieldsAndWidgets.content import BrFieldsAndWidgetsDemo


def initialize(context):

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)
    utils.ContentInit(
            PROJECTNAME + ' Content',
            content_types = content_types,
            permission = ADD_CONTENT_PERMISSION,
            extra_constructors = constructors,
            fti = ftis,
            ).initialize(context)
