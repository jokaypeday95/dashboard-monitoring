"""
Info deteksi gempa terkini
Modularisasi dengan function
"""


def ekstraksiData():
    hasil = dict()
    hasil['tanggal'] = '24 November 2022'
    hasil['waktu'] = '03:51:00 WIB'
    hasil['magnitudo'] = 3.4
    hasil['kedalaman'] = '6 km'
    hasil['lokasi'] = {'ls': 6.85, 'bt': 107.08}
    hasil['pusat'] = 'Pusat gempa berada di darat 7 km BaratDaya Kab-Cianjur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Cipanas, II - III Cibeber'
    return hasil


def tampilData(result):
    print('Info Terakhir berdasarkan data dari https://www.bmkg.go.id/')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['waktu']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('running...')
    result = ekstraksiData()
    tampilData(result)

