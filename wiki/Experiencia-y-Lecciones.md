# Experiencia y Lecciones Aprendidas

## Historia del Proyecto

### El inicio: un proyecto frustrado

Originalmente, el plan era desarrollar una aplicación con machine learning para la predicción de sarcopenia. Sin embargo, otro compañero borró mi nombre de la lista de asignación en el Excel y puso el suyo. La coordinadora no intervino a pesar de reportarlo. Así que quedé con el proyecto de la página web.

### La incertidumbre tecnológica

Al preguntar qué tecnologías podía usar, la respuesta fue ambigua:

1. **Primera respuesta**: "Las que quieras"
2. **Segunda respuesta** (con un maestro): "Drupal o PHP"
3. **Decisión final**: Solo Drupal

Esto significó que la planeación inicial (hecha antes de saber que sería Drupal) quedó obsoleta. El documento de planeación estimaba tiempos con tecnologías que después no podría usar.

### La espera por los accesos (~3 meses)

Solicité los accesos al sistema Drupal y pasaron aproximadamente **3 meses** sin respuesta. Durante ese tiempo:
- Estudié Drupal por mi cuenta
- Aprendí sobre sus módulos, vistas, bloques y themes
- No podía avanzar porque no tenía acceso al sistema

### Desarrollo en Drupal

Una vez con acceso, trabajé en la arquitectura del sitio usando:
- **Vistas de Drupal** para páginas dinámicas
- **Bloques personalizados** para componentes reutilizables
- Una arquitectura que permitiría mostrar años anteriores y futuros del coloquio llenando un formulario simple

### El problema del CSS (~3 semanas perdidas)

Cuando el sitio ya estaba casi terminado, me di cuenta de que **no tenía acceso a la sección de diseño (CSS) de Drupal**. Intenté:
- Solicitar los permisos → no hubo respuesta
- Buscar alternativas dentro de Drupal → no se podía sin los accesos adecuados
- Usar workarounds → limitados

Perdí aproximadamente **3 semanas** tratando de resolver esto. Eventualmente reporté que era imposible continuar sin los accesos. La respuesta fue contradictoria: "no ocupas acceso, no te pedí eso" (visible en los correos).

### La solución: páginas estáticas

Después de una sesión donde expliqué la situación, la solución fue cambiar a **páginas básicas estáticas** en Drupal, que sí permiten HTML, CSS y JS en el cuerpo. En aproximadamente **1 semana** repliqué el diseño del Google Sites actualizado.

### Hacks necesarios por falta de accesos

Como nunca me dieron acceso completo al diseño, tuve que:

1. **Navbar en HTML**: El menú de navegación se configuró como un bloque personalizado, pero al no poder acceder al CSS del theme, los estilos del navbar van **inline en el footer** mediante un bloque global
2. **`!important` masivo**: Para invalidar los estilos del theme Drupal que no podía modificar, usé `!important` en cada regla CSS
3. **Redirección por script**: Drupal no permitía configurar la página de inicio fácilmente, así que puse un script en el footer que redirige `/` a `/inicio`
4. **Desactivar Smoove**: El theme Drupal tenía una animación Smoove que ocultaba el footer. Tuve que desactivarla con CSS forzado
5. **Errores de seguridad**: Al inspeccionar la página, Drupal marca errores de seguridad por los scripts inline. No afectan la experiencia del usuario pero son visibles en consola

### Ajustes finales (2-3 semanas)

Las últimas semanas se dedicaron a los ajustes solicitados por la Dra. Karen:
- Cambiar "Etiqueta editable" por nombres reales
- Eliminar años de las fechas
- Añadir PDF de convocatoria
- Agregar "Título" en rojo antes del nombre de cada charla
- Poner nombres en rojo y más grande bajo las fotos

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