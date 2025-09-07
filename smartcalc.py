#toda função de conta precisa de return pois eu preciso guardar o valor para usar dps
#funçao de ler numero com tratamento de erro, ele tenta antes de agir, e se der erro da uma msg e tenta dn, QPushButton, QLineEdit, QVBoxLayout, QWidgetv
def ler_num(msg):
   while True:
    try: #ele tenta primeiro
        return float(input(msg)) #retorna um valor float para ser usado dps
    except ValueError: #impede o programa de dar erro
        print("❌ Erro: Digite um número válido!")
        return ler_num(msg)  # Tenta 
#recebe os número e faz varias contas de uma vez
def main():
    print("🧮 CALCULADORA INTELIGENTE")
    print("=" * 30)
    num1 = ler_num("Primeiro número:")
    num2 = ler_num("Segundo número:")
    print("-" * 40)
    print(f"➕ adição:{num1} + {num2} = {num1 + num2:_.1f}".replace("_", "."))
    print("-" * 40)
    print(f"➖ subtração:{num1} - {num2} = {num1-num2:_.1f}".replace("_", "."))
    print("-" * 40)
    print(f"✖️  multiplicação:{num1} x {num2} = {num1*num2:_.0f}".replace("_", "."))
    print("-" * 40)
    #divisão com proteção contra 0
    if num2 != 0:
        print(f"➗ divisão:{num1} ÷ {num2} = {num1 / num2:_.0f}".replace("_", "."))
    else:
        print("divisão:❌ Não é possivél dividir por zero!")
    print("-" * 40)
    #potência de 2
    quadrado1 = num1 * num1  # Quadrado do primeiro número
    quadrado2 = num2 * num2  # Quadrado do segundo número
    print(f"Quadrado de {num1} = {quadrado1:_.0f}".replace("_", "."))
    print(f"Quadrado de {num2} = {quadrado2:_.0f}".replace("_", "."))
    print("-" * 40)
    #calculo de porcentagem
    if num2 != 0:
        porcentagem = (num1 / num2) * 100
        print(f"💯 Porcentagem: {num1} % de {num2} = {porcentagem:.2f}")
        print("-" * 40)
    #raiz quadrada com prevenção de erro
    if num1 >= 0:
        raiz1 = num1 ** 0.5
        print(f"Raiz quadrada: √{num1} = {raiz1:.3f}")
    else:
        print(f"Raiz quadrada: √{num1} = ❌ Número negativo!")
    if num2 >= 0:
        raiz2 = num2 ** 0.5
        print(f"Raiz quadrada: √{num2} = {raiz2:.3f}")
    else:
        print(f"Raiz quadrada: √{num2} = ❌ Número negativo!")
    print("=" * 40)
main()


