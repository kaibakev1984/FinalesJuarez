def leer_archivo(archivo, devolver):
	linea = archivo.readline()
	if not linea:
		linea = devolver
	return linea.rstrip("\n").split(",")

def grabar_art_vtas_total(ar_vtas_total, cod_art, tot_vtas_art):
		ar_vtas_total.write(cod_art + ',' + tot_vtas_art + '\n')

def grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_sin_vtas, descripcion):
	ar_art_sin_vtas.write(cod_art_sin_vtas + ',' + descripcion + '\n')

def grabar_art_erroneos(ar_art_erroneos, cod_art_erroneo, descripcion_error):
	ar_art_erroneos.write(cod_art_erroneo + ',' + descripcion_error)

def calcular_ventas_totales(ar_articulos, ar_vtas_s1, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos):
	MAXIMO = '9999'
	cod_art_mae, descripcion = leer_archivo(ar_articulos, MAXIMO + ',')
	cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ',,')
	contador = 0	
	while(cod_art_mae != MAXIMO or cod_art_s1 != MAXIMO):
		#  Este "if" auxiliar lo uso para evitar el bucle infinito
		#  Se lo sacará una vez encontrado el problema que ocasiona..
		#  el bucle infinito
		if contador > 19:
			return
		contador += 1
		tot_vtas_art = 0
#		min_cod_art = min(cod_art_mae, cod_art_s1)
		min_cod_art = cod_art_s1  #  Es una asignación trivial. Solo cambiará cuando se encuentre el problema
		if(cod_art_mae < min_cod_art and cod_art_mae != MAXIMO):
			grabar_art_sin_vtas(ar_art_sin_vtas, cod_art_mae, descripcion)
			cod_art_mae, descripcion = leer_archivo(ar_articulos, MAXIMO + ',')
		elif cod_art_mae == min_cod_art:
			while min_cod_art == cod_art_s1:
				tot_vtas_art += int(tot_vta_s1)
				cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ',,')
			grabar_art_vtas_total(ar_vtas_total, cod_art_mae, str(tot_vtas_art))
			cod_art_mae, descripcion = leer_archivo(ar_articulos, MAXIMO + ',')
		else:
			if cod_art_mae > cod_art_s1:
				grabar_art_erroneos(ar_art_erroneos, cod_art_s1, "El codigo de Articulo no existe")
				cod_art_s1, id_vta_s1, tot_vta_s1 = leer_archivo(ar_vtas_s1, MAXIMO + ',,')

def main():
	print('Inicio Proceso')
	ar_articulos = open('articulos.csv', 'r')
	ar_vtas_s1 = open('ventas_sucursal1.csv', 'r')
	
	ar_vtas_total = open('ventas_total.csv', 'w')
	ar_art_sin_vtas = open('articulos_sin_ventas.csv', 'w')
	ar_art_erroneos = open('articulos_erroneos.txt', 'w')
	
	calcular_ventas_totales(ar_articulos, ar_vtas_s1, ar_vtas_total, ar_art_sin_vtas, ar_art_erroneos)
	
	ar_articulos.close()
	ar_vtas_s1.close()
	ar_vtas_total.close()
	ar_art_sin_vtas.close()
	ar_art_erroneos.close()
	print('Fin Proceso')
main()
