# Modelo de Datos y Tablas de Relación – Sistema de Gerontología

## 1. Introducción
El modelo de datos del sistema de Gerontología fue diseñado para organizar
de manera estructurada la información de los pacientes, permitiendo
almacenar datos personales, clínicos, sociales y administrativos de forma
segura y coherente.

El diseño se basa en un modelo relacional, utilizando claves primarias y
claves foráneas para conectar las tablas y garantizar la integridad de los
datos dentro del sistema.

---

## 2. Estructura general del modelo
La base de datos está compuesta por varias tablas especializadas que cumplen
una función específica. La tabla principal del sistema es `personas`, ya que
representa a cada paciente o usuario registrado.

A partir de esta tabla se relacionan las demás entidades, permitiendo
centralizar la información sin duplicarla.

---

## 3. Tabla principal: personas
La tabla `personas` almacena la información básica del paciente, como
nombres, apellidos, datos de contacto y fecha de nacimiento.

Ejemplo de estructura:

```sql
CREATE TABLE personas (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    primer_apellido VARCHAR(100),
    segundo_apellido VARCHAR(100),
    celular VARCHAR(15),
    correo VARCHAR(150),
    ciudad VARCHAR(80),
    direccion VARCHAR(150),
    sexo VARCHAR(20),
    fecha_nacimiento DATE
);
Esta tabla funciona como el núcleo del sistema, ya que la mayoría de las
tablas dependen de ella.

4. Tablas relacionadas al paciente

Las tablas clínicas y sociales no se almacenan directamente en personas,
sino que se separan para mantener la normalización de la base de datos.

Ejemplos de tablas relacionadas:

grado_escolaridad

seguridad_social

datos_socioeconomicos

medicamentos

antecedentes_toxicos

Ejemplo de relación con medicamentos:

CREATE TABLE medicamentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    dosis VARCHAR(50),
    frecuencia VARCHAR(50),
    alergia BOOLEAN,
    fk_persona INT
);

ALTER TABLE medicamentos
ADD CONSTRAINT fk_medicamentos_persona
FOREIGN KEY (fk_persona) REFERENCES personas(id);


Esto permite que una persona tenga registrados uno o varios medicamentos.

5. Tipo de relaciones utilizadas

El sistema utiliza principalmente relaciones uno a muchos (1:N),
donde una persona puede tener múltiples registros asociados.

Ejemplo:

Una persona → muchos medicamentos

Una persona → varias adversidades

Una persona → múltiples antecedentes

Este enfoque facilita el crecimiento del sistema y la correcta organización
de la información.

6. Ventajas del modelo de datos

Evita duplicación de información

Facilita el mantenimiento de la base de datos

Permite consultas más eficientes

Garantiza integridad referencial

Mejora la escalabilidad del sistema

7. Ejemplo de consulta utilizando relaciones
SELECT p.nombre, p.primer_apellido, m.nombre AS medicamento
FROM personas p
JOIN medicamentos m ON p.id = m.fk_persona;


Esta consulta permite obtener los medicamentos asociados a cada paciente,
demostrando el uso práctico de las relaciones entre tablas.

8. Conclusión

El modelo de datos del sistema de Gerontología está diseñado para soportar
la gestión integral de la información del paciente, permitiendo un manejo
ordenado, escalable y confiable de los datos dentro de la aplicación.
