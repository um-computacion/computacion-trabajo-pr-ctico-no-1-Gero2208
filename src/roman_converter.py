def decimalromanos(decimal):
    conversion = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M", 4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}

    resultado = ""

    for valor, simbolo in sorted(conversion.items(), reverse=True):
        while decimal >= valor:
            resultado += simbolo
            decimal -= valor
        
    return resultado

def main():

    while True:
        decimal = int(input("Ingrese un valor decimal:"))
        print(decimalromanos(decimal))

        while True:
            reinicio = input("Desea ingresar otro número? (s/n)").lower()
            if reinicio == "s":
                break
            if reinicio == "n":
                return
            else:
                print("No ingresó una respuesta válida")

if __name__ == "__main__":
    main()