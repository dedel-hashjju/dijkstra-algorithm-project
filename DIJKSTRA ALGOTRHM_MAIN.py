import tkinter as tk
from tkinter import ttk, messagebox
import heapq

tempat = {
    "A": "DELI PARK MALL",
    "B": "Jl. Guru Patimpus I- Jl. Laboratorium",
    "C": "Jl. Laboratorium - Jl. Kelapa Sawit",
    "D": "Jl. Kelapa Sawit - Jl. KL. Yos Sudarso",
    "E": "Jl. KL. Yos Sudarso - Jl. Putri Hijau I/II",
    "F": "Jl. Putri Hijau I/II - Jl. Putri Merak Jingga",
    "G": "Jl. Putri Merak Jingga - Jl. Perintis Kemerdekaan",
    "H": "Jl. Perintis Kemerdekaan - Jl. M.H Thamrin I",
    "I": "Jl. Guru Patimpus II - Jl. Sei Deli",
    "J": "Jl. Sei Deli - Jl. Gatot Subroto",
    "K": "Jl. Gatot Subroto - Jl. Kapten Maulana Lubis",
    "L": "Jl. Kapten Maulana Lubis - Jl. Imam Bonjol",
    "M": "Jl. Imam Bonjol - Jl. Letjen Suprapto",
    "N": "Jl. Letjen Suprapto - Jl. Pemuda 1",
    "O": "Jl. Pemuda 1 - Jl. Palang Merah",
    "P": "Jl. Palang Merah - Jl. M.T Haryono",
    "Q": "Jl. M.T Haryono - Jl. M.H Thamrin",
    "R": "Jl. Raden Saleh - Jl. Balai Kota",
    "S": "Jl. Balai Kota - Jl. Prof. H.M Yamin",
    "T": "Jl. Prof. H.M Yamin - Jl. Stasiun Kereta Api",
    "U": "Jl. Stasiun Kereta Api - Jl. M.T Haryono",
    "V": "Jl. M.H Thamrin I - Jl. Prof. H.M Yamin",
    "W": "Jl. Pemuda 2 - Jl. Jend. Ahmad Yani",
    "X": "Jl. Jend. Ahmad Yani - Jl. Balai Kota",
    "Y": "Jl. Perdagangan - Jl. Pemuda 2",
    "Z": "Thamrin Plaza (Jl. M.H. Thamrin)",
    "AB": "Jl. Gwangju - Jl. Jend. Ahmad Yani",
    "AC": "Jl. Prof. H.M Yamin - Jl. Sutomo - Jl. M.T Haryono",
    "AD": "Jl. M.H Thamrin - Jl. Veteran",
    "AE": "Jl. Veteran - Jl. Timor",
    "AF": "Jl. Veteran - Jl. Jawa",
    "AG": "Jl. Perintis Kemerdekaan - Jl. HM. Said - Jl. Prof. H.M Yamin",
    "AH": "Jl. Jend. Ahmad Yani - Jl. Perdana - Jl. Imam Bonjol",
    "AI": "Jl. H.M Yamin - Jl. Bedagai",
    "AJ": "Jl. M.T Haryono - Jl. Irian Barat - Jl. Veteran",
    "AK": "Jl. M.H Thamrin - Jl. Sei Kera 1",
    "AL": "Jl. Sei Kera 1 - Jl. Sei Kera 2",
    "AM": "Jl. Putri Merak Jingga 2 - Jl. Perintis Kemerdekaan",
    "AN": "Jl. Perintis Kemerdekaan 2 - Jl. Guru Patimpus (Deli Park)",
    "AO": "Jl. M.H Thamrin I - Jl. M.H Thamrin II"
}

