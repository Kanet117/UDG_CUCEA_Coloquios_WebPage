# Guia de Modificacion en Drupal

## Como editar el contenido de una pagina

### Paso 1: Iniciar sesion
Ir a `https://ccas.cucea.udg.mx/user` e ingresar con las credenciales de administrador.

### Paso 2: Localizar la pagina
- Ir a **Contenido** → se desplegara el listado completo de paginas del sitio
- Identificar la pagina por su titulo (ej. "inicio", "convocatoria", "comite")
- Click en **Editar**

### Paso 3: Editar el contenido
La interfaz mostrara el contenido en modo preview con un editor visual. Existen dos modalidades de edicion:

**Opcion A: Editor visual (recomendado para cambios sencillos)**
- Seleccionar directamente el texto o imagen en el preview
- Utilizar las herramientas de la barra superior (negritas, colores, alineacion, enlaces)
- Ideal para actualizar textos, fechas o imagenes sin modificar la estructura

**Opcion B: Fuente HTML (recomendado para cambios estructurales)**
- Click en el icono **`<>`** (Fuente HTML) para ver el codigo completo
- **Importante**: Verificar que el formato de texto seleccionado sea **"HTML completo"**
- Realizar las modificaciones directamente en el codigo
- Utilizar esta opcion para: agregar iframes, modificar estilos, cambiar estructura de componentes

### Paso 4: Guardar los cambios
- Click en **Guardar** (boton ubicado en la parte inferior)
- Opcional: utilizar **Preview** para visualizar los cambios antes de guardar

## Como modificar el footer

1. Navegar a **Estructura → Diseno de bloques → Biblioteca de bloques personalizados**
2. Seleccionar **Footer Global CCAs**
3. El proceso de edicion es identico al de una pagina (Fuente HTML + Guardar)
4. El footer contiene los estilos globales del sitio, por lo que se debe tener precaucion al modificarlo

## Como modificar el menu de navegacion (navbar)

1. Ir a **Estructura → Menus → Main navigation**
2. Se mostraran todos los enlaces del menu principal:

| Enlace del menu | Accion |
|---|---|
| CCAs | Editar |
| Inicio | Editar |
| Convocatoria | Editar |
| Comite | Editar |
| Guias | Editar |
| Registro | Editar |
| Programa | Editar |
| Conferencistas | Editar |

3. Para modificar un enlace: Click en **Editar** → cambiar titulo o ruta → Guardar
4. Para agregar un enlace: Click en **"Agregar enlace"** → completar titulo y ruta → Guardar
5. Para eliminar un enlace: Click en **"Eliminar"**
6. El orden de los enlaces se controla mediante los pesos (valores mas pequenos aparecen primero)

## Como reemplazar el PDF de convocatorias

1. Subir el nuevo PDF a Google Drive
2. Obtener el ID del archivo desde la URL (ej. `13Y7NFPjp9BVZO2C17iC-ccZwR6ykr1Cu`)
3. Construir la URL de previsualizacion: `https://drive.google.com/file/d/[ID]/preview`
4. Ir a la pagina **Convocatorias** en Drupal
5. Editar → Fuente HTML
6. Localizar el iframe y reemplazar el valor del atributo `src`
7. Guardar

## Como actualizar los enlaces de YouTube en Programa

1. Ir a la pagina **Programa**
2. Editar → Fuente HTML
3. Localizar el enlace (`<a>`) del dia que se desea modificar
4. Reemplazar el atributo `href` por la nueva URL de YouTube Live
5. Guardar

## Como agregar o eliminar ediciones en la pagina de inicio

1. Ir a la pagina **Inicio**
2. Editar → Fuente HTML
3. Localizar los botones con clase `botton-events`
4. Para agregar: copiar la estructura de un boton existente y ajustar el texto y enlace
5. Para deshabilitar un boton (ediciones futuras): agregar la clase `botton-events disabled`
6. Guardar