#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import codecs

f = codecs.open('municipios.json', 'r', 'utf-8')
data = f.read()
parsed_json = json.loads(data)

#def getChildrens(children, indentacao, arq):
#    for x in children:
#        idPesquisa =  x['id']
#        nome = x['indicador']
#        aux = str(indentacao) + '' + str(idPesquisa) + ' - ' + nome + '\n'
#        children = x['children']
#        arq.write(aux)
#        getChildrens(children, indentacao + '  ' , arq)


with codecs.open('municipios-tarjas.txt', 'w', 'utf-8') as w:

    for item in parsed_json:

        cod = item['id']
        nome = item['nome']
        microrregiao = item['microrregiao']
        mesorregiao = microrregiao['mesorregiao']
        uf = mesorregiao['UF']['sigla']
        w.write('%s-%s\n' % (nome, uf))


    #print item['microrregiao']

#    idPesquisa =  item['id']
#    nome = item['nome']
#    observacao = item['observacao']
#    aux2 = unicode(idPesquisa) + ' - ' + unicode(nome)  + '\n'
#    arq.write(aux2)
#    url = 'http://servicodados.ibge.gov.br/api/v1/pesquisas/' + str(idPesquisa) + '/indicadores'
#    f = urllib.urlopen(url)
#    data = f.read()
#    folhas = json.loads(data)
#    aux3 = getChildrens(folhas, '  ', arq)

#arq.close()


{
u'microrregiao':
    {u'id': 53001,
    u'mesorregiao':
        {u'UF':
            {u'regiao':
                {u'nome': u'Centro-Oeste', u'id': 5, u'sigla': u'CO'},
                u'nome': u'Distrito Federal',
                u'id': 53,
                u'sigla': u'DF'
            }, u'id': 5301, u'nome': u'Distrito Federal'},
        u'nome': u'Bras\xedlia'},
    u'id': 5300108,
u'nome': u'Bras\xedlia'
}
