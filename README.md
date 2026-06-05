# 🔍 Network Sniffer

> A lightweight, real-time network packet analyzer built with Python and Scapy — logs traffic to both human-readable text and structured CSV formats.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output Files](#output-files)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Disclaimer](#disclaimer)
- [Author](#author)

---

## ✨ Features

- 📡 **Live packet capture** on any network interface
- 🔎 **Protocol detection** — TCP, UDP, ICMP, and others
- 🏷️ **Detailed packet info** — IPs, ports, TCP flags, payload size, and summary
- 📝 **Dual logging** — human-readable `.txt` and structured `.csv`
- 🎛️ **BPF filter support** — capture only what you need (e.g., `tcp`, `icmp`, `port 80`)
- 💾 **Custom output filenames** via CLI argument

---

## ⚙️ Requirements

- Python 3.7+
- [Scapy](https://scapy.net/)
- Root / Administrator privileges (required for raw socket access)

---

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/network-sniffer.git
cd network-sniffer
```

**2. Install dependencies**

```bash
pip install scapy
```

> On Linux/macOS, run with `sudo`. On Windows, run your terminal as Administrator.

---

## 🛠️ Usage

```bash
sudo python sniffer.py [OPTIONS]
```

### Options

| Flag | Long Form | Description | Default |
|------|-----------|-------------|---------|
| `-i` | `--iface` | Network interface to sniff on | System default |
| `-f` | `--filter` | BPF filter expression | None (capture all) |
| `-o` | `--output` | Output filename (without extension) | `captured_packets` |

### Examples

```bash
# Capture all traffic on the default interface
sudo python sniffer.py

# Capture only TCP traffic on eth0
sudo python sniffer.py -i eth0 -f tcp

# Capture ICMP packets and save to custom file
sudo python sniffer.py -f icmp -o icmp_log

# Capture HTTP traffic on a specific interface
sudo python sniffer.py -i wlan0 -f "port 80" -o http_traffic
```

Press **Ctrl + C** to stop the sniffer gracefully.

---

## 📁 Output Files

The sniffer produces two output files simultaneously:

### `captured_packets.txt` (or custom name)
Human-readable log with one block per packet:

```
[2024-12-01 14:32:10]
Protocol         : TCP
Source IP        : 192.168.1.5
Destination IP   : 142.250.182.46
Source Port      : 54320
Destination Port : 443
Length           : 66 bytes
TCP Flags        : PA
Payload Size     : 26 bytes
Summary          : Ether / IP / TCP 192.168.1.5:54320 > 142.250.182.46:https PA / Raw
------------------------------------------------------------
```

### `captured_packets.csv` (or custom name)
Structured CSV for analysis in Excel, pandas, or any BI tool:

| timestamp | protocol | src_ip | dst_ip | src_port | dst_port | length | tcp_flags | payload_size | summary |
|-----------|----------|--------|--------|----------|----------|--------|-----------|--------------|---------|
| 2024-12-01 14:32:10 | TCP | 192.168.1.5 | 142.250.182.46 | 54320 | 443 | 66 | PA | 26 | Ether / IP / TCP ... |

---

## 📂 Project Structure

```
network-sniffer/
├── sniffer.py               # Main script
├── captured_packets.txt     # Text log (auto-generated)
├── captured_packets.csv     # CSV log (auto-generated)
└── README.md
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized network monitoring only**.

- Only use this tool on networks you **own or have explicit permission** to monitor.
- Unauthorized packet capture may violate local laws and regulations (e.g., CFAA, GDPR, IT Act).
- The author is **not responsible** for any misuse or damage caused by this tool.

---

## 👨‍💻 Author

**Manikandan**

- Part of the **CodeAlpha Internship Project**
- Built with ❤️ using Python & Scapy

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
