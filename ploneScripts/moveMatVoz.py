# -*- coding: utf-8 -*-

from plone import api
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime


path = '/radio/programas/materias-da-voz/'

date_range = {
    'query': (
        DateTime('2015-01-01 00:00:00'),
        DateTime('2015-12-31 23:59:59'),
    ),
    'range': 'min:max',
}

app.radio

portal = api.portal.get()
destino = portal['programas']['materias-da-voz']['2015'] 


items = app.radio.portal_catalog.searchResults(Type="File", sort_on="created", sort_order="descending", path=path, created=date_range)
for item in items:
  obj = item.getObject()
  api.content.move(obj,destino)

  print item.created, item.title

# Commit transaction
import transaction; transaction.commit()
# Perform ZEO client synchronization (if running in clustered mode)
app._p_jar.sync()

