#!/usr/bin/python

import requests
import ast
import urllib
import os
from slugify import slugify

def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename


log = open('log.txt','w')



imdb = open('imdb.txt','r')

imdb_codes = [line.strip() for line in imdb]

imdb.close()

imdb = open('imdb.txt','w')

contador = 0
tamanho = 0
skipped = 0
baixados = 0




for a in range(150):

    response = requests.get('https://yts.ag/api/v2/list_movies.json?sort_by=date_added&order_by=desc&limit=50&page='+str(a))
    aux = response.text
    page = ast.literal_eval(aux)

    if 'data' in page.keys():

        data = page['data']

        if 'movies' in data.keys():

            for filme in data['movies']:

                t1 = filme['title']
        #        t2 = filme['title_long']
        #        t3 = filme['title_english']
                t4 = filme['year']
                t5 = filme['genres']
        #        t6 = filme['runtime']
        #        t7 = filme['language']
        #        t8 = filme['mpa_rating']
                t9 = filme.get('rating','0')
        #        t10 = filme['date_uploaded_unix']
                t11 = filme.get('date_uploaded', '2000-01-01 00:00:00')
                t12 = filme.get('torrents', [] )
        #        t13 = filme['id']
                t14 = filme['imdb_code']
        #        t15 = filme['state']
        #        t16 = filme['small_cover_image']
        #        t17 = filme['medium_cover_image']
        #        t18 = filme['large_cover_image']
        #        t19 = filme['background_image_original']
        #        t20 = filme['background_image']
        #        t21 = filme['slug']
        #        t22 = filme['description_full']
        #        t23 = filme['summary']
        #        t24 = filme['synopsis']
        #        t25 = filme['url']
        #        t26 = filme['yt_trailer_code']

                if ('Horror' not in t5) and (t14 not in imdb_codes):

                    tam = ''
                    quality = ''
                    for torrent in t12:
                        tt1 = torrent['quality']
                        tt2 = torrent['url']
                        tt3 = torrent['seeds']
                        tt4 = torrent['size']

                        if quality == '':
                            quality = tt1
                            url = tt2
                            tam = tt4
                        else:
                            if tt1 == '1080p' and quality <> tt1:
                                quality = tt1
                                url = tt2
                                tam = tt4

                    if len(torrent)>0:
                        tam_aux = tam.split(' ')

                        if len(tam_aux) > 1:
                            if tam_aux[1] == 'MB':
                                tamanho = tamanho + float(tam[0])
                            elif tam_aux[1] == 'GB':
                                tamanho = tamanho + float(tam[0]) * 1024

                        url = url.replace('\/','/')

                        filename = unicode(str(t1) + ' - ' + str(t4) + ' - ' + str(quality) + ' - ' +  str(t14))
                        filename = slugify(filename) + '.torrent'
                        baixados = baixados + 1
                        contador = contador + 1
                        print "====================================================="
                        print contador, t11, filename, t9
                        print tamanho, baixados, skipped

                        rating = str(int(round(float(t9))))

                        cmd = "curl " + url + " -k -o " + rating+'/'+filename
                        a = os.system(cmd)
                        imdb.write(t14+'\n')
                        if a <> 0:
                            log.write(str(contador) + '\n')
                            log.write(filename + '\n')
                            log.write(url + '\n')
                            log.write('====================================\n')

                else:
                    skipped = skipped + 1
                    contador = contador + 1
                    print "====================================================="
                    print 'Pulou', contador, t11, str(t1), str(t4)
                    print tamanho, baixados, skipped

log.close()
imdb.close()
