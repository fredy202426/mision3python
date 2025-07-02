import csv


ventas = {}
# Leer un CSV con encabezados
with open("datos.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        ventas[fila["Nombre"]] = {
            "enero": int(fila["Enero"]),
            "febrero": int(fila["Febrero"]),
            "marzo": int(fila["Marzo"]),
            "abril": int(fila["Abril"]),
            "mayo": int(fila["Mayo"]),
            "junio": int(fila["Junio"]),
            
        }
        
print(ventas)

import matplotlib.pyplot as plt

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]

for nombre, datos in ventas.items():
    plt.plot(meses, [datos[mes] for mes in meses], marker='o', label=nombre)

plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas por Mes")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

returnt plt
@app.get('/') 
def single_converter(): 
	# Get the matplotlib plot 
	plot = get_plot() 

	# Save the figure in the static directory 
	plot.savefig(os.path.join('static', 'images', 'plot.png')) #cambiar el nombre a la carpeta donde debe ir la img

return render_template('index.html')