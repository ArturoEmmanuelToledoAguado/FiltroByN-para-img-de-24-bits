'''
Programa que aplica un filtro binario (Blanco y negro en este caso)
a una imagen .bmp de 24 bits (no funciona para otro tipo)
'''
#Definimos los colores en notación hexadecimal RGB (BGR)
Blanco = [0xff,0xff,0xff]
Negro = [0x00,0x00,0x00]
#Abrimos la imagen a tratar y creamos la nueva imagen
file = open("volcan.bmp","rb")#Solo vamos a leer el original
fileOut = open("volcanBlancoNegro.bmp","wb")#En este escribiremos los datos modificados

file.seek(0,0)#Nos posicionamos en el primer byte
metaData = file.read(54)#Leemos los 54 bytes del metadata (0:53)

#Escribimos el metadata en el nuevo (Esto no se altera)
fileOut.write(metaData)

#Valor maximo y medio
valorMaximo = pow(2,24)#2^(24) <- 24bits
valorMedio = valorMaximo/2#Por ser un biltro binario :P

file.seek(54,0)#Nos movemos para no modificar el metaData
noPix = 0

#Leemos toda la info de los pixeles en el archivo
while(True):
    pixelData = file.read(3)
    if(len(pixelData) > 0):#Nos dice si pudimos leerlos
        #Conversion de byte a entero
        intPixel = int.from_bytes(pixelData,byteorder = 'little')
        #EL color que se asigna cuando es menor es arbitrario
        if(intPixel < valorMedio):
            fileOut.write(bytes(Blanco))#Lo escribimos en bytes
        else:
            fileOut.write(bytes(Negro))#Lo escribimos en bytes
        noPix +=1
    else:
        break
print('No Pixels: '+str(noPix))
file.close()
fileOut.close()