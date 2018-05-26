# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
import datetime
import DateTime

from plone.app.textfield.value import RichTextValue



vet = [


 { "titulo" : "Governo quer humanizar e dar mais eficiência ao atendimento no SUS",  "id" : "sleep-away.mp3",  "data" : "2011-11-14 05-00",  "descricao" : "A presidenta Dilma Rousseff fala sobre as ações que o governo lançou na semana passada para melhorar a qualidade e humanizar o atendimento na saúde púlica. Ela explica no programa desta semana que o SOS Emergências vai dar mais agilidade e eficiência ao atendimento nos prontos-socorros dos maiores hospitais do país, começando por 11 capitais. Já o Melhor em Casa, será o serviço de atendimento médico domicilitar do SUS - o Sistema Único de Saúde. ",  "transcricao": "<p>Apresentador: Olá, eu sou o Luciano Seixas e estou aqui para o Café com a Presidenta, o nosso encontro semanal com a presidenta Dilma Rousseff. Bom dia, presidenta! <br /> <br />Presidenta: Bom dia, Luciano! E bom dia aos nossos ouvintes! <br /> <br />Apresentador: Presidenta, a senhora lançou, na semana passada, duas ações do governo na área de saúde: o SOS Emergências e o Melhor em Casa. Qual a importância destes programas? <br /> <br />Presidenta: Olha, Luciano, esses dois programas são muito importantes. Estamos, com eles, dando mais um passo para melhorar a qualidade da saúde pública e aumentar a eficiência do atendimento do Sistema Único de Saúde, o nosso SUS. Com o SOS Emergências e o Melhor em Casa, vamos enfrentar, com coragem, dois dos principais problemas da saúde pública: a superlotação nos prontos-socorros e a falta de leitos nos hospitais. O SOS Emergências, sabe, Luciano, vai permitir que a população seja atendida com mais rapidez e qualidade nas urgências dos hospitais. Já o Melhor em Casa é um serviço de atendimento médico domiciliar, que vai evitar as internações para aquelas pessoas que podem receber o tratamento em casa. <br /> <br />Apresentador: Bom, agora vamos falar de um programa de cada vez. O SOS Emergências vai reduzir a espera nos prontos-socorros? <br /> <br />Presidenta: Olha, Luciano, esse é o nosso objetivo. Nossa ação para melhorarmos os prontos-socorros vai começar por 11 hospitais de referência, em nove capitais. Até 2014, Luciano, nós vamos chegar a 40 emergências atendidas em todos os estados da Federação. Para esse programa dar certo, precisamos melhorar a gestão dos hospitais e o treinamento das equipes. E, para isso, vamos contar com a parceria dos melhores hospitais do país, aqueles que são chamados de hospitais de excelência. Mas a gente sabe que não se resolve o problema da qualidade do atendimento somente melhorando os prontos-socorros. Então, Luciano, o SOS Emergências estará integrado a outras ações do programa Saúde Toda Hora, que prevê investimentos de R$ 18,8 bilhões até 2014. Esses recursos vão para a rede do SAMU, para as UPAs 24 Horas, que são as Unidades de Pronto-Atendimento. Também serão utilizados para ampliação de leitos de UTI, para os serviços de atenção básica e no programa de atendimento médico domiciliar, o nosso Melhor em Casa. <br /> <br />Apresentador: E sobre o Melhor em Casa, presidenta, ele é parecido com o que chamam de ‘Home Care’, da rede privada? <br /> <br />Presidenta: A ideia é muito parecida. Oferecer a segurança e o cuidado do hospital no conforto do lar, onde o paciente terá o carinho da família e menor risco de infecções. Por isso ele chama Melhor em Casa. Hoje, o atendimento domiciliar já é adotado, como você sabe, na rede privada de saúde; e também temos algumas experiências municipais muito bem sucedidas. Nós então, Luciano, decidimos oferecer o tratamento domiciliar para humanizar o serviço público de saúde. Esse projeto é ainda mais positivo para os idosos, principalmente com o aumento da expectativa de vida no país. Nós vamos atender, em suas próprias casas, os doentes crônicos, os pacientes que estão em recuperação de cirurgias e as pessoas em processo de reabilitação motora. Para implantar esse programa, Luciano, nós vamos investir R$ 1 bilhão até 2014. Serão contratadas mil equipes de Atenção Domiciliar, e mais 400 equipes de apoio. Os governos estaduais e as prefeituras serão nossos queridos parceiros, porque um programa dessa dimensão, ele precisa de uma ação integrada. Eles é que vão selecionar, contratar e coordenar o trabalho das equipes do Melhor em Casa. Quando as mil equipes estiverem habilitadas, nós vamos conseguir atender 60 mil pacientes em suas casas, em todo o Brasil. Agora, tem uma coisa importante, os médicos dos hospitais vão indicar o tratamento domiciliar dependendo do caso de cada paciente. Mas opção de aderir ao programa será sempre do paciente e de sua família. Porque você sabe, não é, Luciano, há famílias que têm condições de receber os pacientes em casa, e outras famílias, infelizmente, não têm. <br /> <br />Apresentador: Presidenta, nosso tempo chegou ao fim. <br /> <br />Presidenta: Queria lembrar só mais uma coisa sobre o nosso Sistema Público de Saúde. O Brasil, Luciano, é o único país do mundo com mais de 100 milhões de habitantes que assumiu o desafio de ter um sistema universal, público, gratuito e, que nós queremos, de qualidade. Dos 190 milhões de brasileiros, 145 milhões dependem do SUS, veja só. Sabemos que é uma tarefa enorme, mas nós vamos enfrentar esse desafio, Luciano, porque os brasileiros e as brasileiras merecem uma saúde de qualidade. <br /> <br />Apresentador: Presidenta, muito obrigado por mais esse Café. <br /> <br />Presidenta: Muito obrigada a você. E um bom-dia para todos aqueles que nos acompanharam até agora! <br /> <br />Apresentador: Você pode acessar este programa na internet, o endereço é www.cafe.ebc.com.br. Voltamos segunda-feira, até lá!</p>"}, 
 
]





app.radio


for item in vet:

    id = item['id']
    titulo = item['titulo']
    data = item['data']
    descricao = item['descricao']
    transcricao = item['transcricao']

    result = app.radio.portal_catalog(Type="File",path={'query': '/radio/acervo/cafe-com-a-presidenta'}, Title=id)

    if len(result)>0:
        obj = result[0].getObject()
        
        d = data.split(' ')[0]
        h = data.split(' ')[1]
        ano = int(d.split('-')[0])
        mes = int(d.split('-')[1])
        dia = int(d.split('-')[2])
        hor = int(h.split('-')[0])
        min = int(h.split('-')[1])

        data = datetime.datetime(ano, mes, dia, hor, min)


        obj.creation_date = data
        obj.setModificationDate(data)
        obj.setTitle(titulo)
        obj.setDescription(descricao)
        obj.transcricao = RichTextValue( transcricao, 'text/html', 'text/html')
        obj.reindexObject()
        
    else:
        print data


# Commit transaction
import transaction; transaction.commit()
# Perform ZEO client synchronization (if running in clustered mode)
app._p_jar.sync()
