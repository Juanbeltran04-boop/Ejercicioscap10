class Symbol:
    def __init__(self, nombre):
        self.nombre = nombre

    def __eq__(self, otro):
        return isinstance(otro, type(self)) and self.nombre == otro.nombre

    def __hash__(self):
        return hash((type(self), self.nombre))

    def __repr__(self):
        return self.nombre

class Terminal(Symbol):
    pass

class NoTerminal(Symbol):
    pass

class AnalizadorSintactico:
    def __init__(self, entrada_str):
        self.entrada = [Terminal(token) for token in entrada_str.split()] + [Terminal('$')]
        self.posicion = 0
        self.token_actual = self.entrada[0] if self.entrada else Terminal('$')

    def obtener_siguiente_token(self):
        self.posicion += 1
        if self.posicion < len(self.entrada):
            self.token_actual = self.entrada[self.posicion]
        else:
            self.token_actual = Terminal('$')

    def coincidir(self, terminal_esperado):
        if self.token_actual == terminal_esperado:
            print(f"Coincide: {self.token_actual}")
            self.obtener_siguiente_token()
            return True
        else:
            return False

    def S(self):
        print("Intentando S")
        # S → ABC S'
        if self.token_actual in [Terminal('dos'), Terminal('cuatro'), Terminal('tres')]:
            self.A()
            self.B()
            self.C()
            self.S_prima()
            print("S completado con ABC S'")
            return True
        elif self.token_actual == Terminal('uno'): # Aunque S no empieza con 'uno' directamente
            # Esto es una interpretación para intentar cubrir las posibilidades
            self.A()
            self.B()
            self.C()
            self.S_prima()
            print("S completado (interpretación con uno)")
            return True
        else:
            return False

    def S_prima(self):
        print("Intentando S'")
        # S' → uno S' | ε
        if self.coincidir(Terminal('uno')):
            self.S_prima()
            print("S' completado con uno S'")
            return True
        else:
            print("S' completado con epsilon")
            return True # ε-producción

    def A(self):
        print("Intentando A")
        # A → dos BC | ε
        if self.coincidir(Terminal('dos')):
            self.B()
            self.C()
            print("A completado con dos BC")
            return True
        else:
            print("A completado con epsilon")
            return True # ε-producción

    def B(self):
        print("Intentando B")
        # B → C tres | ε
        # Priorizamos la producción con terminal 'tres'
        if self.token_actual in [Terminal('cuatro')]:
            self.C()
            if self.coincidir(Terminal('tres')):
                print("B completado con C tres")
                return True
        # Si no se cumple, intentamos la ε-producción
        print("B completado con epsilon")
        return True # ε-producción

    def C(self):
        print("Intentando C")
        # C → cuatro B | ε
        if self.coincidir(Terminal('cuatro')):
            self.B()
            print("C completado con cuatro B")
            return True
        else:
            print("C completado con epsilon")
            return True # ε-producción

if __name__ == "__main__":
    entrada_prueba = input("Ingrese la secuencia de tokens a analizar (separados por espacios): ")
    analizador = AnalizadorSintactico(entrada_prueba)
    try:
        if analizador.S() and analizador.token_actual == Terminal('$'):
            print("Análisis sintáctico exitoso.")
        else:
            print("Error: Análisis sintáctico fallido o entrada no completamente consumida.")
    except Exception as e:
        print(f"Error durante el análisis: {e}")
