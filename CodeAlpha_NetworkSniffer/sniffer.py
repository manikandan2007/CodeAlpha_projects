from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import argparse
import csv
import os

LOG_FILE = "captured_packets.txt"
CSV_FILE = "captured_packets.csv"


def ensure_csv_header(csv_path):
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "timestamp",
                "protocol",
                "src_ip",
                "dst_ip",
                "src_port",
                "dst_port",
                "length",
                "tcp_flags",
                "payload_size",
                "summary"
            ])


def log_packet_text(info):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(info + "\n")


def log_packet_csv(row):
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)


def process_packet(packet):
    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    packet_len = len(packet)

    src_port = "-"
    dst_port = "-"
    protocol = "OTHER"
    flags = "-"

    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        flags = packet[TCP].flags

    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    payload_size = len(bytes(packet.payload))

    output = (
        f"\n[{timestamp}]\n"
        f"Protocol         : {protocol}\n"
        f"Source IP        : {src_ip}\n"
        f"Destination IP   : {dst_ip}\n"
        f"Source Port      : {src_port}\n"
        f"Destination Port : {dst_port}\n"
        f"Length           : {packet_len} bytes\n"
        f"TCP Flags        : {flags}\n"
        f"Payload Size     : {payload_size} bytes\n"
        f"Summary          : {packet.summary()}\n"
        + "-" * 60
    )

    print(output)

    log_packet_text(output)

    log_packet_csv([
        timestamp,
        protocol,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        packet_len,
        str(flags),
        payload_size,
        packet.summary()
    ])


def main():
    global LOG_FILE, CSV_FILE

    parser = argparse.ArgumentParser(
        description="CodeAlpha Project - Network Sniffer"
    )

    parser.add_argument(
        "-i",
        "--iface",
        help="Network interface to sniff on",
        default=None
    )

    parser.add_argument(
        "-f",
        "--filter",
        help="BPF filter (example: tcp or icmp)",
        default=None
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output filename without extension",
        default=None
    )

    args = parser.parse_args()

    if args.output:
        LOG_FILE = f"{args.output}.txt"
        CSV_FILE = f"{args.output}.csv"

    ensure_csv_header(CSV_FILE)

    print("=" * 60)
    print("CodeAlpha Project")
    print("Created by Manikandan")
    print("Network Sniffer Started")
    print("Press Ctrl + C to Stop")
    print("=" * 60)

    try:
        sniff(
            iface=args.iface,
            filter=args.filter,
            prn=process_packet,
            store=False
        )
    except KeyboardInterrupt:
        print("\nSniffer stopped.")


if __name__ == "__main__":
    main()
