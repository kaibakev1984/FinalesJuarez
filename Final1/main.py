MAXIMO = '999999'

def grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_maestro, descripcion):
	linea_art_sin_vtas = cod_art_maestro + "," + descripcion
	ar_art_sin_vtas.write(linea_art_sin_vtas)

def grabar_art_vtas_total(ar_vtas_total, cod_art, tot_vtas_art_s1, tot_vtas_art_s2, tot_vtas_art_s3):
	linea_vtas_total = cod_art + "," + tot_vtas_art_s1 + "," + tot_vtas_art_s2 + "," + tot_vtas_art_s3 + ","
	ar_vtas_total.write(linea_vtas_total)

def grabar_art_erroneos(ar_art_erroneos, cod_art_erroneo,  descripcion, mensaje_error):
	linea_art_erroneo = cod_art_erroneo + "," + descripcion + "," + mensaje_error
	ar_art_erroneos.write(linea_art_erroneo)

def leer_linea(archivo, devolver):
	linea = archivo.readline()
	linea.rstrip("\n")
	if not linea:
		linea = devolver
	return linea.split(",")

def cod_art_es_maximo(cod_art_maestro, cod_art_s1, cod_art_s2, cod_art_s3):
	return cod_art_maestro != MAXIMO or cod_art_s1 != MAXIMO or cod_art_s2 != MAXIMO or cod_art_s3 != MAXIMO

def actualizar_ventas(ar_articulos, ar_vtas_s1, ar_vtas_s2, ar_vtas_s3, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos):
	cod_art_maestro, descripcion = leer_linea(ar_articulos, MAXIMO + ",")
	cod_art_s1, id_vta_s1, tot_vta_s1 = leer_linea(ar_vtas_s1, MAXIMO + ",,")
	cod_art_s2, id_vta_s2, tot_vta_s2 = leer_linea(ar_vtas_s2, MAXIMO + ",,")
	cod_art_s3, id_vta_s3, tot_vta_s3 = leer_linea(ar_vtas_s3, MAXIMO + ",,")
	
	tot_vtas_s1 = tot_vtas_s2 = tot_vtas_s3 = 0
	while(cod_art_es_maximo(cod_art_maestro, cod_art_s1, cod_art_s2, cod_art_s3)):	
		min_cod_art = min(cod_art_maestro, cod_art_s1, cod_art_s2, cod_art_s3)	
		if cod_art_maestro not in [cod_art_s1, cod_art_s2, cod_art_s3]:
			grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_maestro, descripcion)
		"""	
		while min_cod_art == cod_art_maestro:
			grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_maestro, descripcion)
			cod_art_maestro, descripcion = leer_linea(ar_articulos, MAXIMO + ",")
		"""
		while cod_art_s1 == min_cod_art:
			tot_vtas_s1 += int(tot_vta_s1)
			cod_art_s1, id_vta_s1, tot_vta_s1 = leer_linea(ar_vtas_s1, MAXIMO + ",,")
		while cod_art_s2 == min_cod_art:
			tot_vtas_s2 += int(tot_vta_s2)
			cod_art_s2, id_vta_s2, tot_vta_s2 = leer_linea(ar_vtas_s2, MAXIMO + ",,")
		while cod_art_s3 == min_cod_art:
			tot_vtas_s3 += int(tot_vta_s3)
			cod_art_s3, id_vta_s3, tot_vta_s3 = leer_linea(ar_vtas_s3, MAXIMO + ",,")
		grabar_art_vtas_total(ar_vtas_total, cod_art_maestro, str(tot_vtas_s1), str(tot_vtas_s2), str(tot_vtas_s3))
		cod_art_maestro, articulo = leer_linea(ar_articulos, MAXIMO + ",")		
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
