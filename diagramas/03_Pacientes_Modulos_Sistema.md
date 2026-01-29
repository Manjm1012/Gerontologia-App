# Relación de Pacientes con los Módulos del Sistema

## 1. ¿Qué son los módulos en el sistema de Gerontología?
Los módulos representan las diferentes áreas del sistema donde se gestiona
la información del paciente, como enfermería, gerontología, medicamentos y
seguimiento clínico.

Cada módulo trabaja sobre la información del paciente, por lo que es
necesario establecer una relación clara entre ambos.

---

## 2. Relación entre pacientes y módulos
Un paciente puede estar asociado a varios módulos del sistema, y cada
módulo puede contener información de muchos pacientes.

Por esta razón, se implementa una relación **muchos a muchos (N:N)**,
resuelta mediante una tabla intermedia.

---

## 3. Estructura de tablas

### Tabla pacientes
```sql
CREATE TABLE pacientes (
    id_paciente INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_nacimiento DATE
);
Tabla modulos
CREATE TABLE modulos (
    id_modulo INT PRIMARY KEY,
    nombre_modulo VARCHAR(100),
    descripcion TEXT
);
Tabla intermedia paciente_modulo
CREATE TABLE paciente_modulo (
    id INT PRIMARY KEY,
    fk_paciente INT,
    fk_modulo INT,
    fecha_asignacion DATE,
    FOREIGN KEY (fk_paciente) REFERENCES pacientes(id_paciente),
    FOREIGN KEY (fk_modulo) REFERENCES modulos(id_modulo)
);
Esta tabla permite registrar en qué módulos se encuentra activo cada
paciente.

4. Representación en el diagrama
En el diagrama entidad-relación:

Paciente se relaciona con Paciente_Modulo (1:N)

Módulo se relaciona con Paciente_Modulo (1:N)

Paciente_Modulo actúa como tabla puente

Esto permite que el sistema sea flexible y escalable.

5. Ejemplo de asignación de un paciente a un módulo
INSERT INTO paciente_modulo (id, fk_paciente, fk_modulo, fecha_asignacion)
VALUES (1, 101, 3, '2026-01-15');
Este registro indica que el paciente con ID 101 fue asignado al módulo de
enfermería.

6. Consulta de pacientes por módulo
SELECT p.nombre, m.nombre_modulo
FROM pacientes p
JOIN paciente_modulo pm ON p.id_paciente = pm.fk_paciente
JOIN modulos m ON m.id_modulo = pm.fk_modulo;
Esta consulta permite visualizar qué pacientes están asociados a cada
módulo del sistema.

7. Conclusión
La relación entre pacientes y módulos garantiza una correcta organización
de la información y permite que cada área del sistema acceda únicamente a
los datos correspondientes al paciente.

