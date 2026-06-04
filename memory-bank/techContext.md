# Tech Context

## Technologies Used
- **HTML5**: Documentos semánticos, sin frameworks
- **CSS3**: Flexbox, transitions, media queries, sin preprocesadores
- **JavaScript (vanilla)**: Mínimo, solo redirección y scripts inline
- **SVG**: Iconos inline (sobre de email)

## Development Setup
- **Editor**: Visual Studio Code
- **OS**: Linux (Ubuntu)
- **Shell**: /bin/bash
- **Git**: Control de versiones

## Technical Constraints
- Sin acceso a servidor Drupal (migración total)
- Sin dependencias externas (no CDN, no npm, no librerías)
- Sin build steps (no webpack, no sass, no postcss)
- Compatibilidad: navegadores modernos (Chrome, Firefox, Edge, Safari)
- Imágenes servidas desde Drupal (URLs remotas)

## Dependencies
- **Ninguna externa**. Cero.

## Tool Usage Patterns

### CSS Organization
```
global.css      →  Drupal overrides, navbar, footer, reset
inicio.css      →  Banner hero, acordeones, botones
comite.css      →  Tarjetas de comité con colores
conferencistas.css →  Speaker cards con fotos
guias.css       →  Cajas informativas, tablas de fechas
registro.css    →  Botones de formulario, estados disabled
```

### HTML Structure Pattern
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CCAs | [Página]</title>
    <link rel="stylesheet" href="css/global.css">
    <link rel="stylesheet" href="css/[pagina].css">
</head>
<body>
    <!-- NAVBAR (copiado en cada página) -->
    <!-- CONTENIDO ESPECÍFICO -->
    <!-- FOOTER (copiado en cada página) -->
    <script src="js/main.js"></script>
</body>
</html>
```

### Navbar Structure
```html
<nav class="navbar-ccas">
    <div class="navbar-inner">
        <ul class="navbar-nav">
            <li><a href="inicio.html" class="navbar-brand">CCAs</a></li>
            <li><a href="inicio.html">Inicio</a></li>
            <li><a href="comite.html">Comité</a></li>
            <li><a href="conferencistas.html">Conferencistas</a></li>
            <li><a href="guias.html">Guías</a></li>
            <li><a href="registro.html">Registro</a></li>
        </ul>
    </div>
</nav>
```

## Colors Reference
| Color | Uso | Hex |
|---|---|---|
| Azul marino | Navbar, títulos, fondos oscuros | #203864 |
| Rojo institucional | Títulos de página, nombres de speakers | #B22222 |
| Naranja | Acentos, fechas, algunos comités | #FF6600 |
| Azul claro | Links, botones | #2E75B6 |
| Azul acero | Bordes de tarjetas | #4975b6 |
| Teal | Fondo de tarjeta CA | #009999 |
| Gris claro | Fondo de footer bandas | #f2f2f2 |
| Amarillo | Fondo icono sobre | #ffd333 |
| Púrpura | Links de email | #330099 / #4b2c85 |

## Fonts
- Principal: "Helvetica Neue", Helvetica, Arial, sans-serif
- Navbar: 'Roboto', Arial, sans-serif
- Título footer: 'EB Garamond', serif