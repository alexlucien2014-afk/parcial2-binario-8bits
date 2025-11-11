def to_8bit_binary(n: int) -> str:
    """
    Convierte un número entero a su representación binaria de 8 bits.
    Si es negativo, usa complemento a dos (n & 0xFF).
    """
    n8 = n & 0xFF
    return format(n8, '08b')

def main():
    print("Conversor decimal → binario de 8 bits")
    s = input("Ingresa un número (00–99 o negativo): ").strip()

    try:
        n = int(s)
    except ValueError:
        print("Error: debes ingresar un número entero.")
        return

    if not (-99 <= n <= 99):
        print("Advertencia: el programa está pensado para números de dos cifras.")
    
    bits = to_8bit_binary(n)
    print(f"Decimal: {n}  →  Binario (8 bits): {bits}")

if __name__ == "__main__":
    main()
