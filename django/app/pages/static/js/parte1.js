var productos, items,menu,xml,xsl;
function limpiar(){
 productos = document.querySelector('.col-lg-9 .row');
 menu = document.querySelector('.col-lg-9 .row .col-lg-12')
  productos.textContent = "";
productos.appendChild(menu);
carga();
}
//Funcion que obtiene los ficheros xml y xsl de manera asíncrona
 function obtenerFicheros(url) {
  const result =  fetch(url, {
    method: 'GET',
    cache: 'no-cache'
  })
    .then(response => response.text())
    .then(str => (new window.DOMParser()).parseFromString(str, "text/xml"))
    .catch(error => console.log("Error:" + error))
  return result;
}
async function carga() {
  //Llamo a la funcion que obtiene los ficheros xml y xsl del servidor.
  var xmlPromesa = obtenerFicheros("xml");
  var xslPromesa = obtenerFicheros("xsl");
  xml = await xmlPromesa;
  xsl = await xslPromesa;
  try {
    xslProcesor = new XSLTProcessor();
    xslProcesor.importStylesheet(xsl);
    resultDocument = xslProcesor.transformToFragment(xml, document);
    items = resultDocument.childElementCount;
    productos.appendChild(resultDocument);

    let p = document.querySelector('.product_top_bar h2');
    p.innerHTML = 'Productos (' + items + ')';
  } catch (error) {
    console.log("Error al generar el html");
    console.log("Error:"+error);
  }

}
document.addEventListener('DOMContentLoaded', limpiar)
