# Shapr3D Modeling Guide: Mac Mini M4 Enclosure

Pasos para crear el protector manualmente en Shapr3D con medidas de precisión.

## 1. Dimensiones Base
- **Mac Mini M4**: 127 x 127 x 50 mm.
- **Hub Minisopuro**: 127 x 127 x 20 mm.
- **Holgura recomendada**: +3 mm total (1.5mm por lado).

## 2. Instrucciones de Modelado
1. **Sketch**: Cuadrado de 130mm en el plano XY.
2. **Radius**: Fillet de 22mm en las esquinas.
3. **Extrude**: Hacia arriba (Eje Z) 75mm.
4. **Shell**: Grosor de 3mm (eliminar la cara superior).
5. **Front Cutout**: Rectángulo 60x15mm centrado a baja altura.
6. **Rear Cutout**: Rectángulo 110x40mm centrado para puertos principales.
7. **Side Grid**: Dibujar un hexágono de 4mm -> Linear Pattern -> Subtract.

## 3. Exportación para Impresión 3D
- Formato: **STL (High Quality)**.
- Unidades: **Millimeters (mm)**.
