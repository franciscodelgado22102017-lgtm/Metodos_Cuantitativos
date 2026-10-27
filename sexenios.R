# Instalar los paquetes necesarios si aún no están instalados:
# install.packages("DBI")
# install.packages("RPostgres")
# install.packages("dplyr")

library(DBI)
library(RPostgres)
library(dplyr)

# 1. Configuración de parámetros de conexión a PostgreSQL
USER     <- "escuela-user"
PASSWORD <- "escuela123"
HOST     <- "localhost"
PORT     <- 5432
DB_NAME  <- "escuela_db_bk"

# 2. Crear la conexión a la base de datos
con <- dbConnect(
  RPostgres::Postgres(),
  dbname   = DB_NAME,
  host     = HOST,
  port     = PORT,
  user     = USER,
  password = PASSWORD
)

# 3. Realizar la consulta filtrada (materia_id = 5)
query <- "SELECT * FROM calificaciones WHERE materia_id = $1;"
df <- dbGetQuery(con, query, params = list(5))

# 4. Cerrar la conexión con la base de datos
dbDisconnect(con)

# 5. Asegurar que la columna calificacion sea de tipo numérico
df$calificacion <- as.numeric(df$calificacion)

# 6. Cálculo de métricas estadísticas (media, varianza y desviación estándar)
media               <- mean(df$calificacion, na.rm = TRUE)
varianza            <- var(df$calificacion, na.rm = TRUE)
desviacion_estandar <- sd(df$calificacion, na.rm = TRUE)

# 7. Mostrar resultados en consola
cat("--- Resultados Estadísticos ---\n")
cat("Media:", media, "\n")
cat("Varianza:", varianza, "\n")
cat("Desviación Estándar:", desviacion_estandar, "\n")
