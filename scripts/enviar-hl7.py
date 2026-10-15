import socket

mensaje = (
    r"MSH|^~\&|HIS|RIH|EKG|EKG|200202150930||ADT^A01|MSG00001|P|2.3"
    + "\r"
    + "PID|1||123456||PEREZ^JUAN"
    + "\r"
)

# Envoltura MLLP: inicio + mensaje + final.
paquete = b"\x0b" + mensaje.encode("utf-8") + b"\x1c\x0d"

with socket.create_connection(("127.0.0.1", 6661), timeout=10) as conexion:
    conexion.settimeout(60)
    conexion.sendall(paquete)

    respuesta = b""

    while b"\x1c\x0d" not in respuesta:
        parte = conexion.recv(4096)

        if not parte:
            raise RuntimeError("La conexión se cerró sin un ACK completo")

        respuesta += parte

ack = (
    respuesta.split(b"\x1c\x0d")[0]
    .lstrip(b"\x0b")
    .decode("utf-8")
)

print("Respuesta de Mirth:")
print(ack.replace("\r", "\n"))

msa = next(
    (
        segmento.split("|")
        for segmento in ack.split("\r")
        if segmento.startswith("MSA|")
    ),
    None
)

if not msa or len(msa) < 3:
    raise RuntimeError("No se encontró el segmento MSA del ACK")

if msa[1] != "AA" or msa[2] != "MSG00001":
    raise RuntimeError("Mirth devolvió un error o un identificador diferente")

print("OK: Mirth devolvió ACK AA para MSG00001.")

