import jinja2
import pdfkit

def crea(ruta_template,info, rutacss):
    nombre_template = ruta_template.split("/")[-1]
    ruta_template = ruta_template.replace(nombre_template,"")
    env = jinja2.Environment(loader = jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)
    options = {
        "page-size" : "Letter",
        "encoding" : "UTF-8"
    }
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    ruta_salida = "C:/Users/pc/OneDrive - Escuela Politécnica Nacional/Escritorio/Archivo.pdf"
    pdfkit.from_string(html,ruta_salida,css=rutacss,options=options,configuration=config)

if __name__ == '__main__':
    ruta_template = "C:/Users/pc/Python/Crear_pdfs/template.html"
    rutacss = r"C:\Users\pc\Python\Crear_pdfs\estilos.css"
    info = {"nombre": "Hola", "edad" : 15}
    crea(ruta_template,info,rutacss)
    print ("! Pdf creado de forma exitosa ¡")