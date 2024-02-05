import requests
import json

url = 'https://datos.comunidad.madrid/catalogo/dataset/ae433b7e-98f7-4547-8aa5-6ada557a429f/resource/21424b1c-6465-4db9-a5e3-6ddf180c634b/download/centros_educativos.json'

response = requests.get(url)

if response.status_code == 200:
    centros_json = json.loads(response.text)
    centros_publicos=[]
    for centro in centros_json['data']:
        if centro['centro_titularidad'] == 'PÚBLICO':
            prioridad = 0
            if(centro['centro_tipo_desc_abreviada'] == 'IES' or centro['centro_tipo_desc_abreviada'] == 'CP IFP' or centro['centro_tipo_desc_abreviada'] == 'EOI'):
                prioridad = 2
            elif(centro['centro_tipo_desc_abreviada'] == 'CP PRI' or centro['centro_tipo_desc_abreviada'] == 'CP INF-PRI'):
                prioridad = 1
            else:
                prioridad = 0

            if(centro['dat_nombre'] == 'Madrid-Sur'):
                prioridad+=1
    
            if(centro['centro_titular'] == 'AYUNTAMIENTO'):
                 prioridad-=1

            centros_publicos.append( { 
                'x_cod_centro': centro['centro_codigo'],
                'name': centro['centro_nombre'],
                'email_from': centro['contacto_email1'],
                'phone': centro['contacto_telefono1'],
                'website': centro['contacto_web'],
                'street': centro['direccion_via_tipo'] + " " + centro['direccion_via_nombre'] + " " + centro['direccion_numero'],
                'zip': centro['direccion_codigo_postal'],
                'city': centro['municipio_nombre'],
                'x_tipo_centro_abreviatura': centro['centro_tipo_desc_abreviada'],
                'x_nombre_dat': centro['dat_nombre'],
                'priority': str(prioridad)
            })

else:
    print(f"Error al obtener el archivo. Código de estado: {response.status_code}")
   

import xmlrpc.client

url = 'http://192.168.146.21:8069'

db = 'P4_Thomas_Jiaxin'
username = 'thomas@admin.com'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password, 'crm.lead', 'check_access_rights', ['read'], {'raise_exception': False})


for centro in centros_publicos:
    try:
        id = models.execute_kw(db, uid, password, 'crm.lead', 'create',
            [{'x_cod_centro': centro['x_cod_centro'],
              'name': centro['name'],
             'email_from': centro['email_from'],
             'phone': centro['phone'],
             'website': centro['website'],
             'street': centro['street'],
             'zip': centro['zip'],
             'city': centro['city'],
             'x_tipo_centro_abreviatura': centro['x_tipo_centro_abreviatura'],
             'x_nombre_dat': centro['x_nombre_dat'],
             'priority': centro['priority']}])
    except Exception as e:
        print(f"Error creating lead: {e}")