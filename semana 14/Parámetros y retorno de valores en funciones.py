def calculara_descueto(monto_total,porcentanje_descuento=10):
    descuento =monto_total * porcentanje_descuento/100
    return descuento
monto_compra=float(input("Ingrese monto: "))
porcentaje_descuento=float(input("Ingrese descuento: "))
descuento=calculara_descueto(monto_compra,porcentaje_descuento)
total_con_descuento=monto_compra-descuento
print("\n monto del descuento",descuento)
print("monto final de pagar despues del descuento",total_con_descuento)