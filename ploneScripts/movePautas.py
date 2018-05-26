# -*- coding: utf-8 -*-

from plone import api
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

mes   = '201707'
date_range = {
    'query': (
        DateTime('2017-07-01 00:00:00'),
        DateTime('2017-07-31 23:59:59'),
    ),
    'range': 'min:max',
}

app.redacao
items = app.redacao.portal_catalog.searchResults(meta_type='Pauta', path={'query': '/redacao/pautas/'}, getData=date_range)


content_folder = app.redacao.pautas
destino = content_folder[mes]


for item in items:
  obj = item.getObject()
  content_folder.move(obj,destino)
  print item.created, item.title

# Commit transaction
import transaction; transaction.commit()
# Perform ZEO client synchronization (if running in clustered mode)
app._p_jar.sync()
