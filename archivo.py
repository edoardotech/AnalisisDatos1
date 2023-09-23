
nombre = "jaime"
años = 42
estatura = 1.72

print(type(nombre))
print(type(años))
print(type(estatura))

mayor_edad = 18
print(años >= mayor_edad)

print(nombre + " tiene " + str(años) + " años y mide " + str(estatura))


"""En Python, los enteros no tienen un límite absoluto. Puedes tener enteros tan grandes como tu memoria permita. Sin embargo, la velocidad para realizar operaciones con números enteros aumenta a medida que los números son más pequeños. Por lo tanto, si los números enteros que estás utilizando son demasiado grandes, es posible que experimentes una disminución en el rendimiento.
En cuanto a los números de punto flotante, Python utiliza el estándar IEEE 754 para representar estos valores. Los números de punto flotante en Python se almacenan en 64 bits y siguen el formato de punto flotante de doble precisión. Esto significa que pueden representar números con hasta 15-17 dígitos decimales significativos.

Sin embargo, a medida que los números de punto flotante se vuelven más grandes o más pequeños, la precisión se pierde gradualmente. Esto se debe a que los números se almacenan en una notación científica normalizada, donde se utiliza una cantidad limitada de bits para representar la parte decimal y la parte entera del número. Por lo tanto, a medida que el número aumenta o disminuye en exponente, se pierde precisión gradualmente en la parte decimal.

Es importante tener en cuenta que Python proporciona un módulo llamado "sys" que te permite verificar los valores mínimo y máximo para los enteros y los números de punto flotante en tu sistema. Puedes usar las siguientes líneas de código:

import sys

print(sys.maxsize)  # Límite máximo para los enteros
print(sys.float_info)  # Límites para los números de punto flotante

Esto te dará información específica sobre los límites en tu sistema."""

# suma de los primeros n números pares
n = 100
print(n*(n+1)/2)
