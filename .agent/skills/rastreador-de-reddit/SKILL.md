---
name: rastreador-de-reddit
description: Esta habilidad permite al agente rastrear y extraer las mejores publicaciones de un subreddit específico utilizando el subagente de navegación. Debe activarse cuando el usuario pida resúmenes o las publicaciones más populares de Reddit.
---

# Habilidad: Rastreador de Reddit

Esta habilidad automatiza la extracción de información de Reddit para obtener las publicaciones más populares de cualquier comunidad (subreddit).

## Cuándo usar esta habilidad

- Cuando el usuario solicita: "¿Cuáles son los mejores posts de r/tecnologia esta semana?"
- Cuando se requiere un resumen de las tendencias en un subreddit particular.
- Cuando necesites obtener enlaces o títulos de publicaciones destacadas de Reddit.

## Flujo de Trabajo

### 1. Preparación del Usuario

Antes de empezar, asegúrate de tener el nombre del subreddit. Si el usuario no lo proporciona, pregúntale.

### 2. Navegación y Extracción

Debes delegar la tarea al `browser_subagent` con las siguientes instrucciones específicas:

**Instrucción para el subagente:**

1. Navega a la URL: `https://www.reddit.com/r/<SUBREDDIT>/top/?t=week` (sustituye `<SUBREDDIT>` por el nombre real).
2. Si aparece un pop-up de cookies o de "uso de la app", intenta cerrarlo o ignorarlo.
3. Identifica los elementos de las publicaciones. Busca títulos, enlaces y, si es posible, la puntuación (upvotes).
4. Extrae los datos de las primeras 5 a 10 publicaciones.
5. Devuelve una lista estructurada con:
   - Título de la publicación.
   - Enlace (URL).
   - Número de upvotes (si se encontró).

### 3. Formateo de Resultados

Una vez que el subagente devuelva la información, preséntala al usuario en un formato limpio:

| Puesto | Título                 | Upvotes | Enlace          |
| :----- | :--------------------- | :------ | :-------------- |
| 1      | [Título del Post](URL) | 1.2k    | [Ver post](URL) |
| ...    | ...                    | ...     | ...             |

## Reglas y Restricciones

- **No intentes iniciar sesión**: Reddit funciona bien para lectura pública sin cuenta.
- **Límite de publicaciones**: No excedas las 10 publicaciones a menos que el usuario lo pida explícitamente.
- **Manejo de errores**: Si el subreddit no existe o es privado, informa al usuario claramente.

## Ejemplo de Prompt para el Subagente

"Navega a reddit.com/r/learnjavascript/top/?t=week y extrae el título y la URL de los 5 posts más populares de esta semana. Ignora cualquier anuncio."
