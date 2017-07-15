import requests
api = "http://api.fixer.io/latest?base="

print ("""
    AUD = Avustralya Doları
    BGN = Yeni Bulgar Levası
    BRL = Brezilya Reali
    CAD = Kanada Doları
    CHF = İsviçre Frangı
    CNY = Çin Yuanı Renminbi
    CZK = Çek Cumhuriyeti Korunası
    DKK = Danimarka Kronu
    GBP = İngiliz Sterlini
    HKD = Hong Kong Doları
    HRK = Hırvat Kunası
    HUF = Macar Forinti
    IDR = Endonezya Rupiahı
    ILS = Yeni İsrail Şekeli
    INR = Hindistan Rupisi
    JPY = Japon Yeni
    KRW = Güney Kore Wonu
    MXN = Meksika Pezosu
    MYR = Malezya Ringiti
    NOK = Norveç Kronu
    NZD = Yeni Zelanda Doları
    PHP = Filipinler Pezosu
    PLN = Polonya Zlotisi
    RON = Romen Leyi
    RUB = Rus Rublesi
    SEK = İsveç Kronu
    SGD = Singapur Doları
    THB = Tayland Bahtı
    TRY = Türk Lirası
    ZAR = Güney Afrika Randı
    EUR = Euro 
""")

From = input ("From: ")
To = input ("To: ")
Number = float(input ("Number: "))

currency = requests.get(api + From)
json = currency.json()
get_data= json["rates"][To]

print (float(get_data*Number))