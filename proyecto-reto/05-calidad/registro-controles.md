# Registro de controles de calidad

Responsable de calidad del equipo: **Rodrigo Herrera** (firma las hojas viajeras).
Actualizado: 2026-10-10.

## Controles realizados

| Fecha | Control | Tipo | Sobre qué | Resultado | Evidencia |
|---|---|---|---|---|---|
| 2026-09-30 | Simulación CAM de las 5 piezas del brazo | Prevención (antes de maquinar) | OF-2026-BRZ-001…005 | 0 colisiones | `04-manufactura/cam-brazo/README.md` |
| 2026-10-01 | FEA de la rueda mecanum V6 (estática, torsión y combinada) | Validación de diseño | Rueda mecanum | Hub con cople de acero: FS 3.9 a carga de diseño (482 N). Punto débil: unión entre capas del PETG (FS ≈ 1.2–1.4 en operación) | `04-fabricacion/simulacion/rueda-mecanum-simulacion-fea.md` |
| 2026-10-03 | Procedimiento de impresión de rodillos en TPU 95A | Control de proceso | Rodillos mecanum (48 + repuestos) | Orientación vertical sin soportes en la banda de rodadura | `04-fabricacion/impresion-rodillos-tpu.md` |
| 2026-10-03 | Validación eléctrica NXP ↔ RoboClaw | Prueba funcional | Motor del AGV + batería | Telemetría válida a 23.6 V. Velocidad hasta 5050 qpps | `08-software/control/ensayos/2026-10-03-laboratorio-nxp/` |
| 2026-10-06 | Holguras aplicadas al CAD V6 | Diseño para manufactura | Hub y cubiertas | Ensamble reconstruye con 0 errores | `04-fabricacion/banco-tolerancias.md` |
| 2026-10 | **Banco de tolerancias PETG impreso** | Inspección de proceso (impresión 3D) | Hexágono, cuello del hub, M5, ejes 1/4 in | ⏳ Impreso. **Falta registrar qué medida pasó en cada fila** | `04-fabricacion/banco-tolerancias.md` |

## Controles pendientes (abiertos)

| Control | Sobre qué | Por qué falta |
|---|---|---|
| Inspección dimensional contra plano (contorno, barrenos, bolsa) | 5 piezas del brazo (OF-BRZ-001…005) | Las piezas se maquinaron, pero no hay medición registrada |
| Escuadra, diagonales y planitud | Chasis soldado (OF-AGV-002) | Fabricado del 2026-10-05 al 2026-10-08, sin inspección registrada |
| Cupón TPU (contraalojamiento del buje) | Rodillos | No se ha impreso |
| Conteo de piezas buenas y scrap, y firma | Las 6 OF fabricadas | Las hojas viajeras tienen el operador y las fechas, pero no la firma |
| Identificación física de piezas | Todas | Las piezas no tienen marca. Propuesta: grabar o etiquetar el número de OF |
