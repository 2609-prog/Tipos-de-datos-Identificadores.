# Autor: Lisseth  Puco
# Programa para calcular el área de un triangulo a partir de la base y la altura ingresadas por el usuario
# Se utilizan tipos de datos: float, int, string y boolean.
# El resultado se muestra con dos decimales.



def calcular_area_triangulo(base, altura):
    """Calcula el área de un triangulo usando la fórmula: (base * altura) / 2"""
    area = (base * altura) / 2
    return area

# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ") # String
print(f"Hola, {nombre_usuario}. Vamos a calcular el área de un triangulo.")


base_triangulo = float(input("Ingrese la base del triangulo en cm: "))  # float
altura_triangulo = float(input("Ingrese la altura del triangulo en cm: "))  # float


# Cálculo del área
area_resultado = calcular_area_triangulo(base_triangulo, altura_triangulo)

# Mostrar resultado
print(f"{nombre_usuario}, el área del triangulo es: {area_resultado:.2f} cm²")


# Verificacion (boolean)
es_mayor_que_diez = area_resultado > 10 #boolean
print(f"¿El área es mayor que 10 cm²? {es_mayor_que_diez}")
