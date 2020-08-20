#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
#saber cuanto deberá pagar finalmente por su compra.
class shop():
    def __init__(self):
        self.eje=tc=float(input("ingrese el valor de la compra"))
        self.eje=d=tc*0.15
        self.eje=tp=tc-d
costo = shop()
print(f"\n El total para pagar es de:$ {costo.eje:.3f}")