# Definir la función para calcular la regresión lineal
regresion_lineal <- function(x, y) {
  # Crear un data frame con los datos de entrada[cite: 1]
  datos <- data.frame(x = x, y = y)

  # Ajustar el modelo lineal utilizando lm()[cite: 1]
  modelo <- lm(y ~ x, data = datos)

  # Retornar el objeto del modelo ajustado[cite: 1]
  return(modelo)
}

# Crear los vectores x e y con los valores de ejemplo[cite: 1]
x <- c(2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
y <- c(60, 65, 70, 75, 80, 85, 90, 95, 100, 105)

# Llamar a la función y almacenar el resultado en la variable modelo[cite: 1]
modelo <- regresion_lineal(x, y)

# Ver los coeficientes básicos del modelo[cite: 1]
print(modelo)

# Opcional: mostrar un resumen estadístico detallado
summary(modelo)

