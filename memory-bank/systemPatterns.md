# System Patterns

## System Architecture
```
┌──────────────────────────────────────────────────────┐
│                    index.html                         │
│              (redirección → inicio.html)              │
└──────────────────────────────────────────────────────┘
                        │
    ┌───────────────────┼───────────────────┐
    ▼                   ▼                   ▼
inicio.html        comite.html        conferencistas.html
    │                   │                   │
    ├── global.css      ├── global.css      ├── global.css
    ├── inicio.css      ├── comite.css      ├── conferencistas.css
    └── main.js         └── main.js         └── main.js
    ▲                   ▲                   ▲
    └─── navbar ────────┼───────────────────┘
    └─── footer ────────┼───────────────────┘
                        │
            guias.html  │  registro.html
            ├── global.css  ├── global.css
            ├── guias.css   ├── registro.css
            └── main.js     └── main.js
```

## Key Technical Decisions

### 1. HTML Estático Puro (sin framework)
- **Razón**: Eliminar dependencia del CMS institucional y sus procesos burocráticos
- **Alternativa descartada**: Mantener en Drupal (problemas de accesos), usar Flask/Next.js (dependencias innecesarias)

### 2. CSS Organizado en 1 + N
- `global.css`: Estilos compartidos (navbar, footer, reset Drupal, tipografía base)
- `pagina.css`: Estilos específicos de cada página (acordeones, tarjetas, speakers, tablas)
- **Razón**: Separación clara de responsabilidades, facilita el mantenimiento

### 3. Navbar y Footer Copiados (no inyectados por JS)
- Navbar y footer se incluyen directamente en cada archivo HTML
- **Razón**: Cero dependencias de JavaScript para la estructura base
- **Trade-off**: Si se cambia el navbar, hay que editar 5 archivos. Aceptable para este tamaño.

### 4. Iconos SVG Inline
- **Razón**: Sin dependencias externas (no FontAwesome, no Bootstrap Icons)
- SVG pequeño para el icono de sobre (email) en el footer

## Design Patterns Used

### Layout Pattern: Full-width bands with centered content
```css
.banda {
    width: 100vw;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
}
.inner {
    max-width: 1100px;
    margin: 0 auto;
}
```
Usado en: banner principal, navbar, footer (3 bandas)

### Navigation Pattern: Flexbox navbar
- Primer elemento (CCAs) con `margin-right: auto` para empujar los demás a la derecha
- Items con `flex: 0 0 auto` para que no se estiren
- Responsive: wrap en móvil

### Content Cards Pattern
- Comité: Tarjetas con title-bar de color + descripción con borde del mismo color
- Conferencistas: Speaker cards con foto a la izquierda/derecha alternando (nth-child even)
- Guías: Caja informativa + tabla de fechas en display flex

### Accordion Pattern (Inicio)
- Checkbox oculto + label como título
- `height: 0` / `height: auto` con transición CSS
- Sin JavaScript

## Component Relationships
```
global.css
├── Reset Drupal overrides
├── Navbar styles
└── Footer styles

[Página].css (hereda de global)
├── Títulos y tipografía específica
├── Componentes de la página (cards, acordeones, etc.)
└── Media queries responsive