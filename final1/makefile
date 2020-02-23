CC = python3
CODEPY = main.py
ARCH_SUCURSALES = ventas_sucursal1.csv ventas_sucursal2.csv ventas_sucursal3.csv
ARCH_ARTICULOS = articulos.csv
ARCH_RES = ventas_total.csv articulos_sin_ventas.csv articulos_erroneos.txt

run: $(ARCH_SUCURSALES) $(CODEPY)
	$(CC) $(CODEPY)
del: $(ARCH_RES)
	rm -f $(ARCH_RES)
see: $(ARCH_RES)
	cat ventas_total.csv
	cat articulos_sin_ventas.csv
	cat articulos_erroneos.txt
check: $(ARCH_SUCURSALES)
	cat ventas_sucursal1.csv
	cat ventas_sucursal2.csv
	cat ventas_sucursal3.csv
art: $(ARCH_ARTICULOS)
	cat $(ARCH_ARTICULOS)

