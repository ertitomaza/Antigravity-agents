---
name: github-automator
description: Automatiza el proceso de commit y push a GitHub cuando el usuario lo solicita explícitamente usando comandos de texto.
---

# Habilidad: GitHub Automator

Esta habilidad permite realizar commits y pushes rápidos a GitHub siguiendo un formato específico solicitado por el usuario.

## Cuándo activar esta habilidad

- Cuando el usuario escriba la frase literal "push and commit" seguida de un mensaje entre paréntesis, por ejemplo: `push and commit (mensaje)`.

## Flujo de trabajo

1. **Extraer el mensaje**: Extraer el texto que se encuentra dentro de los paréntesis `()`.
2. **Preparar cambios**: Ejecutar `git add .` para añadir todos los cambios pendientes en el repositorio actual.
3. **Realizar commit**: Ejecutar `git commit -m "[mensaje extraído]"`.
4. **Push**: Ejecutar `git push`.

## Reglas

- Si la identidad de git no está configurada, usar:
  - Email: `tactica_mielina7g@icloud.com`
  - Name: `ertitomaza`
- Avisar al usuario si hay conflictos o errores durante el push.
- Proporcionar un resumen del resultado al finalizar.
