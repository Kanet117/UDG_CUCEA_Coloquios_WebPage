# Active Context

## Current Work Focus
Migración completa de 5 páginas Drupal a HTML/CSS/JS estático puro.

## Recent Changes
- Creación de estructura de directorios (css/, js/, memory-bank/)
- Memory Bank inicializado con projectbrief.md y productContext.md

## Next Steps
1. Completar memory-bank core (systemPatterns, techContext, progress, activeContext)
2. Crear `css/global.css` con:
   - Drupal overrides unificados (reset sidebar, breadcrumbs, listón)
   - Estilos del navbar azul
   - Estilos del footer completo
3. Crear `js/main.js` (redirección index → inicio)
4. Crear `index.html`
5. Crear cada página HTML con sus CSS correspondientes
6. Crear `.gitignore` y `README.md`

## Active Decisions
- **Sin dependencias externas**: No Bootstrap, no jQuery, no FontAwesome (iconos SVG inline)
- **CSS por página**: global.css para lo compartido + un .css por página para estilos únicos
- **Navbar inferido**: CCAs (marca) | Inicio | Comité | Conferencistas | Guías | Registro
- **Imágenes remotas**: Se mantienen las URLs originales de Drupal
- **SVG inline**: Para iconos de contacto (sobre), sin dependencias de iconos

## Important Patterns
- Fuente principal: "Helvetica Neue", Helvetica, Arial, sans-serif (ocasionalmente Roboto, Arial)
- Colores institucionales: #203864 (azul marino), #B22222 (rojo), #FF6600 (naranja), #2E75B6 (azul claro)
- Contenedor max-width: 1100px centrado
- Footer con 3 bandas: azul (institución), blanca (logos), gris (contacto + créditos)

## Known Issues
- Ninguno por ahora — migración directa de código existente

## Learnings
- Drupal forzaba IDs específicos (#liston, #navigation) que en HTML puro se simplifican a clases semánticas
- Los `!important` masivos eran necesarios en Drupal para vencer al tema; en HTML puro se reducen drásticamente