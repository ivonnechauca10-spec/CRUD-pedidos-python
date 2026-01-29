
import random
from prettytable import PrettyTable


detalleComprasTupla = ( [],[],[],[],[],[],[],[])

detalleCompras = list(detalleComprasTupla)

def menu() :
    print("Que accion desea realizar ")
    print('* 1) Registrar pedidos')
    print('* 2) Mostrar pedidos ')
    print('* 3) Actualizar pedido ')
    print('* 4) Eliminar pedido ')
    print('* 5) Salir del sistema ')
    return int(input("Ingrese la opcion: "))




def registrarPedidos():
    print("Ingres los datos del clinte")
    nombre= input("Nombre: ")
    apellido =input("Apellido :")
    telefono = input("Telefono:")
    print("Ingrese los datos del destinatario")
    nombreDestinatario = input("Nombre: ")
    lugarDestinatario = input("Lugar :")
    celularDestinatario = input("Celular :")


    detalleCompras[0].append(nombre)
    detalleCompras[1].append(apellido)
    detalleCompras[2].append(telefono)
    detalleCompras[3].append(nombreDestinatario)
    detalleCompras[4].append(lugarDestinatario)
    detalleCompras[5].append(celularDestinatario)
    detalleCompras[6].append(random.randint(1,1000))
    
    print("Selecciona el tipo de repartidor ")
    print('* 1) Repartidor basico ')
    print('* 2) Repartidor Premium ')
    print('* 3) Repartidor VIP ')
    opcion = int (input("Ingrese la opcion:"))
    if opcion == 1:
        detalleCompras[7].append(1.0 + (0.1*1.0))
    elif opcion == 2:
        detalleCompras[8].append(2.0 + (0.1*2.0))
    elif opcion == 3:
        detalleCompras[9].append(3.0 +( 0.1*3.0))

    print("Pedido registrado exitosamente ")



def mostrarPedidosTabla(c):
    tabla = PrettyTable()
    tabla.field_names= ["Pedido " , "Detalle"]
    tabla.align = "l"
    tabla.add_row (["Nombre cliente ", detalleCompras[0][c]])
    tabla.add_row (["Apellido cliente ", detalleCompras[1][c]])
    tabla.add_row (["Telefonocliente ", detalleCompras [2][c]])
    tabla.add_row (["Nombre destinatario " , detalleCompras[3][c]])
    tabla.add_row (["lugar stinatario " , detalleCompras[4][c]])
    tabla.add_row (["celul destinatario " , detalleCompras[5][c]])
  
    print(tabla)
  



    
                  
def mostrarPedidos(c):
    print("Datos del cliente")
    print(" \t\t  Nombre del cliente: ", detalleCompras[0][c])
    print(" \t\t  Apellido del cliente: ", detalleCompras[1][c])
    print(" \t\t Telefono del cliente: " , detalleCompras[2][c])

    print("Datos del destinatario ")
    print(" \t\t Nombre del destinaario :", detalleCompras[3][c])
    print(" \t\t Lugar destinatario :", detalleCompras[4][c])
    print(" \t\t celular destinatario :", detalleCompras[5][c])

    print("Datos del pedido ")
    print(" \n\n Codigo del pedido :", detalleCompras[6][c])
    print(" \t\t Costo del pedido:", detalleCompras[7][c])


    

def eliminarPedidos():
    print("Ingrese el codigo para eliminar el pedido")
    codigo = int(input("Codigo: "))
    if codigo in detalleCompras[6]:
        codigoFound = detalleCompras[0]. index(codigo)
        for f in range(len(detalleCompras)):
            detalleCompras[f].pop(codigoFound)
        print("Pedido eliminado con exito")
    else :
        print("El codigo no existe")





def main ():
    opcion = menu()
    while opcion !=5:
        if opcion == 1:
           registrarPedidos()
        elif opcion == 2:
           if len(detalleCompras[0]) == 0:
               print("No hay pedidos registrados ")
           else:
               for c in range(len(detalleCompras[0])):
                  mostrarPedidos(c)

        elif opcion == 3:
            print("Actualizar pedido ")
        elif opcion == 4:
            if len(detalleCompras[0] )==0:
                print("No hay pedidos registrados")
            else :
                eliminarPedidos()      
           

        opcion = menu()
        print("Muchas gracias ")
                         

main ()


    


   