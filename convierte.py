def InvertirString(Cadena):
    retorno = ""
    largo = len(Cadena) - 1
    while(largo >=  0):
        retorno += Cadena[largo]
        largo -= 1
    return retorno

def HelpBinary(num):
    salidaAux = ""
    cociente = int(num)
    resto = 0
    while(cociente > 0):
        resto = cociente % 2
        salidaAux += str(resto)
        cociente = cociente // 2
    salida = InvertirString(salidaAux)
    return salida

def MantraHelp(Bin):
    aux = Bin
    while(len(aux) != 23 ):
        aux += "0"
    return aux

def DecimalBinary(num):
    nom = "0." + num 

    salida = ""
    decimal = float(nom)
    entero = 0
    while(decimal != 0):
        aux  = decimal * 2
        entero = int(aux)      #transforma el resultado de la multiplicacion en entero para quedarte con el numero
        salida += str(entero)     #suma la parte entera a la salida
        decimal = aux - int(aux)    #resta el auxiliar al entero
    
    return salida

def ToBinary(Number):
    BinStr = "" #bit para signo
    act = 0  # indicador para recorrer el Number
    if Number[act] == "-":   #si el primer digito es - , el bit para el signo es 1, sino es 0
        BinStr += "1"
        act +=  1
    else:
        BinStr += "0"
        #act +=  1
    NumEntero = ""
    NumDecimal = ""
    while(Number[act] != "."):      #copia la parte entera a NumEntero
        NumEntero += Number[act]
        act += 1

    act += 1

    while(act < len(Number)):
        print(Number[act])       #copia la parte decimal a NumDecimal
        NumDecimal +=  Number[act]
        act += 1
    decimalBinary = DecimalBinary(NumDecimal)
    NumEnteroBinary = HelpBinary(NumEntero)
    E = len(NumEnteroBinary) + 127 - 1
    EBinary = HelpBinary(E)
    BinStr += EBinary
    mantra = NumEnteroBinary[1:] + decimalBinary
    mantra = MantraHelp(mantra)
    BinStr += mantra
    return BinStr   #devuelve un string



#######################################################################3

def sumaHelp(bin1 , bin2):
    suma = ''
    carry = 0 

    partes_1 = bin1.split('.')
    partes_2 = bin2.split('.')

    binario1 = partes_1[0] + partes_1[1]
    binario2 = partes_2[0] + partes_2[1]
    
    for bit_a, bit_b in zip(reversed(binario1), reversed(binario2)):
        bit_suma = int(bit_a) + int(bit_b) + carry
        suma = str(bit_suma % 2) + suma
        carry = bit_suma // 2
  
    if carry:
        suma = '1.' + suma
    else:
        suma = suma[0] + '.' + suma[1:]
    
    return suma


def BinaryDecimal(binario):
    decimal = 0
    potencia = 0
    
    # Iterar a través de los dígitos binarios en orden inverso
    for bit in reversed(binario):
        if bit == '1':
            decimal += 2 ** potencia
        potencia += 1
    
    return decimal


def sumaFloatingPoint(fpA , fpB):  
    if fpA[0] != fpB[0]:
        return 'signos distintos, no se puede efectuar suma'        
    
    resultado = 0

    signo = fpA[0]

    expSesgadoA = fpA[1:9]
    expSesgadoB = fpB[1:9]
    
    mantisaA = fpA[9:]
    mantisaB = fpB[9:]

    expA = BinaryDecimal(expSesgadoA) - 127
    expB = BinaryDecimal(expSesgadoB) - 127
    mantisaA = '1.' + mantisaA
    mantisaB = '1.' + mantisaB

    #print(mantisaA)
    #print(mantisaB)
    #print(expA)
    #print(expB)

    if expA > expB:
        #revisar si se puede usar zfill
        partes = mantisaB.split('.')
        parte_entera = partes[0]
        parte_decimal = partes[1] if len(partes) > 1 else ''
        nueva_parte_decimal = '0.'+'0' * (expA - expB - 1) + parte_entera + parte_decimal
        mantisaB = nueva_parte_decimal   
        mantisaA = mantisaA + "0"*(expA-expB)
        expB = expA

    else:
        partes = mantisaA.split('.')
        parte_entera = partes[0]
        parte_decimal = partes[1] if len(partes) > 1 else ''
        nueva_parte_decimal = '0.' +'0' * (expB-expA - 1) +parte_entera+ parte_decimal  
        mantisaA = nueva_parte_decimal
        mantisaB = mantisaB + "0"*(expB-expA)
        expA = expB


    mantisa = sumaHelp(mantisaA,mantisaB)
    mantisa = mantisa[2:]

    print('signo:' + signo)
    print('exponente:' + str(expA))
    exponente = HelpBinary(127 + expA)
    print('exponente sesgado: '+ exponente)
    print('mantisa :' + mantisa)

    resultado = signo + exponente + mantisa

    return resultado



a =  ToBinary("-110.0")
b = ToBinary("-8.625")

print(a)
print(b)

print(sumaFloatingPoint(a,b))