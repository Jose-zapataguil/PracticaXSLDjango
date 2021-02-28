from django.shortcuts import render
import lxml.etree as ET
# Create your views here.

from django.http import HttpResponse

import psycopg2


def xml(request):
    conn = None
    xml = ""
    try:
        #        params = config()
        #        conn = psycopg2.connect(**params)
        conn = psycopg2.connect(user="odoo",
                                password="odoo",
                                host="192.168.18.2",
                                port="5432",
                                database="odoo")
        cur = conn.cursor()
        consulta = """ select
	'' || xmlroot(elem_secuencia, version '1.0', standalone yes) as documento
from
	(
	select
		xmlelement(name "Products" , xmlagg (campo) ) as elem_secuencia
	from
		(
		select
			xmlelement(name "Product", 
			xmlelement(name "Product_ID", pp.id), 
			xmlelement (name "Imagen",pp.id || '.png'),
			xmlelement (name "Name", case when custom.atributos_custom is null then it.value else it.value || ' ' || custom.atributos_custom end ), 
			xmlelement (name "Retail_Price" , pt.list_price + coalesce(custom.precio_extra_custom, 0)), 
			xmlelement(name "Thumbnail_URL", coalesce(itd.value, pt.description_sale)), 
			xmlelement (name "Product_URL", '/web#id=' || pt.id || '&amp;model=product.template&amp;view_type=form&amp;cids=') 
			) as campo
		from
			product_product pp
		left join ir_translation it on
			it.name = 'product.product,name'
			and it.res_id = pp.id
			and it.lang = 'es_PA'
		left join product_template pt on
			pp.product_tmpl_id = pt.id
		left join product_category pc on
			pt.categ_id = pc.id
		left join ir_translation itd on
			pt.id = itd.res_id
			and itd.lang = 'es_PA'
			and itd.name = 'product.template,description_sale'
		left join uom_uom uu on
			pt.uom_id = uu.id
		left join ir_translation itu on
			itu.name = 'uom.uom,name'
			and itu.lang = 'es_PA'
			and itu.res_id = uu.id
		left join (
			select
				pp.id as id_producto, string_agg(coalesce(ita.value, pa.name) || ': ' || coalesce(itv.value, pav.name), ', ') as atributos_custom, string_agg(coalesce(ita.value, pa.name) || ': ' || ptav.price_extra, ', ') as precios_custom, sum(ptav.price_extra) as precio_extra_custom
			from
				product_product pp
			left join product_variant_combination pvc on
				pvc.product_product_id = pp.id
			left join product_template_attribute_value ptav on
				pvc.product_template_attribute_value_id = ptav.id
			left join product_attribute pa on
				ptav.attribute_id = pa.id
			left join ir_translation ita on
				pa.id = ita.res_id
				and ita.lang = 'es_PA'
				and ita.name = 'product.attribute,name'
			left join product_attribute_value pav on
				ptav.product_attribute_value_id = pav.id
			left join ir_translation itv on
				pav.id = itv.res_id
				and itv.lang = 'es_PA'
				and itv.name = 'product.attribute.value,name'
			group by
				pp.id ) custom on
			pp.id = custom.id_producto
		left join ir_attachment ia on
			pt.id = ia.res_id
			and ia.res_model = 'product.template'
			and ia.name = 'image_512'
		where
			pt.type = 'product' ) c )consulta;"""

        #        cur.execute("select * from prueba")
        cur.execute(consulta)
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            xml = row[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    #    return HttpResponse(open('prueba.xml').read())
    return HttpResponse(xml, content_type="application/xml")


def parte1(request):
    return render(request, 'category1.html')


def ficheroXSLT(request):
    xsl = open("pages/static/productos.xsl")
    return HttpResponse(xsl, content_type="application/xml")


def parte2(request):
    try:
        conn = psycopg2.connect(user="odoo",
                                password="odoo",
                                host="192.168.18.2",
                                port="5432",
                                database="odoo")
        cur = conn.cursor()
        consulta = """ select
		'' || xmlroot(elem_secuencia, version '1.0', standalone yes) as documento
	from
		(
		select
			xmlelement(name "Products" , xmlagg (campo) ) as elem_secuencia
		from
			(
			select
				xmlelement(name "Product", 
				xmlelement(name "Product_ID", pp.id), 
				xmlelement (name "Imagen",pp.id || '.png'),
				xmlelement (name "Name", case when custom.atributos_custom is null then it.value else it.value || ' ' || custom.atributos_custom end ), 
				xmlelement (name "Retail_Price" , pt.list_price + coalesce(custom.precio_extra_custom, 0)), 
				xmlelement(name "Thumbnail_URL", coalesce(itd.value, pt.description_sale)), 
				xmlelement (name "Product_URL", '/web#id=' || pt.id || '&amp;model=product.template&amp;view_type=form&amp;cids=') 
				) as campo
			from
				product_product pp
			left join ir_translation it on
				it.name = 'product.product,name'
				and it.res_id = pp.id
				and it.lang = 'es_PA'
			left join product_template pt on
				pp.product_tmpl_id = pt.id
			left join product_category pc on
				pt.categ_id = pc.id
			left join ir_translation itd on
				pt.id = itd.res_id
				and itd.lang = 'es_PA'
				and itd.name = 'product.template,description_sale'
			left join uom_uom uu on
				pt.uom_id = uu.id
			left join ir_translation itu on
				itu.name = 'uom.uom,name'
				and itu.lang = 'es_PA'
				and itu.res_id = uu.id
			left join (
				select
					pp.id as id_producto, string_agg(coalesce(ita.value, pa.name) || ': ' || coalesce(itv.value, pav.name), ', ') as atributos_custom, string_agg(coalesce(ita.value, pa.name) || ': ' || ptav.price_extra, ', ') as precios_custom, sum(ptav.price_extra) as precio_extra_custom
				from
					product_product pp
				left join product_variant_combination pvc on
					pvc.product_product_id = pp.id
				left join product_template_attribute_value ptav on
					pvc.product_template_attribute_value_id = ptav.id
				left join product_attribute pa on
					ptav.attribute_id = pa.id
				left join ir_translation ita on
					pa.id = ita.res_id
					and ita.lang = 'es_PA'
					and ita.name = 'product.attribute,name'
				left join product_attribute_value pav on
					ptav.product_attribute_value_id = pav.id
				left join ir_translation itv on
					pav.id = itv.res_id
					and itv.lang = 'es_PA'
					and itv.name = 'product.attribute.value,name'
				group by
					pp.id ) custom on
				pp.id = custom.id_producto
			left join ir_attachment ia on
				pt.id = ia.res_id
				and ia.res_model = 'product.template'
				and ia.name = 'image_512'
			where
				pt.type = 'product' ) c )consulta;"""

        #        cur.execute("select * from prueba")
        cur.execute(consulta)
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            xml = row[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    with open("pages/static/productos.xml", "w") as f:
        f.write(xml)

    xsl = open("pages/static/productos.xsl")
    dom = ET.parse(open("pages/static/productos.xml"))
    xslt = ET.parse(xsl)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    productos = str(newdom)
    context = {'productos':productos}
    return render(request,'category2.html',context)
