# Integridad Referencial y Control de Datos del Paciente

## 1. ¿Qué es la integridad referencial?
La integridad referencial es el mecanismo que garantiza que las relaciones
entre las tablas de la base de datos sean válidas y coherentes.

En el sistema de Gerontología, este concepto es esencial para asegurar que
los registros asociados a un paciente no queden huérfanos ni inconsistentes.

---

## 2. Uso de claves foráneas
Las claves foráneas permiten relacionar las tablas secundarias con la tabla
principal de pacientes (`personas`).

Ejemplo:

```sql
CREATE TABLE adversidades (
    id INT PRIMARY KEY,
    tipo_adversidad VARCHAR(100),
    descripcion VARCHAR(255),
    fk_persona INT,
    FOREIGN KEY (fk_persona) REFERENCES personas(id)
);
Gracias a esta relación, no es posible registrar una adversidad sin que
exista previamente un paciente.

3. Control de inserción de datos
La integridad referencial evita errores como:

Registrar medicamentos para un paciente inexistente

Crear historias clínicas sin identificación válida

Asociar módulos a personas no registradas

Ejemplo de inserción correcta:

INSERT INTO personas (id, nombre, primer_apellido)
VALUES (10, 'Ana', 'Gómez');

INSERT INTO medicamentos (id, nombre, dosis, fk_persona)
VALUES (1, 'Acetaminofén', '500mg', 10);
Ejemplo de inserción incorrecta (rechazada por el sistema):

INSERT INTO medicamentos (id, nombre, dosis, fk_persona)
VALUES (2, 'Ibuprofeno', '400mg', 99);
4. Reglas de eliminación y actualización
Para proteger la información del paciente, se definen reglas al eliminar o
actualizar registros.

Ejemplo:

FOREIGN KEY (fk_persona)
REFERENCES personas(id)
ON DELETE CASCADE
ON UPDATE CASCADE;
Esto permite que, si un paciente se elimina, sus registros relacionados
también se eliminen automáticamente.

5. Validación del flujo del sistema
Gracias a la integridad referencial:

El sistema mantiene consistencia en los datos

Se evita pérdida de información

Se facilita el mantenimiento de la base de datos

Se asegura trazabilidad del paciente

6. Relación con el diagrama entidad–relación
En el diagrama ER, la integridad referencial se representa mediante líneas
que conectan las claves foráneas con las claves primarias, indicando una
dependencia directa entre las tablas.

Esto permite visualizar claramente cómo fluye la información del paciente
en el sistema.

7. Conclusión
La integridad referencial es un pilar fundamental del sistema de
Gerontología, ya que garantiza que la información del paciente sea confiable,
segura y correctamente relacionada entre todos los módulos y tablas.
