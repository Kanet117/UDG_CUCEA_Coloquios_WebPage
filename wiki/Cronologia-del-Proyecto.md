# Cronologia del Proyecto

## Linea de Tiempo Ejecutiva

### Fase 1: Levantamiento de Requerimientos (Noviembre 2025)

Establecimiento del alcance del proyecto con la Dra. Karen Hernandez. Definicion de:
- Integracion con el ecosistema web oficial de CUCEA
- Stack tecnologico: Drupal 10 (CMS institucional)
- Arquitectura basada en paginas estaticas con soporte para contenido dinamico
- 7 secciones de contenido (Inicio, Comite, Conferencistas, Convocatorias, Guias, Programa, Registro)
- Plan de trabajo con cronograma de actividades

### Fase 2: Incorporacion a la Infraestructura Institucional (Diciembre 2025 - Enero 2026)

Proceso de onboarding en el ecosistema Drupal de la Universidad de Guadalajara:
- Solicitud y gestion de accesos al CMS institucional
- Coordinacion con el Centro de Tecnologias de Aprendizaje (CTA) para habilitacion de permisos
- Recepcion de credenciales y primer acceso al sistema

### Fase 3: Desarrollo e Integracion (Febrero - Abril 2026)

Implementacion de la arquitectura del sitio:
- Construccion de vistas y bloques personalizados en Drupal
- Creacion de 7 paginas de contenido
- Integracion de formularios Jotform para registro de asistentes y ponentes
- Vinculacion con Google Drive para documentos de convocatoria
- Integracion de reproductores de YouTube para transmisiones en vivo
- Auditoria de accesos y descubrimiento de limitantes en la personalizacion del tema institucional

### Fase 4: Diseno de Solucion de Contingencia (Abril - Mayo 2026)

Identificada la restriccion de personalizacion visual del tema Drupal institucional, se diseno e implemento una estrategia de mitigacion:
- Migracion de vistas dinamicas a paginas basicas estaticas con HTML/CSS/JS completo
- Implementacion de estrategias de sobrescritura de estilos del CMS (CSS Specificity Override)
- Inyeccion de dependencias CSS via bloques globales para evadir restricciones de acceso al Theme
- Construccion paralela en Flask como alternativa independiente y portable

### Fase 5: Deployment y Documentacion (Mayo - Junio 2026)

Entrega y cierre del proyecto:
- Deployment exitoso en tiempo record (1 semana para reconstruccion completa)
- Correcciones de ajuste fino solicitadas por el cliente
- Documentacion completa del proyecto (arquitectura, guias de modificacion, solucion de fallos)
- Repositorio GitHub con codigo fuente y documentacion
- Migracion a Flask como version independiente de Drupal

## Hitos Clave

| Fecha | Hito | Resultado |
|---|---|---|
| Nov 2025 | Levantamiento de requerimientos | Alcance definido y plan de trabajo entregado |
| Ene 2026 | Acceso al CMS institucional | Primer login en Drupal 10 |
| Feb 2026 | Permisos de administracion de bloques | Capacidad de modificar estructura visual |
| May 2026 | Pivote a arquitectura estatica | Sitio funcional en Drupal + version Flask |
| Jun 2026 | Entrega del proyecto | Documentacion, repositorio y sitio en produccion |

## Resumen de Tiempos

| Actividad | Duracion |
|---|---|
| Planeacion y levantamiento de requerimientos | ~1 mes |
| Onboarding y gestion de accesos institucionales | ~2 meses |
| Desarrollo e integracion | ~3 meses |
| Diseno e implementacion de estrategia de contingencia | ~1 mes |
| Ajustes finales y documentacion | ~1 mes |
| **Total** | **~8 meses** |