graph = {
    "A": {"B": 0.139, "AN": 0.45},
    "B": {"A": 0.139, "C": 0.143, "I": 0.10},
    "C": {"B": 0.143, "D": 0.28},
    "D": {"C": 0.28, "E": 0.14},
    "E": {"D": 0.14, "F": 0.35},
    "F": {"E": 0.35, "G": 1.10, "AM": 0.35, "AN":0.35},
    "G": {"F": 1.1, "AN": 0.45, "AM": 0.3, "AG":0.555, "H":0.23},
    "H": {"G": 0.23, "AG": 0.555, "V":1.0, "AO": 1.3, "Z":0.23},
    "I": {"B": 0.1, "C": 1.43, "J": 0.35},
    "J": {"I": 0.35, "K": 0.07, "AF": 0.428},
    "K": {"J": 0.07, "L": 0.55},
    "L": {"K": 0.55, "R": 0.3, "M":1.365},
    "M": {"L": 1.365, "R": 0.30, "AH":0.614, "N": 0.70},
    "N": {"M": 0.70, "O": 0.412},
    "O": {"N": 0.412, "W": 0.4, "P": 0.14},
    "P": {"O": 0.14, "W": 0.40, "Q": 0.14},
    "Q": {"P": 0.14, "U": 1.0, "AJ": 1.0, "AC": 1.0},
    "R": {"M": 0.30, "L": 0.30, "S": 0.35, "X": 0.30},
    "S": {"X": 0.65, "T": 0.35, "R": 0.35},
    "T": {"S": 0.35, "U": 0.19, "AM": 0.19, "V": 0.19},
    "U": {"T": 0.19, "AM": 0.3, "V": 1.0, "AB": 1.0, "Y": 1.0, "P": 0.14, "Q": 1.0},
    "V": {"H": 1.0, "AO": 1.0, "AG": 1.0, "AI": 1.0, "AC": 1.0, "AE": 1.0, "AF": 1.0, "U": 1.0, "T": 0.19, "AM": 1.0},
    "W": {"AH": 0.614, "O": 0.4, "P": 0.4, "Y": 0.4, "AB": 0.4, "X": 0.4},
    "X": {"AH": 0.614, "AB": 0.65, "W": 0.4, "S": 0.65, "R": 0.65},
    "Y": {"U": 0.073, "W": 0.073},
    "Z": {"H": 0.23, "AO": 1.3},
    "AB": {"W": 0.084, "AH": 0.084, "X": 0.084, "U": 0.084},
    "AC": {"Q": 0.95, "V": 0.95, "AL": 0.29, "AK": 0.95, "AO": 0.95},
    "AD": {"AJ": 0.428, "AF": 0.77, "AE": 0.7, "AI": 0.45, "AO": 1.3},
    "AE": {"V": 0.7, "AD": 0.7},
    "AF": {"AD": 0.93, "AJ": 0.428, "V": 0.77},
    "AG": {"V": 0.555, "G": 0.555, "H": 0.555},
    "AH": {"M": 1.365, "W": 0.614, "AB": 0.614, "X": 0.614},
    "AI": {"AD": 0.93, "V": 0.45, "AK": 0.45, "AL": 0.45},
    "AJ": {"Q": 0.428, "AD": 0.93},
    "AK": {"AC": 0.95, "AI": 0.29},
    "AL": {"AI": 0.29, "AO": 0.29, "AC": 0.29},
    "AM": {"T": 0.3, "U": 1.0, "V": 0.3, "AN": 0.3, "F": 0.35, "G": 0.3},
    "AN": {"A": 0.45, "F": 0.35, "G": 0.45, "AM": 0.45},
    "AO": {"H": 1.3, "V": 1.3, "AL": 1.3, "AD": 0.93, "AC": 0.95, "Z": 1.3},
    "MZ": {}
}


def dijkstra(graph, start, tujuan):
    pq = []
    heapq.heappush(pq, (0, start))
    
    jarak = {}
    sebelumnya = {}

    for node in graph:
        jarak[node] = float("inf")
        sebelumnya[node] = None

    jarak[start] = 0

    while pq:
        jarak_sekarang, node_sekarang = heapq.heappop(pq)

        for tetangga, bobot in graph[node_sekarang].items():
            total = jarak_sekarang + bobot

            if total < jarak[tetangga]:
                jarak[tetangga] = total
                sebelumnya[tetangga] = node_sekarang
                heapq.heappush(pq, (total, tetangga))

    # Jika tujuan tidak bisa dicapai
    if jarak[tujuan] == float("inf"):
        return None, None

    path = []
    sekarang = tujuan

    while sekarang:
        path.append(sekarang)
        sekarang = sebelumnya[sekarang]

    path.reverse()
    return path, jarak[tujuan]

def cari_rute():
    start = combo_awal.get()
    tujuan = combo_tujuan.get()

    if start == "" or tujuan == "":
        messagebox.showwarning(
            "Peringatan",
            "Pilih titik awal dan tujuan!"
        )
        return

    path, total = dijkstra(graph, start, tujuan)

    # Jika tidak ada jalur
    if path is None:
        messagebox.showwarning(
            "Rute Tidak Ditemukan",
            "Rute tidak dapat ditentukan karena node tidak terhubung!"
        )
        return

    hasil_text.delete(1.0, tk.END)
    hasil_text.insert(tk.END, "HASIL PERHITUNGAN DIJKSTRA\n\n")
    hasil_text.insert(tk.END, "Rute Terpendek : \n")

    for p in path:
        hasil_text.insert(tk.END, p + " -> ")

    hasil_text.insert(tk.END, "\n\n")
    hasil_text.insert(tk.END, "Detail Lokasi:\n\n")

    for p in path:
        hasil_text.insert(tk.END, f"{p} = {tempat[p]}\n")

    hasil_text.insert(tk.END, "\n")
    hasil_text.insert(tk.END, f"Total Jarak : {round(total,2)} KM")


root = tk.Tk()
root.title("Program Dijkstra Deli Park - Thamrin Plaza Mall")
lebar = root.winfo_screenwidth()
tinggi = root.winfo_screenheight()
root.geometry(f"{lebar}x{tinggi}")
root.configure(bg="#dfe6e9")

judul = tk.Label(
    root,
    text="IMPLEMENTASI ALGORITMA DIJKSTRA\nMENENTUKAN RUTE TERPENDEK",
    font=("Times New Roman", 16, "bold"),
    bg="#dfe6e9"
)

judul.pack(pady=15)

frame = tk.Frame(root, bg="#dfe6e9")
frame.pack()

tk.Label(frame, text="Titik Awal", bg="#dfe6e9").grid(row=0, column=0, padx=10)

combo_awal = ttk.Combobox(frame, values=list(graph.keys()), width=20)
combo_awal.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Titik Tujuan", bg="#dfe6e9").grid(row=0, column=2, padx=10)

combo_tujuan = ttk.Combobox(frame, values=list(graph.keys()), width=20)
combo_tujuan.grid(row=0, column=3, padx=10)

btn = tk.Button(
    root,
    text="Cari Rute Terpendek",
    command=cari_rute,
    bg="#0984e3",
    fg="white",
    font=("Arial", 11, "bold")
)

btn.pack(pady=15)

hasil_text = tk.Text(root, width=90, height=25)
hasil_text.pack(pady=10)

root.mainloop()