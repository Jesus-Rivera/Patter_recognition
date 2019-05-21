
def evaluar(adyacente,punto,grupo,fig):
	for i in range(0,len(fig)):
		if adyacente in fig[i]:
			if grupo != 0 and grupo != i:
				fig[i] = fig[i] + fig[grupo]
				fig.pop(grupo)
			else:
				fig[i].append(punto)
			break

def get_figuras(matriz_binaria):
	figuras = []
	for i in range(1,len(matriz_binaria) - 1,2):
		for j in range(1,len(matriz_binaria[i]) - 1,2):
			temp = [i,j]
			if matriz_binaria[i][j] == 1:
				bandera = 0
				grupo = 0
				if matriz_binaria[i][j - 2] == 1:
					aux = [i,j - 2]
					for k in range(0,len(figuras)):
						if aux in figuras[k]:
							figuras[k].append(temp)
							grupo = k
							break
					bandera = 1
				if matriz_binaria[i - 2][j] == 1:
					aux = [i - 2,j]
					evaluar(aux,temp,grupo,figuras)
					bandera = 1
				if matriz_binaria[i - 2][j - 2] == 1:
					aux = [i - 2,j - 2]
					evaluar(aux,temp,grupo,figuras)
					bandera = 1
				if matriz_binaria[i - 2][j + 2] == 1:
					aux = [i - 2,j + 2]
					evaluar(aux,temp,grupo,figuras)
					bandera = 1
				if bandera == 0:
					figuras.append([temp])
	return figuras