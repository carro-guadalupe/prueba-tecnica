# PPRUEBA TÉCNICA – DEVOPS/SYSADMIN  

Implementación de una POC de mensajeria HL7 clásica (v2.x) usando Docker Compose 

---

## Requisitos 
- Docker y Docker Compose
- Python 3
- Mirth Connect Administrator Launcher
- DBeaver u otro cliente PostgreSQL
- Git


## Credenciales
.env -> usuario y clave de la DB
Deben completarlo con los datos que les paso correo



## Despliegue

1. Clonar el repositorio
bash
git clone https://github.com/carro-guadalupe/prueba-tecnica.git
cd prueba-tecnica


2. Iniciar los servicios

bash
docker-compose up -d


3. Importar y Desplegar el Canal en Mirth Connect
    1. Conectarse a https://localhost:8443 y descargar Mirth Connect Administrator Launcher
    2. Iniciar sesion con usuario "admin" y clave "admin". (Va a pedir cambio de clave)
    3. Navegar a Channels -> Clic derecho -> Import Channel
    4. Seleccionar el archivo export-canal-mirth.xml (esta en el raiz del proyecto)
    5. Hacer clic derecho sobre el canal cargado y seleccionar Deploy Channel


## Prueba de Envío

Para enviar un mensaje de prueba HL7:

bash
python scripts/enviar-hl7.py



## Verificación y Consultas

 1. Consultar en PostgreSQL el mensaje en crudo
Conectarse desde DBeaver
Localhost:5433
DB: hl7db
Se enviara un link por correo


SELECT * FROM hl7_raw_messages ORDER BY id DESC LIMIT 10;


2. Consultar recursos en el servidor FHIR (HAPI)

http://localhost:8081/fhir/Patient?_format=json


## Endpoint
- Mirth HTTP: http://localhost:8080
- Mirth Connect Administrator: https://localhost:8443
- HL7 MLLP: localhost:6661
- PostgreSQL: localhost:5433
- Patients: http://localhost:8081/fhir/Patient
