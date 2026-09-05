# Preguntas para el Socio Formador — Reto Celda Ciberfísica

**Generado:** 2026-09-01 · **Reunión:** _______________

**Para qué sirve esto:** el Socio Formador **califica la Evidencia 2 (Demostrativa, 10 %)**.
Esta reunión no es informativa: es donde se cierra el alcance que él va a evaluar.

> Anota las respuestas aquí mismo. Lo que quede escrito entra al plan, al BOM y
> al tablero. Lo que quede solo en la cabeza se pierde.

---

## Las cinco que no puedes salir sin responder

Si la reunión se corta a los 20 minutos, que sean estas. Cada una bloquea
semanas de trabajo o miles de pesos.

1. **¿Brazo propio o cobot comercial?** — la decisión de alcance más cara del semestre
2. **¿El Haas tiene la tarjeta de interfaz de M-códigos instalada?** — sin ella no hay handshake discreto
3. **¿Cuándo y con qué supervisión podemos usar el CNC?** — es el riesgo R4 y no depende de nosotros
4. **¿Qué pieza real se va a cargar?** — define el gripper, el fixture, el pallet y el payload del brazo
5. **¿Quién paga qué, y con cuánto tiempo de aprobación?** — la ruta crítica son las compras

---

## Bloque 0 · Las tres divergencias abiertas

Están documentadas en `plan-de-trabajo.md` y llevan una semana sin cerrarse.

### 0.1 Brazo robótico propio vs. cobot comercial

- ¿Esperan un **brazo diseñado y fabricado por nosotros**, o un **cobot comercial** (UR3e, Doosan, Techman) montado sobre el riel?
- Si es propio: ¿hay taller, CNC y presupuesto de manufactura disponibles? ¿Quién valida la seguridad de un brazo casero que va a trabajar cerca de personas?
- Si es comercial: **¿lo prestan ustedes?** ¿Qué modelo, y desde qué fecha está disponible?
- ¿Aceptarían un punto intermedio — brazo propio para demostrar el diseño, cobot comercial para la celda que se evalúa?

> **Por qué importa:** fabricar un brazo es un proyecto completo aparte. Si la
> respuesta es "propio", hay que replantear el calendario entero hoy, no en octubre.

**Respuesta:**


### 0.2 Ruedas mecanum

- ¿El piso donde va a operar el AGV es **plano, liso y continuo**? ¿Concreto pulido, epóxico, loseta?
- ¿Hay juntas, rejillas, rampas o desniveles en la ruta?
- ¿Hay viruta, refrigerante o aceite en el piso cerca del CNC?

> **Por qué importa:** las mecanum pierden tracción y odometría con cualquier
> irregularidad, y son especialmente malas sobre viruta y aceite — que es
> exactamente lo que hay alrededor de un centro de maquinado. Si el piso no
> ayuda, hay que decidirlo ahora: mecanum exige 4 motores con encoder y
> cinemática omnidireccional, y cambia el driver, el modelo y el firmware.

**Respuesta:**


### 0.3 Arquitectura de cómputo

- ¿Tienen preferencia o restricción de marca para el controlador de bajo nivel? Nosotros vamos con **NXP S32K312** (ya recibido).
- ¿Aceptan que ROS 2 / SLAM / Nav2 corra en una **SBC clase Jetson Orin Nano** separada? El S32K312 no puede correrlos.
- ¿Tienen una SBC que puedan prestar, o la compramos?

> **Por qué importa:** la SBC faltaba en el BOM original y tiene 5 semanas de
> lead time. Es una de las dos únicas compras con riesgo de calendario.

**Respuesta:**


---

## Bloque 1 · El CNC Haas — el corazón de la integración

Aquí está el riesgo técnico más alto y el que menos controlamos.

### 1.1 La máquina

- **Modelo y año** exactos del Haas
- **Control:** ¿NGC (Next Generation Control) o Classic Haas? ¿Versión de software?
- ¿Tiene la opción **Ethernet / Networking** habilitada y licenciada?

**Respuesta:**


### 1.2 MTConnect

- ¿El **agente MTConnect ya está corriendo**, o hay que habilitarlo?
- ¿Qué **versión del estándar** publica (1.3, 1.7, 2.0)? ¿En qué puerto — el 8082 que asumimos?
- ¿Nos pueden dar el **`/probe`** para ver qué *data items* expone realmente? Necesitamos al menos `execution`, `controllerMode`, `program`, posiciones de ejes y alarmas.
- ¿Publica **estado de puerta y de mandril**? Sin eso no sabemos cuándo es seguro entrar.
- ¿Es solo lectura, o el agente acepta escritura?

> **Por qué importa:** MTConnect es de solo lectura por diseño. Nos dice qué está
> pasando, pero no le podemos *ordenar* nada. Todo el mando tiene que ir por otro
> canal — de ahí la pregunta que sigue.

