# Progress

## What Works
- **5 páginas HTML completas**: inicio, comite, conferencistas, guias, registro
- **index.html** con redirección automática a inicio.html
- **Navbar** funcional en todas las páginas con enlaces relativos y clase `.active` en la página actual
- **Footer** idéntico en todas las páginas (3 bandas: azul, blanca con logos, gris con contacto)
- **CSS organizado**: global.css (compartido) + 1 CSS por página
- **Acordeones** en Inicio (funcionan con checkbox CSS, sin JS)
- **Speaker cards** en Conferencistas con layout alternante (imagen izq/der)
- **Tarjetas de comité** con header de color y borde del mismo color
- **Cajas informativas + tablas de fechas** en Guías
- **Botones de registro** con estados disabled
- **Memory Bank** completo (6 archivos core)

## What's Left to Build
- Nada — proyecto completo.

## Current Status
**COMPLETED** — Todos los archivos HTML, CSS, JS, templates, memory-bank, .gitignore, README.md, wiki/Home.md y LICENSE están creados.

## Known Issues
- Ninguno conocido. Todo migrado del Drupal original. El proyecto es estático con Flask para desarrollo local y template inheritance.

## Evolution of Project Decisions
1. **Drupal → HTML estático**: Decisión forzada por burocracia de accesos (~3 meses para primer acceso, accesos CSS incompletos después de 4 meses)
2. **Sin JS para navbar/footer**: Se optó por HTML directo en cada página para simplicidad y cero dependencias
3. **CSS por página**: Se prefirió sobre un solo CSS gigante para mejor organización y mantenimiento
4. **Imágenes remotas**: Se mantienen las URLs de Drupal para no duplicar assets
5. **Sin preprocesadores**: CSS plano, sin SASS, sin build steps