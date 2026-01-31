# 🔍 WichSystem | OS Fingerprinting Tool ⚡

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-cyan?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Language-Python3-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Field-Reconnaissance-red?style=for-the-badge" alt="Field">
</p>

**whichsystem** es una herramienta de reconocimiento pasivo/activo diseñada para identificar el Sistema Operativo de un host remoto mediante el análisis de paquetes ICMP. Utiliza la técnica de inspección del valor **TTL (Time To Live)** para determinar con precisión si el objetivo es una máquina **Linux** o **Windows**.

---

```text
  ██╗    ██╗██╗  ██╗██╗ ██████╗██╗  ██╗██╗  ██╗ ██████╗ ███████╗████████╗
  ██║    ██║██║  ██║██║██╔════╝██║  ██║██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
  ██║ █╗ ██║███████║██║██║     ███████║███████║██║   ██║███████╗   ██║   
  ██║███╗██║██╔══██║██║██║     ██╔══██║██╔══██║██║   ██║╚════██║   ██║   
  ╚███╔███╔╝██║  ██║██║╚██████╗██║  ██║██║  ██║╚██████╔╝███████║   ██║   
   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   

             [ OS Detection Tool | By: Hacknet ]
-------------------------------------------------------------------------
```
```bash
# Clonar el repositorio
git clone https://github.com/matiashenao/whichsystem

# Acceder al directorio
cd whichsystem

# Asignar permisos de ejecución al script
chmod +x whichsystem.py

# Ejecución
python3 whichsystem.py <ip_objetivo>
```

| Sistema Operativo   | Valor TTL |            Comportamiento             |
| :---------------:   | :-------: | :-----------------------------------: |
| **Linux/Unix**      |   `64`    | Respuesta rápida, stack estable       |
| **Windows**         |   `128`   | Stack de red estándar de Microsoft    |
| **Network Devices** |   `255`   | Routers, Switches o sistemas antiguos |
