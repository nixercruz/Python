from fpdf import FPDF

proyecto = input("Ingresa la descripción del proyecto: ")
horas_estimadas = input("Ingresa las horas estimadas: ")
valor_hora = input("Ingresa el valor por hora: ")
termino = input("Ingrese el tiempo estimado de finalización: ")
valor_total = int(horas_estimadas) * int(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("soy el mejor.jpg", x=0, y=0)

pdf.text(115, 145, proyecto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, termino)
pdf.text(115, 205, str(valor_total))

pdf.output("Presupuesto.pdf")

print("¡Presupuesto generado exitosamente!")