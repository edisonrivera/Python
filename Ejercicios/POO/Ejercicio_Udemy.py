class Alumno: #El ejemplo no da un constructor
    def datos(self,nombre_alumno,nota_alumno):
        self.nombre_alumno = nombre_alumno
        self.nota_alumno = nota_alumno

    def condicion(self):
        if self.nombre_alumno >= 7:
            print(self.nombre_alumno, " HAS !APROBADO¡")
        else:
            print(self.nombre_alumno, " HAS DESAPROBADO")

nombre = input("Nombre del alumno: ")
nota = float(input("Nota del alumno: "))
estudiante = Alumno() #Al no exitir "__init__" no le mandamos argumentos
estudiante.datos(nota,nombre)
estudiante.condicion()