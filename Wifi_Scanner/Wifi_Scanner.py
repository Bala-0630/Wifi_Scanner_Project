import subprocess
import tkinter as tk
from tkinter import messagebox, ttk, font
import re

def signal_quality(signal): if signal > 75: return "Excellent", "green" elif signal > 40: return "Good", "orange" else: return "Poor", "red"

def band_from_channel(channel):
    if channel <= 14:
        return "2.4 GHz"
    else:
        return "5 GHz"

def scan_wifi():
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            encoding="utf-8"
        )

        for item in tree.get_children():
            tree.delete(item)

        networks = {}
        current_ssid = None

        for line in output.splitlines():
            ssid_match = re.search(r"SSID \d+ : (.+)", line)
            if ssid_match:
                current_ssid = ssid_match.group(1).strip()
                networks[current_ssid] = {
                    "signal": [],
                    "authentication": "",
                    "encryption": "",
                    "channel": 0,
                    "rates": "",
                    "bssid_count": 0
                }

            if current_ssid:
                signal_match = re.search(r"Signal\s+: (\d+)%", line)
                if signal_match:
                    networks[current_ssid]["signal"].append(int(signal_match.group(1)))
                    networks[current_ssid]["bssid_count"] += 1

                enc_match = re.search(r"Encryption\s+: (.+)", line)
                if enc_match:
                    networks[current_ssid]["encryption"] = enc_match.group(1)

                auth_match = re.search(r"Authentication\s+: (.+)", line)
                if auth_match:
                    networks[current_ssid]["authentication"] = auth_match.group(1)

                channel_match = re.search(r"Channel\s+: (\d+)", line)
                if channel_match:
                    networks[current_ssid]["channel"] = int(channel_match.group(1))

                rate_match = re.search(r"Basic rates \(Mbps\)\s+: (.+)", line)
                if rate_match:
                    networks[current_ssid]["rates"] = rate_match.group(1)

        if not networks:
            messagebox.showinfo("Info", "No Wi-Fi networks found.")
            return

        # Insert into Treeview
        for ssid, data in networks.items():
            max_signal = max(data["signal"]) if data["signal"] else 0
            quality, color = signal_quality(max_signal)
            band = band_from_channel(data["channel"])

            tree.insert(
                "",
                "end",
                values=(
                    ssid,
                    f"{max_signal}%",
                    quality,
                    data["encryption"],
                    data["authentication"],
                    band,
                    data["channel"],
                    data["bssid_count"],
                    data["rates"]
                ),
                tags=(color,)
            )

        # Color the quality column text
        tree.tag_configure("green", foreground="green")
        tree.tag_configure("orange", foreground="orange")
        tree.tag_configure("red", foreground="red")

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Unable to scan Wi-Fi networks.\nPlease run as Administrator.\n{e}"
        )

def auto_refresh():
    scan_wifi()
    window.after(10000, auto_refresh)

# ---------------- GUI Setup ----------------

window = tk.Tk()
window.title("Wi-Fi Network Scanner")
window.geometry("1400x600")

tk.Label(
    window,
    text="Wi-Fi Network Scanner",
    font=("Arial", 50, "bold")
).pack(pady=10)

tk.Button(
    window,
    text="Scan Wi-Fi Networks",
    font=("Arial", 25),
    command=scan_wifi,
    bg="blue",
    fg="white",
    padx=15,
    pady=8
).pack(pady=10)

# Create Treeview for table
columns = ("SSID", "Signal", "Quality", "Encryption", "Authentication",
           "Bandwidth", "Channel", "Connected Stations", "Rates(MBPS)")

tree = ttk.Treeview(window, columns=columns, show="headings")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Increase font size for header and rows, and add row spacing
tree_font = font.Font(family="Arial", size=14)
style = ttk.Style()
style.configure("Treeview", font=tree_font, rowheight=30)        # Rows font and height
style.configure("Treeview.Heading", font=("Arial", 16, "bold"))  # Header font

# Set column headings and widths
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=130)

# Add a small padding row after the header for spacing
tree.insert("", 0, values=("", "", "", "", "", "", "", "", ""))

# Start auto-refresh
auto_refresh()

window.mainloop()
