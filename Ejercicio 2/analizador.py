from collections import defaultdict

# Estilos para terminal
NEGRITA = "\033[1m"
RESET = "\033[0m"

# Gramática personalizada
gramatica = {
    "S": [["A"]],
    "A": [["B", "uno"], ["dos", "C"], ["ε"]],
    "B": [["A", "tres", "B", "C"], ["cuatro"], ["ε"]],
    "C": [["siete", "A"], ["ε"]],
}

prim = defaultdict(set)
sig = defaultdict(set)
pred = {}

def es_terminal(s):
    return s not in gramatica and s != "ε"

def obtener_prim():
    actualizado = True
    while actualizado:
        actualizado = False
        for nt, alternativas in gramatica.items():
            for produccion in alternativas:
                for simbolo in produccion:
                    if simbolo == "ε":
                        if "ε" not in prim[nt]:
                            prim[nt].add("ε")
                            actualizado = True
                        break
                    elif es_terminal(simbolo):
                        if simbolo not in prim[nt]:
                            prim[nt].add(simbolo)
                            actualizado = True
                        break
                    else:
                        antes = len(prim[nt])
                        prim[nt] |= prim[simbolo] - {"ε"}
                        if "ε" in prim[simbolo]:
                            continue
                        if len(prim[nt]) > antes:
                            actualizado = True
                        break

def obtener_sig():
    sig["S"].add("$")
    cambio = True
    while cambio:
        cambio = False
        for nt, reglas in gramatica.items():
            for prod in reglas:
                for idx, simbolo in enumerate(prod):
                    if simbolo in gramatica:
                        siguiente = prod[idx + 1:]
                        temp = set()
                        nulo = False

                        for s in siguiente:
                            if s == "ε":
                                nulo = True
                                break
                            elif es_terminal(s):
                                temp.add(s)
                                break
                            else:
                                temp |= prim[s] - {"ε"}
                                if "ε" in prim[s]:
                                    continue
                                break
                        else:
                            nulo = True

                        antes = len(sig[simbolo])
                        sig[simbolo] |= temp
                        if nulo:
                            sig[simbolo] |= sig[nt]
                        if len(sig[simbolo]) > antes:
                            cambio = True

def construir_pred():
    for nt, reglas in gramatica.items():
        for regla in reglas:
            clave = f"{nt} -> {' '.join(regla)}"
            primeros = set()
            if regla == ["ε"]:
                primeros = sig[nt].copy()
            else:
                for s in regla:
                    if es_terminal(s):
                        primeros.add(s)
                        break
                    elif s == "ε":
                        primeros |= sig[nt]
                        break
                    else:
                        primeros |= prim[s] - {"ε"}
                        if "ε" in prim[s]:
                            continue
                        break
                else:
                    primeros |= sig[nt]
            pred[clave] = primeros

def verificar_ll1():
    print(f"\n{NEGRITA}== ¿ES LL(1)? =={RESET}")
    es_ll1 = True
    for nt, reglas in gramatica.items():
        conjuntos = []
        for regla in reglas:
            clave = f"{nt} -> {' '.join(regla)}"
            conjuntos.append((clave, pred[clave]))
        # Comparar conjuntos
        for i in range(len(conjuntos)):
            for j in range(i + 1, len(conjuntos)):
                inter = conjuntos[i][1] & conjuntos[j][1]
                if inter:
                    print(f"❌ Conflicto entre:\n  {conjuntos[i][0]} y\n  {conjuntos[j][0]}\n  → Intersección: {inter}")
                    es_ll1 = False
    if es_ll1:
        print("✅ La gramática ES LL(1): no hay intersección en conjuntos de predicción.")
    else:
        print("⚠️ La gramática NO es LL(1): hay intersecciones en los conjuntos de predicción.")
    return es_ll1

# Ejecutar
obtener_prim()
obtener_sig()
construir_pred()

# Mostrar
print(f"\n{NEGRITA}== PRIMEROS =={RESET}")
for nt in gramatica:
    print(f"PRIM({nt}) = {prim[nt]}")

print(f"\n{NEGRITA}== SIGUIENTES =={RESET}")
for nt in gramatica:
    print(f"SIG({nt}) = {sig[nt]}")

print(f"\n{NEGRITA}== CONJUNTOS DE PREDICCIÓN =={RESET}")
for regla, conjunto in pred.items():
    print(f"PRED({regla}) = {conjunto}")

# Verificar LL(1)
verificar_ll1()
