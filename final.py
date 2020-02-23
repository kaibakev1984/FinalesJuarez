def leer_archivo(archivo, devolver):
	linea = archivo.readline()
	linea = linea.rstrip("\n")
	if not linea:
		linea = devolver
	return linea.split(",")

def grabar_arVentas_total(archivo, cod_art, tot_vta_S1, tot_vta_S2, tot_vta_S3):
	datos = "{}, {}, {}, {}\n".format(cod_art, tot_vta_S1, tot_vta_S2, tot_vta_S3)
	archivo.write(datos)

def grabar_arArt_sin_Ventas(archivo, cod_art, descripcion):
	datos1 = "{}, {}\n".format(cod_art, descripcion)
	archivo.write(datos1)

def grabar_arArt_Erroneos(archivo, cod_art, descripcion, mensError):
	datos2 = "{}, {}, {}\n".format(cod_art, descripcion, mensError)
	archivo.write(datos2)

def Actualizar_Vtas(arArticulos, arVtas_S1, arVtas_S2, arVtas_S3,arVTAS_TOTAL, arART_SIN_VTAS, arART_ERRONEOS):

	
	cod_artmae, descripcion = leer_archivo(arArticulos, MAXIMA+",")
	cod_art_S1, ID_vend_S1, tot_vta_S1 = leer_archivo(arVtas_S1, MAXIMA+",,")
	cod_art_S2, ID_vend_S2, tot_vta_S2 = leer_archivo(arVtas_S2, MAXIMA+",,")
	cod_art_S3, ID_vend_S3, tot_vta_S3 = leer_archivo(arVtas_S3, MAXIMA+",,")

	tot_S1 = 0
	tot_S2 = 0
	tot_S3 = 0

	while(cod_artmae != MAXIMA or cod_art_S1 != MAXIMA or cod_art_S2 != MAXIMA or cod_art_S3 != MAXIMA):
		min_cod_art = min(cod_artmae, cod_art_S1, cod_art_S2, cod_art_S3)
		print(min_cod_art)
		while(cod_artmae == min_cod_art):
			grabar_arArt_sin_Ventas(arART_SIN_VTAS, cod_artmae, descripcion)
			cod_artmae, descripcion = leer_archivo(arArticulos, MAXIMA+",")
		while(cod_art_S1 == min_cod_art):
			tot_S1 += int(tot_vta_S1)
			cod_art_S1, ID_vend_S1, tot_vta_S1 = leer_archivo(arVtas_S1, MAXIMA+",,")
		while(cod_art_S2 == min_cod_art):
			tot_S2 += int(tot_vta_S2)
			cod_art_S2, ID_vend_S2, tot_vta_S2 = leer_archivo(arVtas_S2, MAXIMA+",,")
		while(cod_art_S3 == min_cod_art):
			tot_S3 += int(tot_vta_S3)
			cod_art_S3, ID_vend_S3, tot_vta_S3 = leer_archivo(arVtas_S3, MAXIMA+",,")
		if(min_cod_art in arArticulos):
			grabar_arVentas_total(arVTAS_TOTAL, min_cod_art, str(tot_S1), str(tot_S2), str(tot_S3))
		else:
			grabar_arArt_Erroneos(arART_ERRONEOS, min_cod_art, descripcion, "El codigo de art no existe")

##########################################Bloque Principal##########################################

MAXIMA = "99999"

arArticulos = open("ARTICULOS.csv", "r")
arVtas_S1 = open("VTAS_S1.csv", "r")
arVtas_S2 = open("VTAS_S2.csv", "r")
arVtas_S3 = open("VTAS_S3.csv", "r")

arVTAS_TOTAL = open("VTAS_TOTAL.csv", "w")
arART_SIN_VTAS = open("ART_SIN_VTAS.csv", "w")
arART_ERRONEOS = open("ART_ERRONEOS.txt", "w")

Actualizar_Vtas(arArticulos, arVtas_S1, arVtas_S2, arVtas_S3,arVTAS_TOTAL, arART_SIN_VTAS, arART_ERRONEOS )
 
arArticulos.close()
arVtas_S1.close()
arVtas_S2.close()
arVtas_S3.close()

