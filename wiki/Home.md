# Coloquio de Cuerpos Académicos (CCAs) — Historia del proyecto

## Contexto y origen

El sitio web del Coloquio de Cuerpos Académicos (CCAs) nació como un proyecto del Centro Universitario de Ciencias Económico Administrativas (CUCEA) de la Universidad de Guadalajara. El objetivo era crear un espacio digital para difundir y divulgar los trabajos de investigación de los Cuerpos Académicos de la institución, permitiendo la colaboración nacional e internacional entre investigadores.

Inicialmente, el sitio fue implementado en Drupal, el CMS institucional de la UdeG.

## El problema de los accesos (4 meses de espera)

El desarrollo en Drupal se enfrentó a un problema crítico: la burocracia administrativa. Desde la solicitud inicial, pasaron aproximadamente **tres meses** para obtener el primer acceso al proyecto. Pero los problemas no terminaron ahí — los accesos para modificar CSS y personalizar la apariencia del sitio seguían **incompletos después de cuatro meses**.

Esta situación hacía imposible:
- Personalizar el diseño más allá del tema base de Drupal
- Eliminar elementos forzados como sidebar, breadcrumbs y el listón institucional de la UdeG
- Hacer cambios rápidos sin depender de procesos administrativos lentos
- Trabajar con un flujo de desarrollo ágil

## Primera fase: proyecto dinámico con Flask

Ante la imposibilidad de trabajar efectivamente en Drupal, se tomó la decisión de crear un **proyecto paralelo en Flask** (Python). Esto permitió:

- Tener libertad total sobre el diseño y la estructura del sitio
- Trabajar con un flujo de desarrollo local sin depender de permisos institucionales
- Usar Jinja2 templates para mantener navbar, footer y layout compartido
- Servir el sitio mientras se resolvían los problemas de acceso a Drupal

Durante esta fase, el sitio se mantuvo como página dinámica con Flask, a la espera de poder migrar el contenido a Drupal cuando llegaran los accesos completos.

## La decisión del cambio a estático

Los accesos nunca llegaron a ser completos. Después de meses de espera, se tomó una decisión estratégica: **abandonar Drupal por completo** y migrar a HTML/CSS/JS puro.

Las razones fueron claras:

1. **Independencia tecnológica**: No depender de permisos Drupal, módulos o configuraciones del CMS institucional.
2. **Despliegue simple**: Hosting estático sin servidor, sin PHP, sin base de datos.
3. **Mantenibilidad**: Código plano que cualquier desarrollador pueda entender y modificar.

Sin embargo, el proyecto mantuvo Flask como servidor de desarrollo local con template inheritance (`{% extends "base.html" %}`), lo que permitió mantener navbar, footer y layout en un solo archivo (`base.html`) en lugar de copiarlos en cada página.

## Réplica exacta del diseño

El objetivo principal fue replicar visualmente cada página del sitio Drupal original. A continuación, cómo se abordó cada componente:

### Navbar institucional

