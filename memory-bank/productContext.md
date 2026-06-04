# Product Context

## Why This Project Exists
El sitio web del Coloquio de Cuerpos Académicos (CCAs) fue implementado originalmente en Drupal, un CMS institucional de la UdeG. Sin embargo, la burocracia administrativa y la falta de accesos oportunos al sistema (3 meses de retraso inicial, y accesos incompletos durante todo el desarrollo) hicieron inviable mantener el sitio en Drupal a largo plazo. Se decidió migrar a HTML/CSS/JS puro para:

1. **Independencia tecnológica**: No depender de permisos Drupal, módulos, o configuraciones del CMS institucional.
2. **Despliegue simple**: Hosting estático, sin servidor, sin PHP, sin base de datos.
3. **Mantenibilidad**: Código plano que cualquier desarrollador pueda entender y modificar.

## Problems It Solves
- **Burocracia de accesos Drupal**: Se tardaron ~3 meses en dar el primer acceso al proyecto, y luego los accesos para CSS seguían incompletos después de 4 meses.
- **Restricciones del CMS**: Drupal sobrescribía estilos, requería módulos específicos, y forzaba estructuras de layout (sidebar, breadcrumbs, listón UdeG) que no se necesitaban.
- **Dependencia institucional**: Cualquier cambio requería pasar por procesos administrativos lentos.

## How It Should Work
- 5 páginas HTML estáticas con navegación completa entre ellas
- Diseño responsive, limpio, institucional (colores UdeG: azul marino #203864, rojo #B22222, naranja #FF6600)
- Navbar azul fijo en la parte superior con las secciones: CCAs (marca), Inicio, Comité, Conferencistas, Guías, Registro
- Footer con logos institucionales, contacto, y créditos
- Sin dependencias externas — ni siquiera Bootstrap o jQuery

## User Experience Goals
- La página debe verse **exactamente igual** que la versión Drupal
- Carga rápida (sin PHP, sin base de datos, sin módulos)
- Navegación clara e intuitiva
- Accesible desde cualquier dispositivo
- Fácil de actualizar por cualquier persona con conocimientos básicos de HTML/CSS