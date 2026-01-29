Normalización y Organización de las Tablas de Relación

## 1. ¿Por qué se normalizó la base de datos?
La normalización se aplicó en el sistema de Gerontología para evitar la
duplicación de datos y garantizar que cada tabla tenga una función
específica dentro de la base de datos.

En lugar de almacenar toda la información del paciente en una sola tabla,
los datos se separaron en diferentes tablas relacionadas entre sí mediante
claves foráneas.

---

## 2. Separación de la información
La tabla `personas` almacena únicamente la información básica del paciente,
mientras que la información adicional se guarda en tablas independientes.

Ejemplo de una mala práctica (NO normalizado):

```sql
personas(
  nombre,
  apellido,
  eps,
  ips,
  escolaridad,
  medicamentos,
  antecedentes
)
Ejemplo correcto (normalizado):

personas(id, nombre, apellido)
seguridad_social(id, eps, ips, fk_persona)
grado_escolaridad(id, primaria, secundaria, fk_persona)
medicamentos(id, nombre, dosis, fk_persona)
3. Uso de claves primarias y foráneas
Cada tabla tiene una clave primaria que identifica de forma única cada
registro y una clave foránea que la relaciona con la tabla personas.

Ejemplo:

CREATE TABLE seguridad_social (
    id INT PRIMARY KEY,
    eps VARCHAR(100),
    ips_atencion VARCHAR(100),
    fk_persona INT,
    FOREIGN KEY (fk_persona) REFERENCES personas(id)
);
Esto asegura que los datos de seguridad social siempre pertenezcan a una
persona existente.

4. Beneficios de la normalización
Evita información duplicada

Facilita actualizaciones

Mejora el rendimiento de consultas

Permite un mejor control de la información del paciente

5. Ejemplo de consulta con tablas normalizadas
SELECT p.nombre, s.eps, s.ips_atencion
FROM personas p
JOIN seguridad_social s ON p.id = s.fk_persona;
Esta consulta muestra cómo la información del paciente se obtiene
combinando varias tablas relacionadas.

6. Conclusión
La normalización aplicada al sistema de Gerontología permite una estructura
de datos ordenada, escalable y coherente, facilitando el manejo de la
información clínica y administrativa del paciente.