**Respuesta:**


### 1.3 El handshake discreto (M-códigos)

- ¿La máquina tiene instalada la **tarjeta de interfaz de M-códigos** (los relevadores M121–M128 y las entradas discretas)?
- Si sí: ¿cuántas salidas y entradas quedan **libres** para nosotros?
- ¿Nos permiten **cablear a esa tarjeta**? ¿Quién debe hacer la conexión física — nosotros, mantenimiento, o un técnico Haas?
- ¿Hay alguna entrada de "pieza lista" / "celda libre" ya usada por otro equipo?

> **Por qué importa:** sin esa tarjeta no existe el handshake discreto y toda la
> coordinación se cae a sondeo por MTConnect, que tiene latencia y no es
> determinista. Es la pregunta técnica más importante de la reunión.

**Respuesta:**


### 1.4 Transferencia de programas

- ¿Se puede **cargar programas por SMB** hacia la máquina? ¿Ruta del recurso compartido y credenciales?
- ¿O prefieren **DPRNT / puerto serie**?
- ¿Existe alguna **política de aprobación** antes de meter un programa nuevo al control?

**Respuesta:**


### 1.5 Acceso a la máquina — riesgo R4

- ¿En qué **horarios** podemos ocupar el CNC? ¿Días fijos?
- ¿Se requiere **supervisión** de un técnico? ¿Quién y cómo se agenda?
- ¿La máquina está en **producción**? ¿Con cuánta anticipación hay que reservar?
- ¿Podemos **agendar desde ya** la ventana de la fase 5 (9–22 nov)?
- ¿Qué pasa si el AGV falla a media pieza? ¿Quién tiene autoridad para parar?

> **Por qué importa:** R4 en la matriz de riesgos. Es el único riesgo crítico que
> no podemos mitigar con dinero ni con trabajo — solo con calendario.

**Respuesta:**


---

## Bloque 2 · La pieza y el proceso

Sin esto no se puede diseñar el gripper, el fixture ni dimensionar el brazo.

- ¿Qué **pieza real** se va a cargar? ¿Nos pueden dar una muestra o el plano?
- **Material, peso, dimensiones** y geometría de agarre
- **Tolerancia de posicionamiento** que exige la carga en el fixture del CNC
- ¿El **fixture y el pallet ya existen**, o los diseñamos nosotros?
- ¿La pieza entra **en bruto y sale maquinada**, o hay varias operaciones?
- **Tiempo de ciclo** del CNC por pieza → de ahí sale el takt time y cuántos viajes hace el AGV
- **Tamaño de lote:** ¿cuántas piezas queremos correr en la demostración?
- ¿La pieza sale **caliente, con rebaba o con refrigerante**? Afecta al gripper y a la visión.

**Respuesta:**


---

## Bloque 3 · Visión industrial

- ¿La inspección es **dimensional** (medir) o **de superficie** (rayones, porosidad, rebaba)?
- ¿Cuál es el **criterio pass/fail** concreto? ¿Con qué tolerancia?
- **¿Tienen piezas defectuosas de muestra?** ¿Cuántas?
- ¿Existe un **catálogo de defectos** o historial de qué falla más seguido?
- ¿Cómo es la **iluminación** del área? ¿Podemos instalar iluminación propia?
- ¿Hoy quién y cómo hace esta inspección? ¿Qué tasa de error tiene?

> **Por qué importa:** sin piezas malas no hay forma de entrenar ni de validar
> nada. Es el cuello de botella silencioso de todo proyecto de visión — se
> descubre en noviembre, cuando ya no hay tiempo de conseguirlas.

**Respuesta:**


---

## Bloque 4 · Espacio físico y seguridad

### 4.1 El espacio

- ¿Nos pueden dar el **plano o las medidas** del área de la celda?
- ¿Dónde se ubica el **riel lineal de 2.5 m**? ¿Se **ancla al piso**? ¿Permiten taladrar?
- ¿Cuál es la **ruta del AGV** — distancia, vueltas, anchos de paso?
- ¿Hay **tránsito de personas o montacargas** cruzando esa ruta?
- ¿Hay **espacio de resguardo** para el AGV cuando no opera? ¿Con toma para cargar?

**Respuesta:**


### 4.2 Seguridad

- ¿Qué **normativa** aplica aquí — ISO 10218, ISO/TS 15066 para colaborativo, alguna interna?
- ¿Hace falta una **evaluación de riesgo formal**? ¿Quién la firma?
- ¿Se requiere **cerca perimetral, cortina óptica o escáner de área**?
- ¿Cómo se integran nuestros **paros de emergencia** con los de la máquina y los del área?
- ¿Quién **autoriza** que la celda opere con personas cerca?
- ¿Hay requisito de **inducción de seguridad** para que el equipo entre al área?

