MAXIMO = '99999'
SALTO = "\n"

def grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_sin_vtas, descripcion):
	linea_art_sin_vtas = cod_art_sin_vtas + "," + descripcion + SALTO
	ar_art_sin_vtas.write(linea_art_sin_vtas)

def grabar_art_vtas_total(ar_vtas_total, cod_art, tot_vtas_art_s1, tot_vtas_art_s2, tot_vtas_art_s3):
	linea_vtas_total = cod_art + "," + tot_vtas_art_s1 + "," + tot_vtas_art_s2 + "," + tot_vtas_art_s3 + SALTO
	ar_vtas_total.write(linea_vtas_total)

def grabar_art_erroneos(ar_art_erroneos, cod_art_erroneo,  descripcion, mensaje_error):
	linea_art_erroneo = cod_art_erroneo + "," + descripcion + "," + mensaje_error
	ar_art_erroneos.write(linea_art_erroneo)

def leer_archivo(archivo, devolver):
	linea = archivo.readline()
	if not linea:
		linea = devolver
	return linea.rstrip("\n").split(",")

def actualizar_ventas(ar_articulos, ar_vtas_s1, ar_vtas_s2, ar_vtas_s3, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos):
	cod_art, descripcion = leer_archivo(ar_articulos, MAXIMO + ",")
	cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ",,")
	cod_art_s2, id_vta_s2, tot_vta_s2 = leer_archivo(ar_vtas_s2, MAXIMO + ",,")
	cod_art_s3, id_vta_s3, tot_vta_s3 = leer_archivo(ar_vtas_s3, MAXIMO + ",,")
	
	while cod_art != MAXIMO or cod_art_s1 != MAXIMO or cod_art_s2 != MAXIMO or cod_art_s3 != MAXIMO:
		acum_vtas_s1 = acum_vtas_s2 = acum_vtas_s3 = 0
		min_cod_art = min(cod_art, cod_art_s1, cod_art_s2, cod_art_s3)
		
		while min_cod_art == cod_art:
			grabar_art_sin_vtas(ar_art_sin_vtas, cod_art, descripcion)
			cod_art, descripcion = leer_archivo(ar_articulos, MAXIMO + ",")
		
		while cod_art_s1 == min_cod_art:
			acum_vtas_s1 += int(tot_vta_s1)
			cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ",,")
		
		while cod_art_s2 == min_cod_art:
			acum_vtas_s2 += int(tot_vta_s2)
			cod_art_s2, id_vta_s2, tot_vta_s2 = leer_archivo(ar_vtas_s2, MAXIMO + ",,")

		while cod_art_s3 == min_cod_art:
			acum_vtas_s3 += int(tot_vta_s3)
			cod_art_s3, id_vta_s3, tot_vta_s3 = leer_archivo(ar_vtas_s3, MAXIMO + ",,")	
		
		if min_cod_art in ar_articulos:
			grabar_art_vtas_total(ar_vtas_total, min_cod_art, str(acum_vtas_s1), str(acum_vtas_s2), str(acum_vtas_s3))
		else:
			grabar_art_erroneos(ar_art_erroneos, min_cod_art, descripcion, "El código de artículo no existe")	

def main():
	ar_articulos = open('articulos.csv', 'r')
	ar_vtas_s1 = open('ventas_sucursal1.csv', 'r')
	ar_vtas_s2 = open('ventas_sucursal2.csv', 'r')
	ar_vtas_s3 = open('ventas_sucursal3.csv', 'r')

	ar_vtas_total = open('ventas_total.csv', 'w')
	ar_art_sin_vtas = open('articulos_sin_ventas.csv', 'w')
	ar_art_erroneos = open('articulos_erroneos.txt', 'w')

	actualizar_ventas(ar_articulos, ar_vtas_s1, ar_vtas_s2, ar_vtas_s3, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos)
	
	ar_articulos.close()
	ar_vtas_s1.close()
	ar_vtas_s2.close()
	ar_vtas_s3.close()
	ar_vtas_total.close()
	ar_art_sin_vtas.close()
	ar_art_erroneos.close()

main()
