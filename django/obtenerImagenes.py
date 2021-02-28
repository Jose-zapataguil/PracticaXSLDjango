# import psycopg2
import os
import subprocess
ip = "192.168.18.2"
id_contenedor = 'de75a7dfba3b'

def obtenerImagenes():
    for key in dicc.keys():
        os.system("docker cp "+id_contenedor+":/var/lib/odoo/filestore/odoo/"+dicc[key]+" /root/django/app/pages/static/img/"+str(key)+".png")

# try:
#     conn = psycopg2.connect(user="odoo",password="odoo",host=ip,port="5432",database="odoo")
#     cur = conn.cursor()
#     consulta = """select ia.store_fname,pp.id from product_product pp
# left join ir_translation it on it.name = 'product.product,name' and it.res_id=pp.id  and it.lang = 'es_PA'
# left join product_template pt on pp.product_tmpl_id = pt.id left join product_category pc on pt.categ_id = pc.id
# left join ir_attachment ia on pt.id = ia.res_id and ia.res_model = 'product.template' and ia.name = 'image_512'
# where pt.type='consu';"""
#     cur.execute(consulta)
#     rows = cur.fetchall()
#     conn.close()
# except:
#     pass
dicc = {5: 'a1/a1b5d1ebdc80468e880308fd7de60ec1f1831753', 6: 'b4/b41730ccf08d9ef6e15fa932e82b9883b757de51', 7: 'db/db67cfb0c1bde21ed910d1923ccb755348a7bcdf', 8: 'b5/b574b51390549e2006f44b554bfa2e8c8f87ff23', 12: 'eb/ebd7b52d88f7f02185c385a5ec787f482f5abb03', 13: 'eb/ebd7b52d88f7f02185c385a5ec787f482f5abb03', 14: 'eb/ebd7b52d88f7f02185c385a5ec787f482f5abb03', 15: 'eb/ebd7b52d88f7f02185c385a5ec787f482f5abb03', 16: '53/538290e442bbf974e9352e43331042cb2c786a07', 17: '6e/6e4a9b118e2d50dfb8f62ac0b30d8244a8e46853', 18: '9e/9e13dca4ea13eb0ca9eed05c9e4c7d74ca0ff954', 19: 'bc/bc9c191c77030940bb606330888d6a61bcc92663', 20: 'b8/b85968b493abbfcf3466dfb20bbb5eb68f1a884a', 21: 'df/df3e5d978156c1c197e1153b3d3b08822eb061c4', 23: '38/38d079d160952f98332b6e908476bb953f3ab208', 24: '38/38d079d160952f98332b6e908476bb953f3ab208', 25: '00/0030b44c24c51cc1dd3326118a07b129680c3287', 26: '54/5405ae082aaf82b3294f47ba4fd5441104ff253d', 27: '38/382016de005b570a2fe4fc9c2d9de5e79577106d', 28: '21/211fa20e346b17f426f4b5797a25cbbb2f8f2d62', 29: '64/6469bc4f7b6547eab08c45cf4fa1b3eb158e91e3', 30: 'ff/ff1c71b08421c249a5ac82f6e7f67521a9a7a079', 31: 'e2/e23189e6c2a77ad0a655283b13bb5150a42e5a71', 32: 'd7/d740c93c2db274388e178b5a77d7598e0fdf8081', 33: 'b6/b692c522e415e864508fad4e9e9fe6cfa3a556c2', 34: '4a/4abd5429e0001af8b374e095d69fcb85e4afbca4', 35: 'ae/ae5aa793fe2be423c68007efc9f48cc5d8bd751a', 37: 'eb/ebd7b52d88f7f02185c385a5ec787f482f5abb03', 38: 'eb/ebd7b52d88f7f02185c385a5ec787f482f5abb03'}
obtenerImagenes()