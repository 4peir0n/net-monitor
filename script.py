import psutil
import socket  # 🔹 Importar socket para tipos de conexión

# Encabezado
print("Conexiones establecidas:\n")
print(f"{'Protocolo':<8} {'Dirección Local':<23} {'Dirección Remota':<23} {'PID':<8} {'Proceso'}")
print("-" * 80)

# Obtener conexiones activas
for conn in psutil.net_connections(kind='inet'):
    proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
    laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
    raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
    pid = str(conn.pid) if conn.pid else "N/A"

    try:
        process = psutil.Process(int(pid)).name() if pid != "N/A" else "N/A"
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, ValueError):
        process = "N/A"

    # Imprimir línea con formato alineado
    print(f"{proto:<8} {laddr:<23} {raddr:<23} {pid:<8} {process}")