> **Por qué importa:** si exigen certificación o evaluación firmada, eso es
> semanas de trámite que hoy no están en el plan.

**Respuesta:**


### 4.3 Energía

- **Tomas disponibles** en el área: voltaje, corriente, ubicación
- ¿Hay **24 V DC** disponible o lo generamos nosotros?
- ¿Restricciones para **cargar baterías de litio** en el área? ¿Requieren gabinete o zona designada?

**Respuesta:**


---

## Bloque 5 · Red y TI

- ¿Hay **Ethernet o WiFi** en el área de la celda? ¿Cobertura donde circula el AGV?
- ¿La máquina y nuestros equipos pueden estar en la **misma red / VLAN**?
- ¿El **firewall** deja pasar el puerto de MTConnect entre nuestro equipo y el Haas?
- ¿Nos dejan levantar un **broker MQTT**? ¿En nuestra SBC o en un servidor de ustedes?
- **Direccionamiento:** ¿DHCP o IP fija? ¿Quién asigna?
- ¿Hay **política de ciberseguridad** para conectar equipo propio a la red de planta?
- ¿Necesitamos que TI **apruebe** algo, y cuánto tarda?

> **Por qué importa:** un firewall corporativo bloqueando el puerto de MTConnect
> mata la integración completa, y enterarse en noviembre es fatal. Se comprueba
> en cinco minutos desde una laptop en el área — pide que lo agenden ya.

**Respuesta:**


---

## Bloque 6 · Materiales y presupuesto

- ¿Qué **prestan o donan** ustedes y qué compramos nosotros? (Los profes ya cubren riel, LiDAR, módulo I/O, balero y motorreductor.)
- ¿Hay **techo de presupuesto**? ¿Por partida o total?
- **Batería LiFePO4** y **SBC clase Jetson**: ¿las cubren ustedes o van por nuestra cuenta?
- ¿Hay **proveedores preferentes** o convenios que acorten el lead time?
- ¿A nombre de quién se **factura**? ¿Qué datos fiscales?
- **¿Cuánto tarda una aprobación de compra** desde que mandamos la cotización?
- ¿Quién **recibe** el material y dónde se resguarda?

> **Por qué importa:** la ruta crítica del proyecto son las compras, no el
> software. El tiempo de aprobación interno es un dato que hoy no tenemos y que
> puede añadir semanas a un lead time que ya es de cinco.

**Respuesta:**


---

## Bloque 7 · Evaluación y expectativas

Él califica la Demostrativa. Pregúntale directo qué quiere ver.

- ¿**Qué esperan ver funcionando** en la Exposición Demostrativa? ¿Hay rúbrica?
- ¿Qué haría que consideren este proyecto un **éxito**? ¿Y un fracaso?
- ¿Prefieren **una función integrada de punta a punta**, o varios subsistemas demostrados por separado?
- ¿Qué han visto **fallar en equipos de semestres anteriores**?
- ¿Hay un **KPI industrial** que les importe — tiempo de ciclo, disponibilidad, scrap, repetibilidad?
- ¿La celda **sigue viva después del semestre**? ¿Quién la mantiene?
- ¿Qué **formato de documentación** quieren recibir? ¿Manuales, planos, código, todo?
- ¿Hay alguna **restricción de propiedad intelectual o confidencialidad**? El repo de GitHub del equipo es **público** — hay que confirmar que eso no les incomoda.

> **Por qué importa:** la última es delicada y más vale preguntarla ahora. Si el
> socio considera confidencial algo del proceso o de la pieza, el repo tiene que
> dejar de ser público **antes** de que subamos planos o datos.

**Respuesta:**


---

## Bloque 8 · Logística de contacto

- ¿Quién es el **contacto técnico** del día a día? ¿Y para compras?
- ¿Por dónde nos comunicamos — correo, Teams, WhatsApp?
- ¿Qué **tiempo de respuesta** razonable esperamos?
- ¿Podemos ir **fuera del horario de clase**? ¿Con qué aviso?
- ¿Quieren **reportes de avance periódicos**? ¿Con qué frecuencia y formato?
- ¿Cuándo es la **siguiente revisión** con ustedes?

**Respuesta:**


---

## Después de la reunión

1. Pasar las respuestas a `plan-de-trabajo.md` y cerrar las tres divergencias del Bloque 0
2. Actualizar el BOM y disparar las cotizaciones pendientes (`python sistema/erp.py estado`)
3. Sincronizar el tablero y Notion (skill `actualizar-todo`)
4. Si cambió el alcance, rehacer el calendario **antes** de la Evidencia 1 — el
   Anteproyecto vale 6 % y define los otros 30 %
