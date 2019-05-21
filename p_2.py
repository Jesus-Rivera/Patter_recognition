from PIL import Image,ImageDraw
import aux_pattern as ap
import math

#	Abre imagen y extrae informacion de ella
#direccion = 'prueba.jpg'
direccion = 'tornillo.jpg'
imagen = Image.open(direccion)
#imagen.show()	#Imagen original
tam = list(imagen.size)
tam[0] = tam[0]//2
tam[1] = tam[1]//2

imagen = imagen.resize((tam[0],tam[1]),Image.ANTIALIAS)


pixeles = imagen.load()
datos = imagen.getdata()


#	Aplica escala de grises a la imagen
if imagen.mode != 'L':
	imagen = imagen.convert('L')

#	Crea imagen binaria
umbral = 85#85,50
datos = imagen.getdata()
datos_binarios = []

i = 0
for i in datos:
	if i < umbral:
		datos_binarios.append(0)
		continue
	datos_binarios.append(1)

nueva_imagen = Image.new('1',imagen.size)
nueva_imagen.putdata(datos_binarios)

matriz_binaria = []
k = 0
for i in range(0,tam[1]):
	temp = []
	for j in range(0,tam[0]):
		temp.append(datos_binarios[k])
		k += 1
	matriz_binaria.append(temp)

nueva_imagen.close()
tam = list(imagen.size)
tam[0] = tam[0]//2
tam[1] = tam[1]//2
imagen = imagen.resize((tam[0],tam[1]),Image.ANTIALIAS)

figuras = ap.get_figuras(matriz_binaria)

Areas = []
i = 0
while i < len(figuras):
	temp = round((100*(len(figuras[i])/(tam[0]*tam[1]))),2)
	if temp < 1.5:
		figuras.pop(i)
	else:
		Areas.append(temp)
		i += 1

imagen = Image.open(direccion)
imagen = Image.new('RGBA',imagen.size,'black')
print("Cantidad de objetos: "+str(len(figuras)))
for i in range(0,len(figuras)):
	for j in range(0,len(figuras[i])):
		draw = ImageDraw.Draw(imagen)
		draw.ellipse([(figuras[i][j][1]*2,figuras[i][j][0]*2),(figuras[i][j][1]*2 + 3,figuras[i][j][0]*2 + 3)], fill = "yellow")
		del draw

color = ["red","blue","green","yellow","violet","cyan"]
centros = []
for i in range(0,len(figuras)):
	print("\nArea de la figura "+str(i + 1)+": "+str(Areas[i])+"%")
	Angulo_aux = 0
	Angulo = 0
	Sx = 0
	Sy = 0
	Sxx = 0
	Syy = 0
	Sxy = 0
	Mxx = 0
	Myy = 0
	Mxy = 0
	centros.append([0,0])
	for j in range(0,len(figuras[i])):
		Sx += figuras[i][j][0]
		Sy += figuras[i][j][1]
		Sxx += pow(figuras[i][j][0],2)
		Syy += pow(figuras[i][j][1],2)
		Sxy += (figuras[i][j][0]*figuras[i][j][1])
	centros[i][0] = Sx/len(figuras[i])
	centros[i][1] = Sy/len(figuras[i])
	Mxx = Sxx - (pow(Sx,2)/len(figuras[i]))
	Myy = Syy - (pow(Sy,2)/len(figuras[i]))
	Mxy = Sxy - ((Sx*Sy)/len(figuras[i]))

	Angulo_aux = ((Mxx - Myy) + math.sqrt( pow((Mxx - Myy),2) + 4*( pow(Sxy,2) )))/(2*(Mxy))
	#Angulo = round(math.atan(math.radians(Angulo_aux)))
	Angulo = (math.degrees(round(math.atan(Angulo_aux),2)))*-1
	print("Con un angulo de inclinacion de: "+str(Angulo))
	draw = ImageDraw.Draw(imagen)
	draw.ellipse([(centros[i][1]*2,centros[i][0]*2),(centros[i][1]*2 + 5,centros[i][0]*2 + 5)], fill = color[i])
	del draw


imagen.show()
imagen.close()

"""otro = 90+(math.degrees(round(math.atan(-16.8),2)))
print(otro)"""