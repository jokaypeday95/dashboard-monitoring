"""
Info deteksi gempa terkini
Modularisasi dengan function
Modularisasi dengan package
"""
import infoGempaTerkini

if __name__ == '__main__':
    print('running...')
    result = infoGempaTerkini.ekstraksiData()
    infoGempaTerkini.tampilData(result)

