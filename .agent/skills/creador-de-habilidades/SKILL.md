---
name: creador-de-habilidades
description: Esta habilidad guía al agente en la creación de nuevas habilidades dentro del ecosistema de Antigravity. Debe usarse siempre que el usuario pida crear, modificar o entender cómo funcionan las habilidades.
---

# Habilidad: Creador de Habilidades

Esta habilidad define el proceso para crear nuevas capacidades para Antigravity. Las habilidades permiton extender las funciones del agente mediante instrucciones especializadas, scripts y recursos.

## Cuándo usar esta habilidad

- Cuando el usuario solicite crear una nueva "habilidad" (skill).
- Cuando sea necesario modificar una habilidad existente.
- Cuando necesites entender la estructura de archivos y metadatos de las habilidades.

## Estructura de una Habilidad

Cada habilidad debe residir en su propia carpeta dentro de:

- **Global**: `~/.gemini/antigravity/global_skills/<nombre-de-la-habilidad>/`
- **Proyecto**: `.agent/skills/<nombre-de-la-habilidad>/`

### Archivos

1. **`SKILL.md` (Obligatorio)**: El archivo principal con instrucciones. DEBE comenzar con un bloque YAML de frontmatter.
2. **`scripts/` (Opcional)**: Scripts de ayuda (Python, Bash, JS, etc.).
3. **`examples/` (Opcional)**: Ejemplos de uso para que el agente aprenda por imitación.
4. **`resources/` (Opcional)**: Plantillas, archivos JSON u otros activos.

## Creando el archivo `SKILL.md`

### 1. Frontmatter (YAML)

Todo `SKILL.md` debe empezar con:

```yaml
---
name: nombre-de-la-habilidad (opcional, por defecto el nombre de la carpeta)
description: Una descripción clara en tercera persona indicando qué hace la habilidad y cuándo activarla.
---
```

### 2. Cuerpo del Documento

Usa Markdown para detallar:

- **Objetivo**: Qué resuelve esta habilidad.
- **Flujo de trabajo**: Pasos que debe seguir el agente.
- **Uso de herramientas**: Instrucciones específicas sobre qué herramientas o scripts usar.
- **Reglas**: Restricciones o mejores prácticas.

## Mejores Prácticas

1. **Instrucciones claras**: Escribe como si estuvieras programando al agente.
2. **Usa `view_file`**: Siempre lee el archivo `SKILL.md` completo antes de empezar a usar una habilidad.
3. **No leas scripts**: Ejecuta scripts con `--help` en lugar de intentar entender su código fuente, a menos que sea estrictamente necesario para debuggear.
4. **Localización**: Si el entorno es en español, las instrucciones internas deberían favorecer ese idioma para mayor claridad con el usuario, aunque el frontmatter técnico sea estándar.

## Ejemplo de Creación Paso a Paso

1. Identificar si es una habilidad global o de proyecto.
2. Crear la carpeta con un nombre descriptivo en minúsculas y guiones.
3. Escribir el `SKILL.md` con la descripción adecuada.
4. (Opcional) Añadir scripts en `scripts/` y darles permisos de ejecución.
