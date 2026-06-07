# Experiencia y Lecciones Aprendidas

## Historia del Proyecto

### Nov 2025 — Primer contacto formal

El 13 de noviembre se estableció el primer contacto a través de un grupo de WhatsApp conformado por Kanet, Ángela (compañera de servicio social), la Dra. Paty y la Mtra. Aidé (coordinadoras). La Dra. Karen no estaba en ese grupo.

Se confirmó:
- El sitio se haría desde el sitio oficial de CUCEA
- Se usaría **Drupal** (el CMS institucional), aunque podrían consultar con CTA si había alternativas
- Se requerían accesos para comenzar
- Se solicitó un **plan de trabajo** con cronograma

Un problema temprano fue que los correos de la Dra. Karen **llegaban a la carpeta de spam** por no ser una cuenta institucional (gmail.com vs udg.mx), lo que retrasó varias comunicaciones iniciales.

### 21 Nov 2025 — Cirugía de emergencia

La Dra. Karen fue sometida a una cirugía de emergencia, lo que pausó las comunicaciones por varios días. Se reanudó el contacto a finales de noviembre.

### 2 Dic 2025 — Gestión con CTA

El Centro de Tecnologías de Aprendizaje (CTA), encargado de las páginas web de CUCEA, informó que se requería una reunión con la Dra. Karen, el coordinador Eduardo Muñoz y Sergio (del CTA) para habilitar los permisos necesarios, ya que por ser alumnos no podían otorgar accesos directos.

### 23-24 Dic 2025 — Contraseña fallida

La clave del sistema Drupal que la Dra. Karen tenía registrada **no funcionaba**, y no se pudo resetear. Esto, sumado al periodo vacacional, retrasó la entrega de accesos hasta enero.

### 11 Feb 2026 — Reunión presencial en CUCEA

Se realizó una visita presencial al campus para coordinar avances y resolver dudas sobre el desarrollo del sitio.

### 15 Dic 2025 — Plan de trabajo entregado

Se entregó un documento con el cronograma de actividades. El plan se hizo antes de tener acceso al sistema, por lo que estimaba tiempos con tecnologías que después resultaron no ser viables.

### 21 Ene 2026 — Primer acceso a Drupal (~2 meses después)

Se recibieron las credenciales (usuario: MantenimientoCcas). La contraseña había fallado en diciembre y hubo que esperar al periodo post-vacacional para que el CTA la restableciera.

### 28 Ene 2026 — Solicitud de permisos de bloques

Al intentar modificar la distribución visual del sitio, el sistema arrojó **error 403 (Acceso Denegado)** en "Estructura > Diseño de bloques". Se solicitó el permiso a la Dra. Karen, quien lo gestionó. Los permisos se concedieron el 4 de febrero.

### ~Abr 2026 — Sin acceso a CSS del tema Drupal (~3 meses sin diseño)

A pesar de tener acceso al contenido y a los bloques, **nunca se otorgó acceso a la sección de diseño (CSS) del tema Drupal**. Esto impidió:
- Modificar colores, fuentes y estilos del sitio
- Personalizar el navbar y el footer visualmente
- Replicar el diseño del Google Sites que la maestra había aprobado

Se solicitaron los accesos en múltiples ocasiones sin éxito. La respuesta fue que "no ocupaba acceso" y que "no se había pedido eso", a pesar de que sin esos permisos era imposible modificar la apariencia del sitio.

Se perdieron aproximadamente **3 meses** entre solicitudes, esperas y reuniones para explicar el bloqueo técnico.

### 22 Abr 2026 — Nuevo Google Sites 2026 + problema del menú gris

La Dra. Karen envió un nuevo Google Sites con el diseño actualizado del sitio de referencia y señaló que el menú gris que se había generado no era lo requerido. Sin embargo, ese menú gris era parte del tema Drupal al que no se tenía acceso de diseño. Para cambiarlo se necesitaban los permisos que nunca se otorgaron.

