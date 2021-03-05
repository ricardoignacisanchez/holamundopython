import os
import struct
import binascii
import pickle


class Clientes():
    def __init__(self):
        self.code = 0
        self.name = ''
        self.apellidos = ''
        self.dni = ''
        self.edad = 0
        self.debe = 0
        self.haber = 0

    def menu(self):
        print("\033[1;32m" + "a) Dar de alta a un cliente" + "\033[;37m")
        print("\033[1;31m" + "b) Dar de baja a un cliente" + "\033[;37m")
        print("\033[1;33m" + "c) Modificar a un cliente" + "\033[;37m")
        print("\033[1;34m" +
              "d) Consultar la información de un cliente" + "\033[;37m")
        print("\033[1;35m" +
              "e) INFORME DE SITUACIÓN" + "\033[;37m")
        print()
        print("\033[4;30;46m" + "   'back' para volver al menú.'" + '\033[;37m')
        print()

    def main_menu(self):
        letra = ''

        while letra != 'exit':

            if letra == 'text':
                self.menuOp()
            elif letra == 'bin':
                self.menuOp_bin()

            print()
            print("\033[1;30;43m" + '     MENÚ PRINCIPAL     ' + "\033[;37m")
            print()
            print("\033[2;32m" + "'text' para tipo texto" + "\033[;37m")
            print("\033[2;31m" + "'bin' para tipo binario" + "\033[;37m")
            print()
            print("\033[4;30;46m" + "   'exit' para salir'" + '\033[;37m')
            print()

            letra = input('\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')

            while letra != 'text' and letra != 'bin' and letra != 'exit':
                letra = input(
                    '\033[1;31m' + 'ERROR. Introduzca text o bin >>> ' + '\033[;37m')

    def menuOp(self):
        print()
        print("\033[1;37;42m" + '    MENÚ TEXTO    ' + "\033[;37m")
        print()
        print("\033[1;32m" + "a) Dar de alta a un cliente" + "\033[;37m")
        print("\033[1;31m" + "b) Dar de baja a un cliente" + "\033[;37m")
        print("\033[1;33m" + "c) Modificar a un cliente" + "\033[;37m")
        print("\033[1;34m" +
              "d) Consultar la información de un cliente" + "\033[;37m")
        print("\033[1;35m" +
              "e) INFORME DE SITUACIÓN" + "\033[;37m")
        print()
        print("\033[4;30;46m" + "   'back' para volver al menú" + '\033[;37m')
        print()
        letra = input('\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
        self.opciones(letra)

    def menuOp_bin(self):
        print()
        print("\033[1;37;41m" + "    MENÚ BINARIO    " + "\033[;37m")
        print()
        print("\033[1;32m" + "a) Dar de alta a un cliente" + "\033[;37m")
        print("\033[1;31m" + "b) Dar de baja a un cliente" + "\033[;37m")
        print("\033[1;33m" + "c) Modificar a un cliente" + "\033[;37m")
        print("\033[1;34m" +
              "d) Consultar la información de un cliente" + "\033[;37m")
        print("\033[1;35m" +
              "e) INFORME DE SITUACIÓN" + "\033[;37m")
        print()
        print("\033[4;30;46m" + "   'back' para volver al menú" + '\033[;37m')
        print()
        letra = input('\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
        self.opciones_binario(letra)

    def opciones(self, let):
        a = Alta()
        b = Baja()
        m = Modifica()
        c = Consulta()
        i = Informe_Situacion()
        letra = let
        while letra != 'back':
            if letra == 'a':
                a.add()
                i.informe(1)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'b':
                b.disable()
                i.informe(1)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'c':
                m.modifica()
                i.informe(1)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'd':
                c.muestra()
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')

            if letra == 'e':
                i.informe(0)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')

            while letra != 'a' and letra != 'b' and letra != 'c' and letra != 'd' and letra != 'e' and letra != 'back':
                letra = input(
                    '\033[1;31m' + 'ERROR. Introduzca "a", "b", "c", "d", "e" o "back" >>> ' + '\033[;37m')

    def opciones_binario(self, let):
        ab = Alta_bin()
        bb = Baja_bin()
        mb = Modifica_bin()
        cb = Consulta_bin()
        ib = Informe_Situacion()
        letra = let
        while letra != 'back':
            if letra == 'a':
                ab.add()
                ib.informe_binario(1)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'b':
                bb.disable()
                ib.informe_binario(1)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'c':
                mb.modifica()
                ib.informe_binario(1)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'd':
                cb.muestra_bin()
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')
            if letra == 'e':
                ib.informe_binario(0)
                print()
                self.menu()
                letra = input(
                    '\033[3;35m' + '¿Qué desea hacer? >>> ' + '\033[;37m')

            while letra != 'a' and letra != 'b' and letra != 'c' and letra != 'd' and letra != 'e' and letra != 'back':
                letra = input(
                    '\033[1;31m' + 'ERROR. Introduzca "a", "b", "c", "d", "e" o "back" >>> ' + '\033[;37m')


class Informe_Situacion:
    def __init__(self):
        self.pepi = ''
        self.code = ''
        self.debemos = 0
        self.nosDeben = 0
        self.arrayDebemos = []
        self.arrayNosdeben = []
        self.totalDebemos = 0
        self.totalNosdeben = 0
        self.code_bin = ''
        self.debemos_bin = 0
        self.nosDeben_bin = 0
        self.value = []
        self.arrayDebemos_bin = []
        self.totalDebemos_bin = 0
        self.arrayNosdeben_bin = []
        self.totalNosdeben_bin = 0

    def informe_binario(self, num):
        if os.stat('bbdd_binario.txt').st_size == 0:
            print('\033[1;31m:47m' + 'EL FICHERO ESTÁ VACÍO.' + '\033[;37m')
        else:
            f = open('bbdd_binario.txt', 'rb+')

            longitud = f.readline()
            longitud_total = len(longitud)
            puntero = 58
            s = struct.Struct('3s 10s 20s 9s I f f 2s')

            f.seek(0)
            while True:
                registro = f.read(puntero)
                if registro.__len__() == 0:
                    break
                self.value = s.unpack(registro)
                self.debemos_bin = self.value[5]
                self.nosDeben_bin = self.value[6]
                activo = self.value[7].decode('UTF-8')
                if activo == 'SI':
                    # self.debemos_bin = self.debemos_bin + self.debemos_bin
                    self.arrayDebemos_bin.append(self.debemos_bin)
                    # self.nosDeben_bin = self.nosDeben_bin + self.nosDeben_bin
                    self.arrayNosdeben_bin.append(self.nosDeben_bin)
                    self.code_bin = self.value[0].decode('UTF-8')

                self.value = []

            for i in self.arrayDebemos_bin:
                self.totalDebemos_bin += i

            for i in self.arrayNosdeben_bin:
                self.totalNosdeben_bin += i

            self.arrayDebemos_bin = []
            self.arrayNosdeben_bin = []

            final = round(float(self.totalDebemos_bin - self.totalNosdeben_bin), 2)
            pepi = open('informe_bin.pic', 'wb')
            pepi.write(str('Total haber: ' + str(self.totalDebemos_bin) +
                           str(' €') + str('\n')).encode('UTF-8'))
            pepi.write(str('Total deber: ' + str(self.totalNosdeben_bin) +
                           str(' €') + str('\n')).encode('UTF-8'))
            pepi.write(str('Informe: ' + str(final) +
                           str(' €') + str('\n')).encode('UTF-8'))
            pepi.write(str('Código último cliente: ' +
                           str(self.code_bin) + str('\n')).encode('UTF-8'))

            pepi.close()
            f.close()

        if num != 0:
            self.totalDebemos_bin = 0
            self.totalNosdeben_bin = 0

        if num == 0:
            print('\033[4;31m' + 'Total deber: ' +
                  str(self.totalDebemos_bin) + str(' €') + '\033[;37m')
            print('\033[4;32m' + 'Total haber: ' +
                  str(self.totalNosdeben_bin) + str(' €') + '\033[;37m')
            if final > 0:
                print('\033[5;35m' + 'Balance: +' + str(final) + str(' €') + '\033[;37m')
            else:
                print('\033[5;35m' + 'Balance: ' + str(final) + str(' €') + '\033[;37m')

            print('\033[5;36m' + 'Código del último cliente: ' +
                  str(self.code_bin) + '\033[;37m')
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
            self.totalDebemos_bin = 0
            self.totalNosdeben_bin = 0

    def informe(self, num):

        f = open('bbdd_clientes.txt', 'r')

        f.seek(0)
        longitud = f.readlines()
        vulean = False
        if os.stat('bbdd_clientes.txt').st_size == 0:
            print('\033[1;31m:47m' + 'EL FICHERO ESTÁ VACÍO.' + '\033[;37m')
        for i in range(0, len(longitud), 1):
            encuentra = longitud[i][72:74].find('SI')
            if encuentra != -1:
                self.nosDeben = round(float(longitud[i][50:60]), 2)
                self.arrayDebemos.append(self.nosDeben)
                self.nosDeben = 0
                self.debemos = round(float(longitud[i][61:71]), 2)
                self.arrayNosdeben.append(self.debemos)
                self.debemos = 0
                self.code = longitud[i][:3]

        for i in self.arrayDebemos:
            self.totalDebemos += i

        for i in self.arrayNosdeben:
            self.totalNosdeben += i

        self.arrayDebemos = []
        self.arrayNosdeben = []
        total = self.totalDebemos - self.totalNosdeben
        fin = f'Balance: {total} €\n'

        cadena1 = '{0:12s} {1:<12.2f} {2:1s}\n'.format(
            'Total deber:', self.totalDebemos, '€')
        cadena2 = '{0:12s} {1:<12.2f} {2:1s}\n'.format(
            'Total haber:', self.totalNosdeben, '€')
        cadena3 = '{0:24s} {1:3s}\n'.format(
            'Último cliente registrado:', self.code)
        pepi = open('informe.pic', 'w+')
        pepi.write(cadena1)
        pepi.write(cadena2)
        pepi.write(fin)
        pepi.write(cadena3)
        if num == 0:
            print('\033[4;31m' + cadena1 + '\033[;37m')
            print('\033[4;32m' + cadena2 + '\033[;37m')
            print('Balance: ', total,'€')
            print('\033[5;35m' + cadena3 + '\033[;37m')
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")

        self.totalDebemos = 0
        self.totalNosdeben = 0

        pepi.close()

        f.close()


class Alta_bin:
    def __init__(self):
        self.code = ''
        self.name = ''[:10]
        self.apellidos = ''[:20]
        self.dni = ''[:9]
        self.edad = 0
        self.debe = 0
        self.haber = 0
        self.activo = 'SI'
        self.valores = []
        self.todo = []

    def incrementaCodigo_binario(self):
        f = open('bbdd_binario.txt', 'rb')
        longitud = f.readline()
        longitud = len(longitud) / 58
        f.seek(0)
        code = longitud + 1
        code = int(code)
        code = self.compruebaCodigo(code)
        f.close()
        return code

    def compruebaCodigo(self, code):
        code = str(code)
        if len(code) == 1:
            code = '00' + code
        elif len(code) == 2:
            code = '0' + code
        return code

    def validaDNI(self, numero):
        lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
        numeros = "1234567890"

        while True:

            if len(numero) == 8:
                numero = int(numero)
                letra = lista[numero % 23]
                numero = str(numero)
                final = numero + letra
                break
            else:
                numero = input(
                    '\033[2;31m' + 'Introduzca un DNI con 8 caracteres: ' + '\033[;37m')

        return final

    def validaEdad(self, edad):
        while edad < 1 or edad > 120:
            edad = int(
                input('\033[2;31m' + 'Vuelva a introducir la edad del cliente: ' + '\033[;37m'))
            continue

        return edad

    def validaCantidad(self, total):
        while total < 1 or total > 9999999:
            total = round(float(input(
                '\033[2;31m' + 'Vuelva a introducir una cantidad entre 1 y 9.999.999: ' + '\033[;37m')), 2)
        return total

    def add(self):
        f = open('bbdd_binario.txt', 'ab+')
        if os.stat('bbdd_binario.txt').st_size == 0:
            self.code = '001'
        else:
            self.code = self.incrementaCodigo_binario()

        s = struct.Struct('3s 10s 20s 9s I f f 2s')

        print(
            "\033[1;32m" + "EL CÓDIGO DEL CLIENTE ES " + self.code + "\033[;37m")

        self.name = input(
            "\033[1;32m" + "Introduce el nombre del cliente: " + "\033[;37m")

        self.apellidos = input(
            "\033[1;32m" + "Introduce los apellidos del cliente: " + "\033[;37m")

        while True:
            try:
                self.dni = input(
                    "\033[1;32m" + "Introduce el número de DNI del cliente: " + "\033[;37m")
                self.dni = self.validaDNI(self.dni)
                if len(self.dni) == 9:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.edad = int(
                    input("\033[1;32m" + "Introduce la edad del cliente: " + "\033[;37m"))
                self.edad = self.validaEdad(self.edad)
                if self.validaEdad(self.edad) < 120 or self.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.debe = round(float(input(
                    "\033[1;32m" + "Introduce la cantidad que nos debe el cliente: " + "\033[;37m")), 2)
                self.debe = self.validaCantidad(self.debe)
                if self.validaEdad(self.edad) < 120 or self.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.haber = round(float(input(
                    "\033[1;32m" + "Introduce la cantidad que debemos al cliente: " + "\033[;37m")), 2)
                self.haber = self.validaCantidad(self.haber)
                if self.validaEdad(self.edad) < 120 or self.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        self.activo = 'SI'

        # ------------------------------------------------

        self.valores.append(self.code.encode('UTF-8'))
        self.valores.append(self.name.encode('UTF-8'))
        self.valores.append(self.apellidos.encode('UTF-8'))
        self.valores.append(self.dni.encode('UTF-8'))
        self.valores.append(self.edad)
        self.valores.append(self.debe)
        self.valores.append(self.haber)
        self.valores.append(self.activo.encode('UTF-8'))

        registro = s.pack(*self.valores)

        a = f.write(registro)
        print()
        print("\033[1;32m" + "CLIENTE AÑADIDO CON ÉXITO" + "\033[;37m")
        print()
        f.close()

        self.valores = []


class Baja_bin:
    def __init__(self):
        self.activo = ''

    def compruebaCodigo(self, code):
        if len(code) == 1:
            code = '00' + code
        elif len(code) == 2:
            code = '0' + code
        return code

    def disable(self):
        f = open('bbdd_binario.txt', 'br+')
        f.seek(0)
        longitud = f.readline()
        longitud_total = len(longitud)

        print()
        codigo_cliente = input(
            '\033[3;31m' + '¿Qué cliente desea dar de baja? >>> ' + '\033[;37m')
        code = codigo_cliente
        codigo_cliente = self.compruebaCodigo(codigo_cliente)
        print()
        puntero = int(code) * 58 - 2
        f.seek(puntero)
        confirm = input('¿Está segur@ de que desea dar de baja a ese cliente? ("s" para confirmar): ')
        if confirm == 's':
            if puntero < longitud_total:
                f.write('NO'.encode('utf-8'))
                print("\033[4;31m" + 'CLIENTE ' + code +
                      " DADO DE BAJA CON ÉXITO" + "\033[;37m")
                print()
                input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
        else:
            print(f'No se ha dado de baja al cliente {codigo_cliente}')
            print('CONFIRMACIÓN REQUERIDA.')
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
            return

        if puntero > longitud_total:
            print("\033[4;31m" + "***** No se ha encontrado al cliente " +
                  code + " *****" + "\033[;37m")
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
        f.close()


class Modifica_bin:
    def __init__(self):
        self.name = ''[:10]
        self.apellidos = ''[:20]
        self.dni = ''[:9]
        self.edad = 0
        self.debe = 0
        self.haber = 0
        self.activo = ''
        self.valores = []

    def esta_activo(self, mono):
        while mono != 'SI' and mono != 'NO':
            mono = input(
                "\033[1;31m" + "ERROR!!! INTRODUZCA SI o NO >>> " + "\033[;37m")
        return mono

    def modifica(self):
        ab = Alta_bin()
        f = open('bbdd_binario.txt', 'br+')
        f.seek(0)
        longitud = f.readline()
        longitud_total = len(longitud)

        print()
        codigo_cliente = input(
            '\033[3;31m' + '¿Qué cliente desea modificar? >>> ' + '\033[;37m')
        code = codigo_cliente
        codigo_cliente = ab.compruebaCodigo(codigo_cliente)
        print()
        puntero = int(code) * 58 - 58
        f.seek(puntero)

        s = struct.Struct('3s 10s 20s 9s I f f 2s')

        self.code = codigo_cliente

        print("\033[1;32m" + "El codigo del cliente es el " + code + "\033[;37m")

        self.name = input(
            "\033[1;32m" + "Introduce el nombre del cliente: " + "\033[;37m")

        self.apellidos = input(
            "\033[1;32m" + "Introduce los apellidos del cliente: " + "\033[;37m")

        while True:
            try:
                self.dni = input(
                    "\033[1;32m" + "Introduce el número de DNI del cliente: " + "\033[;37m")
                self.dni = ab.validaDNI(self.dni)
                if len(self.dni) == 9:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.edad = int(
                    input("\033[1;32m" + "Introduce la edad del cliente: " + "\033[;37m"))
                self.edad = ab.validaEdad(self.edad)
                if ab.validaEdad(self.edad) < 120 or ab.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.debe = round(float(input(
                    "\033[1;32m" + "Introduce la cantidad que nos debe el cliente: " + "\033[;37m")), 2)
                self.debe = ab.validaCantidad(self.debe)
                if ab.validaEdad(self.edad) < 120 or ab.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.haber = round(float(input(
                    "\033[1;32m" + "Introduce la cantidad que debemos al cliente: " + "\033[;37m")), 2)
                self.haber = ab.validaCantidad(self.haber)
                if ab.validaEdad(self.edad) < 120 or ab.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        self.activo = self.esta_activo(
            input("\033[1;32m" + "¿Está activo el cliente(SI/NO)? >>> " + "\033[;37m"))

        # --------------------------------------------------------------------------------------------------------------------

        self.valores.append(self.code.encode('UTF-8'))
        self.valores.append(self.name.encode('UTF-8'))
        self.valores.append(self.apellidos.encode('UTF-8'))
        self.valores.append(self.dni.encode('UTF-8'))
        self.valores.append(self.edad)
        self.valores.append(self.debe)
        self.valores.append(self.haber)
        self.valores.append(self.activo.encode('UTF-8'))

        registro = s.pack(*self.valores)

        a = f.write(registro)
        print()
        print("\033[1;32m" + "EL CLIENTE " + code +
              " HA SIDO MODIFICADO CON ÉXITO" + "\033[;37m")
        print()
        f.close()

        self.valores = []


class Consulta_bin:
    def __init__(self):
        self.name = ''[:10]
        self.apellidos = ''[:20]
        self.dni = ''[:9]
        self.edad = 0
        self.debe = 0
        self.haber = 0
        self.activo = ''
        self.valores = []

    def muestra_bin(self):
        ab = Alta_bin()
        f = open('bbdd_binario.txt', 'br+')
        f.seek(0)
        longitud = f.readline()
        longitud_total = len(longitud)
        print()
        codigo_cliente = input(
            '\033[3;31m' + '¿Qué cliente desea mostrar? >>> ' + '\033[;37m')
        code = codigo_cliente
        codigo_cliente = ab.compruebaCodigo(codigo_cliente)
        print()
        puntero = int(code) * 58 - 58

        puntero = int(puntero)
        f.seek(puntero)

        if puntero >= longitud_total:
            print("\033[4;31m" + "***** No se ha encontrado al cliente " +
                  codigo_cliente + " *****" + "\033[;37m")
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")

        else:
            s = struct.Struct('3s 10s 20s 9s I f f 2s')
            registro = f.read(58)
            valores = s.unpack(registro)
            print("\033[3;36m" + 'Código: ' +
                  valores[0].decode('UTF-8') + "\033[;37m")
            print("\033[3;36m" + 'Nombre: ' +
                  valores[1].decode('UTF-8') + "\033[;37m")
            print("\033[3;36m" + 'Apellidos: ' +
                  valores[2].decode('UTF-8') + "\033[;37m")
            print("\033[3;36m" + 'DNI: ' +
                  valores[3].decode('UTF-8') + "\033[;37m")
            print("\033[3;36m" + 'Edad: ', valores[4], "\033[;37m")
            print("\033[3;36m" + 'Debe: ',
                  round(float(valores[5]), 2), '€' + "\033[;37m")
            print("\033[3;36m" + 'Haber: ',
                  round(float(valores[6]), 2), '€' + "\033[;37m")
            print("\033[3;36m" + '¿Está activo? ' +
                  valores[7].decode('UTF-8') + "\033[;37m")
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
            valores = []

        f.close()


class Alta:
    def __init__(self):
        self.code = 0
        self.name = ''[:10]
        self.apellidos = ''[:20]
        self.dni = ''[:9]
        self.edad = 0
        self.debe = 0
        self.haber = 0
        self.activo = 'SI'

    def validaEdad(self, edad):
        while edad < 1 or edad > 120:
            edad = int(
                input('\033[2;31m' + 'Vuelva a introducir la edad del cliente: ' + '\033[;37m'))
            continue

        return edad

    def validaCantidad(self, total):
        while total < 1 or total > 9999999:
            total = round(float(input(
                '\033[2;31m' + 'Vuelva a introducir una cantidad entre 1 y 9.999.999: ' + '\033[;37m')), 2)
        return total

    def validaDNI(self, numero):
        lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
                 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
        numeros = "1234567890"

        while True:

            if len(numero) == 8:
                numero = int(numero)
                letra = lista[numero % 23]
                numero = str(numero)
                final = numero + letra
                break
            else:
                numero = input(
                    '\033[2;31m' + 'Introduzca un DNI con 8 caracteres: ' + '\033[;37m')
        return final

    def incrementaCodigo(self):
        f = open('bbdd_clientes.txt', 'a+')
        f.seek(0)
        longitud = f.readlines()
        longitud_final = len(longitud)

        f.seek((longitud_final - 1) * 75)
        cadena = f.readline()
        code = cadena[:3]
        code = int(code)
        code += 1
        code = str(code)
        if len(code) == 1:
            code = '  ' + code
        elif len(code) == 2:
            code = ' ' + code
        code = int(code)

        f.close()
        return code

    def add(self):
        f = open('bbdd_clientes.txt', 'a+')
        if os.stat('bbdd_clientes.txt').st_size == 0:
            self.code = 1
        else:
            self.code = self.incrementaCodigo()

            print('El código de este cliente es el ', self.code)

        self.name = input(
            "\033[1;32m" + "Introduce el nombre del cliente: " + "\033[;37m")[:10]
        self.apellidos = input(
            "\033[1;32m" + "Introduce los apellidos del cliente: " + "\033[;37m")[:20]

        while True:
            try:
                numero_dni = input(
                    "\033[1;32m" + "Introduce el número de DNI del cliente: " + "\033[;37m")[:8]
                self.dni = self.validaDNI(numero_dni)
                if len(self.dni) == 9:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.edad = int(
                    input("\033[1;32m" + "Introduce la edad del cliente: " + "\033[;37m"))
                self.edad = self.validaEdad(self.edad)
                if self.validaEdad(self.edad) < 120 or self.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.debe = round(float(input(
                    "\033[1;32m" + "Introduce la cantidad que nos debe el cliente: " + "\033[;37m")), 2)
                self.debe = self.validaCantidad(self.debe)
                if self.validaEdad(self.edad) < 120 or self.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        while True:
            try:
                self.haber = round(float(input(
                    "\033[1;32m" + "Introduce la cantidad que debemos al cliente: " + "\033[;37m")), 2)
                self.haber = self.validaCantidad(self.haber)
                if self.validaEdad(self.edad) < 120 or self.validaEdad(self.edad) > 1:
                    break
            except ValueError:
                print("\033[1;31m" +
                      "ERROR! Introduzca un valor numérico." + "\033[;37m")

        cadena = '{0:3d} {1:10s} {2:20s} {3:9s} {4:3d} {5:10.2f} {6:10.2f} {7:2s}\n'.format(
            self.code, self.name, self.apellidos, self.dni, self.edad, self.debe, self.haber, self.activo)
        f.write(cadena)
        f.close()
        print()
        print("\033[1;32m" + "CLIENTE AÑADIDO CON ÉXITO" + "\033[;37m")
        print()
        print("\033[1;35m" + cadena + "\033[;37m")


class Baja:
    def __init__(self):
        self.patata = ''

    def disable(self):
        a = Alta()
        f = open('bbdd_clientes.txt', 'r+')
        print()
        codigo_cliente = input(
            '\033[3;31m' + '¿Qué cliente desea dar de baja? >>> ' + '\033[;37m')
        print()
        code = codigo_cliente
        codigo_cliente = self.compruebaCodigo(codigo_cliente)
        f.seek(0)
        longitud = f.readlines()
        puntero = 72
        vulean = False
        for i in range(0, len(longitud), 1):
            encuentra = longitud[i][:3].find(codigo_cliente)
            if encuentra != -1:
                confirm = input('¿Está segur@ de que desea dar de baja a ese cliente? ("s" para confirmar): ')
                if confirm == 's':
                    vulean = True
                    f.seek(puntero)
                    f.write('NO')
                    print("\033[4;31m" + 'CLIENTE ' + code +
                          " DADO DE BAJA CON ÉXITO" + "\033[;37m")
                    print()

                    input("\033[4;32m" +
                          "Pulse intro para mostrar el menú." + "\033[;37m")
                    break
                else:
                    print(f'No se ha dado de baja al cliente {codigo_cliente}')
                    print('CONFIRMACIÓN REQUERIDA.')
                    input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
                    return
            puntero = puntero + 75
        if vulean == False:
            print("\033[4;31m" + "***** No se ha encontrado al cliente" +
                  codigo_cliente + " *****" + "\033[;37m")
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
        f.close()

    def compruebaCodigo(self, code):
        if len(code) == 1:
            code = '  ' + code
        elif len(code) == 2:
            code = ' ' + code
        return code


class Modifica:

    def __init__(self):
        self.code = 0
        self.name = ''
        self.apellidos = ''
        self.dni = ''
        self.edad = 0
        self.debe = 0
        self.haber = 0
        self.activo = ''

    def compruebaCodigo(self, code):
        if len(code) == 1:
            code = '  ' + code
        elif len(code) == 2:
            code = ' ' + code
        return code

    def esta_activo(self, mono):
        while mono != 'SI' and mono != 'NO':
            mono = input(
                "\033[1;31m" + "ERROR!!! INTRODUZCA SI o NO >>> " + "\033[;37m")
        return mono

    def modifica(self):
        f = open('bbdd_clientes.txt', 'r+')
        print()
        codigo_cliente = input(
            '\033[3;33m' + '¿Qué cliente desea modificar? >>> ' + '\033[;37m')

        code = codigo_cliente
        codigo_cliente = self.compruebaCodigo(codigo_cliente)
        f.seek(0)
        longitud = f.readlines()
        puntero = 4
        a = Alta()

        for i in range(0, len(longitud), 1):
            encuentra = longitud[i][:3].find(codigo_cliente)
            vulean = False
            if encuentra != -1:
                vulean = True
                self.name = input(
                    "\033[1;32m" + "Introduce el nuevo nombre del cliente: " + "\033[;37m")[:10]
                self.apellidos = input(
                    "\033[1;32m" + "Introduce los nuevos apellidos del cliente: " + "\033[;37m")[:20]

                while True:
                    try:
                        numero_dni = input(
                            "\033[1;32m" + "Introduce el número de DNI del cliente: " + "\033[;37m")[:8]
                        self.dni = a.validaDNI(numero_dni)
                        if len(self.dni) == 9:
                            break
                    except ValueError:
                        print(
                            "\033[1;31m" + "ERROR! Introduzca un valor numérico." + "\033[;37m")

                while True:
                    try:
                        self.edad = int(
                            input("\033[1;32m" + "Introduce la nueva edad del cliente: " + "\033[;37m"))
                        self.edad = a.validaEdad(self.edad)
                        if a.validaEdad(self.edad) < 120 or a.validaEdad(self.edad) > 1:
                            break
                    except ValueError:
                        print(
                            "\033[1;31m" + "ERROR! Introduzca un valor numérico." + "\033[;37m")

                while True:
                    try:
                        self.debe = round(float(input(
                            "\033[1;32m" + "Introduce la cantidad que nos debe el cliente: " + "\033[;37m")), 2)
                        self.debe = a.validaCantidad(self.debe)
                        if a.validaEdad(self.edad) < 120 or a.validaEdad(self.edad) > 1:
                            break
                    except ValueError:
                        print("\033[1;31m" +
                              "ERROR! Introduzca un valor numérico." + "\033[;37m")

                while True:
                    try:
                        self.haber = round(float(input(
                            "\033[1;32m" + "Introduce la cantidad que debemos al cliente: " + "\033[;37m")), 2)
                        self.haber = a.validaCantidad(self.haber)
                        if a.validaEdad(self.edad) < 120 or a.validaEdad(self.edad) > 1:
                            break
                    except ValueError:
                        print("\033[1;31m" +
                              "ERROR! Introduzca un valor numérico." + "\033[;37m")

                self.activo = self.esta_activo(
                    input("\033[1;32m" + "¿Está activo el cliente(SI/NO)? >>> " + "\033[;37m"))

                cadena = '{0:10s} {1:20s} {2:9s} {3:3d} {4:10.2f} {5:10.2f} {6:2s}\n'.format(
                    self.name, self.apellidos, self.dni, self.edad, self.debe, self.haber, self.activo)

                f.seek(puntero)
                f.write(cadena)
                print()
                print("\033[1;32m" + "CLIENTE MODIFICADO CON ÉXITO" + "\033[;37m")
                print()
                print("\033[1;35m" + cadena + "\033[;37m")
                break

            puntero = puntero + 75
        if vulean == False:
            print()
            print("\033[4;31m" + "***** No se ha encontrado al cliente " +
                  code + " *****" + "\033[;37m")
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
        f.close()


class Consulta:
    def __init__(self):
        self.code = 0
        self.name = ''
        self.apellidos = ''
        self.dni = ''
        self.edad = 0
        self.debe = 0
        self.haber = 0
        self.activo = ''

    def muestra(self):
        m = Modifica()
        f = open('bbdd_clientes.txt', 'r')
        print()

        codigo_cliente = input(
            '\033[3;34m' + '¿Qué cliente desea mostrar? >>> ' + '\033[;37m')
        code = codigo_cliente
        print()
        codigo_cliente = m.compruebaCodigo(codigo_cliente)
        f.seek(0)
        longitud = f.readlines()
        puntero = 4
        for i in range(0, len(longitud), 1):
            encuentra = longitud[i][:3].find(codigo_cliente)
            vulean = False
            if encuentra != -1:
                print("\033[1;35m" + longitud[i] + "\033[;37m")
                vulean = True
                input("\033[4;32m" +
                      "Pulse intro para mostrar el menú." + "\033[;37m")
                break

        if vulean == False:
            print("\033[1;31m" + "***** No se ha encontrado al cliente " +
                  code + " *****" + "\033[;37m")
            print()
            input("\033[4;32m" + "Pulse intro para mostrar el menú." + "\033[;37m")
        f.close()


c = Clientes()
c.main_menu()