El navbar azul marino (#203864) fue el elemento más desafiante de replicar en Drupal debido a los !important necesarios para vencer el tema base. En la versión final:

- Primer elemento (CCAs) con `margin-right: auto` para empujar los demás a la derecha
- Flexbox con `flex: 0 0 auto` para que los items no se estiren
- Efecto hover con text-shadow blanco
- Orden: CCAs | Inicio | Convocatorias | Comité | Guías | Registro | Programa | Conferencistas

### Footer de 3 bandas

El footer se compone de tres bandas de ancho completo:

1. **Banda azul**: "Instituciones participantes" centrado
2. **Banda blanca**: Logos de todas las instituciones participantes (imagen remota desde Drupal)
3. **Banda gris**: Distribución en 3 columnas con CSS Grid:
   - Izquierda: Correo de contacto con icono SVG inline (sobre)
   - Centro: Título del coloquio en tipografía EB Garamond
   - Derecha: Créditos del equipo en formato grid `auto 1fr` para alineación perfecta

### Tarjetas de comité

Cada Cuerpo Académico se representa con una tarjeta de dos partes:
- **Title-bar** con color distintivo del CA (naranja, teal, azul acero, azul marino)
- **Descripción** con borde del mismo color que el title-bar

Los colores ayudan a identificar rápidamente los diferentes grupos participantes.

### Speaker cards (Conferencistas)

Las conferencias plenarias se muestran con un diseño alternante:
- Speaker impar: foto a la izquierda, información a la derecha
- Speaker par: foto a la derecha, información a la izquierda (nth-child even)
- Foto de 220px de ancho fijo
- Nombre en rojo institucional (#B22222), título de charla en azul marino, fecha en naranja

### Acordeones CSS puro (Inicio)

Los acordeones de Objetivos y Eventos anteriores funcionan sin JavaScript:
- Checkbox oculto + label como título clickeable
- `height: 0` / `height: auto` con transición CSS
- `:checked` selector para mostrar el contenido

### Tablas de fechas (Guías)

Las fechas importantes se muestran en bloques de color (naranja para ponencias, azul marino para publicaciones) con formato visual claro utilizando flexbox para la disposición lado a lado.

### Convocatorias

Grid de 3 columnas con fondo azul marino y naranja para las fechas clave, y cajas con borde naranja para la información detallada.

### Programa

Botones de enlace a YouTube por cada día del evento, diseño responsivo con imágenes del programa en flexbox.

### Registro

Botones de formulario Jotform con diseño institucional y estados disabled cuando las fechas aún no están abiertas.

## Template inheritance con Jinja2

Un aspecto clave de la arquitectura final fue el uso de `{% extends "base.html" %}` de Jinja2 para evitar duplicar código. El archivo `base.html` contiene:

- `<head>` completo con etiquetas meta, viewport y CSS global
- Navbar con detección automática de página activa (variable `active_page`)
- Footer completo con créditos y contacto
- Script de JavaScript

Cada página solo define:
- `{% block page_title %}` para el título de la pestaña
- `{% block page_css %}` para su CSS específico
- `{% block content %}` para su contenido único

Esto redujo cada template de ~120-170 líneas a ~10-20 líneas de contenido real.

## Lecciones aprendidas

### CSS Grid vs Flexbox para alineación

Inicialmente se usó Flexbox con `justify-content: flex-end` para los créditos del footer, pero esto creaba un efecto "escalera" donde labels y nombres no se alineaban verticalmente. La solución fue usar **CSS Grid** con `grid-template-columns: auto 1fr`, que alinea labels a la derecha y nombres a la izquierda en columnas perfectas sin importar el largo del texto.

### La importancia de zero dependencies

Al no usar Bootstrap, jQuery, ni FontAwesome, el sitio carga instantáneamente incluso en conexiones lentas. Los iconos SVG inline para el sobre de correo eliminan la necesidad de cargar librerías de iconos.

### Drupal overrides vs HTML puro

En Drupal, los `!important` masivos eran necesarios para vencer la especificidad del tema base. En HTML puro, los estilos se simplifican drásticamente — un reset básico y estilos directos sin necesidad de anular nada.

## Resultado final

El sitio final es exactamente como se quería desde el principio:

- **7 páginas HTML** con navegación fluida entre ellas
- **Diseño responsive** que funciona en cualquier dispositivo
- **Cero dependencias externas** — ni frameworks, ni librerías, ni build tools
- **Código mantenible** con template inheritance y CSS organizado por página
- **Sin burocracia** — cualquier cambio se hace en segundos, editando archivos HTML/CSS directamente

## Créditos del proyecto

| Rol | Persona |
|------|---------|
| Contenido | Dra. Karen Hernández |
| Desarrollo | Jesús A. García Pérez |
| Frontend | Kanet Sahid Ochoa Guzmán |
| Web | Ángela Jusuneith Silva Ramírez |

## Tecnologías usadas

- **Flask 3.x** con Jinja2 (servidor de desarrollo)
- **HTML5** semántico
- **CSS3** con Flexbox y Grid
- **JavaScript vanilla** (mínimo)
- **SVG** inline para iconos
- **Git** para control de versiones

## Enlaces

- [Repositorio en GitHub](https://github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage)
- [Sitio original en Drupal](https://ccas.cucea.udg.mx/)