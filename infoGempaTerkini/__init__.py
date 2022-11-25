import requests
from bs4 import BeautifulSoup


def ekstraksiData():
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        tanggal = soup.find('span', {'class': 'waktu'})
        """
        # cara 1 split
        tanggalSplit = tanggal.__copy__()
        tanggal = tanggalSplit.text.split(', ')[0]
        waktu = tanggalSplit.text.split(', ')[1]
        """
        # cara 2 split
        newSplit = tanggal.text.split(', ')
        tanggal = newSplit[0]
        waktu = newSplit[1]

        results = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        results = results.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for rs in results:
            if i == 1:
                magnitudo = rs.text
            elif i == 2:
                kedalaman = rs.text
            elif i == 3:
                koordinat = rs.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = rs.text
            elif i == 5:
                dirasakan = rs.text
            i += 1

        print(results)

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilData(result):
    if result is None:
        print('Tidak dapat memuat data gempa terkini')
        return

    print('Info Terakhir berdasarkan data dari https://www.bmkg.go.id/')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")

# if __name__ == '__main__':
#     print('running..')
