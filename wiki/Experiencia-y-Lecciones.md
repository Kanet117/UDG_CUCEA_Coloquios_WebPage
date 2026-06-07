# Experiencia y Lecciones Aprendidas

## Resumen Ejecutivo

Proyecto de desarrollo del sitio web oficial del Coloquio de Cuerpos Academicos (CCAs) del CUCEA UdeG, que involucro la creacion de 7 paginas web integradas con el ecosistema Drupal 10 institucional. El proyecto enfrento restricciones de infraestructura tipicas de entornos universitarios que requirieron un diseno de estrategia de contingencia para asegurar la entrega del 100% de los requerimientos de negocio.

## Desafio

Desarrollar un sitio web institucional que cumpliera con los siguientes requerimientos:
- Integrarse al sitio oficial de CUCEA dentro del CMS Drupal 10
- Soportar 7 secciones de contenido: Inicio, Comite, Conferencistas, Convocatorias, Guias, Programa y Registro
- Incluir funcionalidades como acordeones CSS, iframes de Google Drive, reproductores de YouTube y formularios Jotform
- Ser mantenible por personal no tecnico
- Coincidir visualmente con el diseno aprobado en Google Sites

## Solucion Implementada

### Arquitectura Dual: Drupal + Flask

Se implemento una solucion de dos frentes:

**1. Version Drupal (Produccion):**
- Construccion mediante paginas basicas con HTML/CSS/JS completo, aprovechando la flexibilidad del editor de contenido de Drupal
- Estrategias de mitigacion de restricciones del CMS:
  - *CSS Specificity Override*: Uso controlado de selectores de alta especificidad para garantizar la fidelidad visual del diseno aprobado, operando dentro de las limitaciones del tema institucional
  - *Inyeccion de dependencias CSS via bloques globales*: Distribucion de estilos a traves de bloques personalizados para mantener la coherencia visual en todo el sitio sin requerir acceso al theme
  - *Redireccion programatica*: Script de redireccion para normalizar la entrada al sitio
- Diseno responsive con Flexbox y CSS Grid

**2. Version Flask (Alternativa independiente):**
- Servidor ligero en Python con 8 rutas
- Templates Jinja2 con herencia de layouts (base.html)
- CSS organizado en 8 archivos especificos por pagina
- Sin dependencias externas (no Bootstrap, jQuery o FontAwesome)
- Iconografia SVG inline

### Resultados

| Métrica | Resultado |
|---|---|
| Paginas funcionales | 7/7 |
| Tiempo de reconstruccion post-pivote | 1 semana |
| Dependencias externas | Cero |
| Documentacion | Completa (Wiki + ENTREGA_FINAL.md + Checklist) |
| Independencia de CMS | Si (version Flask portable) |

## Lecciones Aprendidas

### Gestion de Stakeholders

- **Comunicacion efectiva con perfiles no tecnicos**: Se logro traducir requerimientos de negocio (definidos en Google Sites) a especificaciones tecnicas implementables, manteniendo reuniones periodicas de alineacion con la Dra. Karen Hernandez
- **Documentacion como herramienta de gestion**: Cada solicitud, decision y cambio quedo registrado, facilitando la trazabilidad y previniendo malentendidos

### Resiliencia Tecnica

- **Adaptabilidad a infraestructura heredada**: Se navigo exitosamente un ecosistema CMS institucional con restricciones de personalizacion, entregando un producto visualmente identico al diseno aprobado
- **Pivote agil**: Cuando la arquitectura inicial (vistas dinamicas de Drupal) encontro limitaciones techniques, se diseno e implemento una solucion alternativa en tiempo record sin comprometer los requerimientos
- **Independencia tecnologica**: La construccion paralela en Flask garantiza que el sitio pueda ser deployado fuera del ecosistema Drupal si es necesario en el futuro

### Ejecucion

- **Entrega del 100% de requerimientos**: A pesar de las restricciones de infraestructura, todas las funcionalidades solicitadas fueron implementadas y desplegadas exitosamente
- **Documentacion completa**: Se entrego no solo el codigo funcional sino la documentacion necesaria para que cualquier desarrollador pueda modificar y mantener el sitio

## Alcance del Proyecto

| Aspecto | Logrado |
|---|---|
| 7 paginas funcionales | Si |
| Diseno responsive | Si |
| Sin dependencias externas | Si |
| Codigo mantenible | Si |
| Documentacion completa | Si |
| Independencia de Drupal (Flask) | Si |
| Archivos para copiar a Drupal | Si |
| Guia de modificacion | Si |
| Guia de solucion de fallos | Si |