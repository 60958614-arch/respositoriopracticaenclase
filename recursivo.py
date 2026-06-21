from datetime import datetime 

print("\n=================== INGRESO DE DATOS ======================")
print("************** Cliente : ************")
dni = int(input("ingrese DNI del cliente :\t\t\t"))
apellido = input("Ingrese apellido del cliente :\t\t")
nombre = input("ingrese nombre del cliente:\t\t\t")
DatosCompletos = nombre + " " + apellido  

print("*************** Automovil ****************")
marca = input("Ingrese marca de automovil : \t\t")
modelo = input("ingrese modelo de automovil : \t\t")
año = int(input("Ingrese año del automovil :\t\t\t"))
preciodeventaendolares = float(input("Ingrese precio de venta en (dolares):\t"))

print("*************** Tipo de cambio  ****************")
Tipodecambio = float(input("Ingrese tipo de cambio a SOLES:\t\t"))

#calculando
MontoimpuestoDolares = preciodeventaendolares * 0.19
MontopagoDolares = preciodeventaendolares + MontoimpuestoDolares

MontoInpuestoSoles = MontoimpuestoDolares * Tipodecambio
MontoPagoSoles = MontopagoDolares * Tipodecambio

#generando el comprovante de pago 
Numcomprobante = input("ingrese el numero de comprovante : \t")
fechaAhora = datetime.now()
Año = fechaAhora.year
mes = fechaAhora.month
Dia= fechaAhora.day

print("\n====================== REPORTE DE DATOS ======================")
print("******************** Comprobante de pago ***************")
print("Numero de comprobante:\t\t",Numcomprobante)
print("Cliente DNI:\t\t\t\t", dni) 
print("cliente datos :\t\t\t\t", DatosCompletos)
print("fecha :\t\t\t\t\t",Dia,"/",mes,"/",año)
print(f"Monto a pagar (dolares) \t\t : ${MontopagoDolares:.2f} ")
print(f"Impuesto (dolares) \t\t\t : ${MontoimpuestoDolares:.2f} ")
print(f"Monto a pagar (soles) \t\t : s/{MontoPagoSoles:.2f} ")
print(f"Impuesto (soles) \t\t : s/{MontoInpuestoSoles:.2f} ")
print("Felicidades por su compra.....!")