Se explicó que para modificar el diseño se requerían los accesos solicitados desde enero, y que sin ellos no se podía replicar el sitio de referencia.

### May 2026 — Solución: páginas estáticas

Después de exponer la situación en una reunión, se acordó cambiar la estrategia: en lugar de usar las vistas dinámicas y el theme de Drupal, se usarían **páginas básicas estáticas** que sí permiten HTML, CSS y JS en el cuerpo del contenido.

En aproximadamente **1 semana** se replicó el diseño completo del Google Sites 2026 usando:
- CSS inline con `!important` para vencer los estilos del theme
- Scripts de redirección en el footer
- El navbar como bloque personalizado con estilos inline

### Hacks técnicos necesarios

Como nunca se obtuvo acceso completo al diseño del tema Drupal, se implementaron las siguientes soluciones técnicas:

1. **Navbar en HTML con estilos en el footer**: El menú de navegación se configuró como un bloque personalizado, pero al no poder acceder al CSS del theme, los estilos visuales del navbar se inyectaron **inline** mediante un bloque global en el footer
2. **`!important` masivo**: Para invalidar los estilos del theme Drupal que no se podían modificar, se usó `!important` en cada regla CSS
3. **Redirección por script**: Se agregó un script en el footer que redirige `/` a `/inicio` porque Drupal no permitía configurar la página de inicio fácilmente
4. **Desactivar animación Smoove**: El theme Drupal tenía una animación Smoove que ocultaba el footer. Se desactivó con CSS forzado
5. **Errores de seguridad en consola**: Drupal marca errores de seguridad por los scripts inline. No afectan la experiencia del usuario pero son visibles en la consola del navegador

### Jun 2026 — Ajustes finales y entrega

Las últimas semanas se dedicaron a los ajustes solicitados por la Dra. Karen:
- Cambiar "Etiqueta editable" por nombres reales en Conferencistas
- Eliminar años de las fechas
- Añadir PDF de convocatoria mediante iframe de Google Drive
- Agregar "Título" en rojo antes del nombre de cada charla
- Poner nombres en rojo y más grande bajo las fotos
- Migrar a Flask como versión independiente de Drupal
- Documentación completa (ENTREGA_FINAL.md, CHECKLIST_ENTREGA.md, wiki)

## Lecciones Aprendidas

### Técnicas

1. **Drupal es poderoso pero restrictivo**: Un CMS institucional puede limitar severamente lo que puedes hacer si no tienes todos los accesos
2. **Los `!important` son un arma de doble filo**: Útiles para vencer estilos del theme, pero difíciles de mantener
3. **Páginas básicas como escape**: Cuando no tienes acceso al diseño, las páginas básicas con HTML completo son una alternativa funcional
4. **Flask como alternativa ligera**: Para sitios estáticos, Flask + HTML/CSS puro es más simple y rápido que Drupal

### Administrativas

1. **Documentar todo**: Cada correo, cada solicitud, cada respuesta. Esto protege cuando hay contradicciones ("no ocupas acceso, no te pedí eso")
2. **Los proyectos institucionales tienen burocracia**: 3-4 meses de espera por accesos no es normal en la industria, pero puede serlo en entornos académicos
3. **Siempre tener un plan B**: Cuando el plan A (vistas dinámicas) falló por falta de accesos, el plan B (páginas estáticas) salvó el proyecto
4. **La comunicación temprana de bloqueos es crítica**: Perder 3 semanas esperando permisos que nunca llegaron fue error; debí escalar antes

## Alcance del proyecto

| Aspecto | Logrado |
|---|---|
| 7 páginas funcionales | ✅ |
| Diseño responsive | ✅ |
| Sin dependencias externas | ✅ |
| Código mantenible | ✅ |
| Documentación completa | ✅ |
| Independencia de Drupal (Flask) | ✅ |
| Archivos para copiar a Drupal | ✅ |