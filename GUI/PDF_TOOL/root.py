from tkinter import *
import jinja2
import pdfkit


#Window Style
root = Tk()
root.title("PDF Tool")
root.configure(background="grey15")
root.attributes("-topmost",1)
width_root = 510
height_root = 300
root.iconbitmap(r"GUI\PDF_TOOL\pictures\pdf_icon.ico")

def create_pdf ():
    ruta_html = r"GUI/PDF_TOOL/pdf_style/structure_pdf.html"
    rutacss = r"GUI\PDF_TOOL\pdf_style\style_pdf.css"
    name = text_name.get()
    level = text_level.get()
    info = {"nombre":name,"level":level}
    nombre_html = ruta_html.split("/")[-1]
    ruta_html = ruta_html.replace(nombre_html,"")
    env = jinja2.Environment(loader = jinja2.FileSystemLoader(ruta_html))
    html = env.get_template(nombre_html)
    template = html.render(info)
    options = {"page-size":"Letter","encoding" :"UTF-8"}
    pdf_name = str(name[0] + "_certificado")
    config = pdfkit.configuration(wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    ruta_salida = f"C:/Users/pc/OneDrive - Escuela Politécnica Nacional/Escritorio/{pdf_name}.pdf"
    pdfkit.from_string(template,ruta_salida,css=rutacss,options=options,configuration=config)

#Center the Window
height_screen = root.winfo_screenheight() #Value about your screen
width_screen = root.winfo_screenwidth() #Value about your screen
x_center = int(width_screen/2 - width_root/2) 
y_center = int(height_screen/2 - height_root/2)
root.geometry(f"{width_root}x{height_root}+{x_center}+{y_center}") #Only allow int variables
root.resizable(False,False)

#Elements into a root
button_icon = PhotoImage(file="GUI\PDF_TOOL\pictures\create_pdf.png")
title = Label(root,text="Pdf Creator",justify="right",font="Roboto 30",fg="grey86",bg="grey15")
subtitle = Label(root,text="Python Certificate",justify="right", font="Roboto 15",fg="grey86",bg="grey15")
static_button = Button(root, text= "Create PDF",state="active", command=create_pdf,image=button_icon, compound=LEFT,width=100,fg="blue2")
label_name = Label(root,text="Student name is: ",justify="right",font= "Roboto 15",fg="firebrick1",bg="grey15")
label_level = Label(root,text="Level: ",justify="right",font = "Robot 15",fg="firebrick1",bg="grey15")
text_name = Entry(root,font="Roboto 15")
text_name.focus()
text_level = Entry(root,font="Roboto 15")

#Show into a root
title.grid(row = 0 ,column= 1)
subtitle.grid(row=1,column= 1,pady=15)
label_name.grid(row=2,column=0,pady=5)
text_name.grid(row =2,column=1)
label_level.grid(row=3,column=0)
text_level.grid(row=3,column=1)
static_button.grid(row=6, column=1,pady=20)
root.mainloop()