def leer_archivo(archivo, devolver):
	linea = archivo.readline()
	if not linea:
		linea = devolver
	return linea.rstrip("\n").split(",")

def grabar_art_vtas_total(ar_vtas_total, cod_art, tot_vtas_art_s1, tot_vtas_art_s2, tot_vtas_art_s3):
		ar_vtas_total.write(cod_art + ',' + tot_vtas_art_s1 + ',' + tot_vtas_art_s2 + ',' + tot_vtas_art_s3 + '\n')

def grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_sin_vtas, descripcion):
	ar_art_sin_vtas.write(cod_art_sin_vtas + ',' + descripcion + '\n')

def grabar_art_erroneos(ar_art_erroneos, cod_art_erroneo, descripcion_error):
	ar_art_erroneos.write(cod_art_erroneo + ',' + descripcion_error + '\n')

def calcular_ventas_totales(ar_articulos, ar_vtas_s1, ar_vtas_s2, ar_vtas_s3, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos):
	MAXIMO = 'ZZZZZZZ'
	cod_art_mae, descripcion = leer_archivo(ar_articulos, MAXIMO + ',')
	cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ',,')
	cod_art_s2, id_vta_s2, tot_vta_s2 = leer_archivo(ar_vtas_s2, MAXIMO + ',,')
	cod_art_s3, id_vta_s3, tot_vta_s3 = leer_archivo(ar_vtas_s3, MAXIMO + ',,')

	while(cod_art_mae != MAXIMO or cod_art_s1 != MAXIMO or cod_art_s2 != MAXIMO or cod_art_s3 != MAXIMO):
		acum_vtas_s1 = acum_vtas_s2 = acum_vtas_s3 = 0
		min_cod_art = min(cod_art_s1, cod_art_s2, cod_art_s3)
		if(cod_art_mae < min_cod_art and cod_art_mae != MAXIMO):
			grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_mae, descripcion)
			cod_art_mae, descripcion = leer_archivo(ar_articulos, MAXIMO + ',')
		elif cod_art_mae == min_cod_art:
			while min_cod_art == cod_art_s1:
				acum_vtas_s1 += int(tot_vta_s1)
				cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ',,')

			while min_cod_art == cod_art_s2:
				acum_vtas_s2 += int(tot_vta_s2)
				cod_art_s2, id_vta_s2, tot_vta_s2 = leer_archivo(ar_vtas_s2, MAXIMO + ',,')

			while min_cod_art == cod_art_s3:
				acum_vtas_s3 += int(tot_vta_s3)
				cod_art_s3, id_vta_s3, tot_vta_s3 = leer_archivo(ar_vtas_s3, MAXIMO + ',,')

			grabar_art_vtas_total(ar_vtas_total, cod_art_mae, str(acum_vtas_s1), str(acum_vtas_s2), str(acum_vtas_s3))
			cod_art_mae, descripcion = leer_archivo(ar_articulos, MAXIMO + ',')
		else:
			if cod_art_mae > cod_art_s1:
				grabar_art_erroneos(ar_art_erroneos, cod_art_s1, "El codigo de Articulo no existe")
				cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ',,')
			if cod_art_mae > cod_art_s2:
				grabar_art_erroneos(ar_art_erroneos, cod_art_s2, "El codigo de Articulo no existe")
				cod_art_s2, id_vta_s2, tot_vta_s2 = leer_archivo(ar_vtas_s2, MAXIMO + ',,')
			if cod_art_mae > cod_art_s3:
				grabar_art_erroneos(ar_art_erroneos, cod_art_s3, "El codigo de Articulo no existe")
				cod_art_s3, id_vta_s3, tot_vta_s3 = leer_archivo(ar_vtas_s3, MAXIMO + ',,')

def main():
	print('Comienzo Proceso')
	ar_articulos = open('articulos.csv', 'r')
	ar_vtas_s1 = open('ventas_sucursal1.csv', 'r')
	ar_vtas_s2 = open('ventas_sucursal2.csv', 'r')
	ar_vtas_s3 = open('ventas_sucursal3.csv', 'r')
	
	ar_vtas_total = open('ventas_total.csv', 'w')
	ar_art_sin_vtas = open('articulos_sin_ventas.csv', 'w')
	ar_art_erroneos = open('articulos_erroneos.txt', 'w')
	
	calcular_ventas_totales(ar_articulos, ar_vtas_s1, ar_vtas_s2, ar_vtas_s3, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos)
	
	ar_articulos.close()
	ar_vtas_s1.close()
	ar_vtas_s2.close()
	ar_vtas_s3.close()
	ar_vtas_total.close()
	ar_art_sin_vtas.close()
	ar_art_erroneos.close()
	print('Fin Proceso')
main()
