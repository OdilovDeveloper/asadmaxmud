def extract_city_name(country: str, address: str) -> str:
    address = address.lower()
    country = country.lower()

    known_city_names_latin = [
        "Asaka tumani", "Andijon shahri", "Xonobod shahri", "Andijon tumani", "Baliqchi tumani",
        "Buloqboshi tumani", "Bo'z tumani", "Jalaquduq tumani", "Izboskan tumani", "Ulug'nor tumani",
        "Marhamat tumani", "Paxtaobod tumani", "Xo'jaobod tumani", "Oltinko'l tumani", "Qo'rg'ontepa tumani",
        "Shahrixon tumani", "Pop tumani", "Namangan shahri", "Mingbuloq tumani", "Kosonsoy tumani",
        "Namangan tumani", "Norin tumani", "To'raqo'rg'on tumani", "Uychi tumani", "Uchqo'rg'on tumani",
        "Chortoq tumani", "Chust tumani", "Yangiqo'rg'on tumani", "Xiva shahri", "Urganch shahri",
        "Bog'ot tumani", "Urganch tumani", "Qo'shko'pir tumani", "Xonka tumani", "Yangiariq tumani",
        "Xiva tumani", "Yangibozor tumani", "Xozarasp tumani", "Shovot tumani", "Gurlan tumani",
        "Tuproqqal'a tumani", "Toshkent tumani", "Yangiyo'l shahri", "Ohangaron shahri", "Nurafshon shahri",
        "Angren shahri", "Bekobod shahri", "Olmaliq shahri", "Chirchiq shahri", "Bekobod tumani",
        "Bo'stonliq tumani", "Qibray tumani", "Zangiota tumani", "Quyichirchiq tumani", "Oqqo'rg'on tumani",
        "Parkent tumani", "O'rta Chirchiq tumani", "Chinoz tumani", "Yuqorichirchiq tumani", "Bo'ka tumani",
        "Yangiyo'l tumani", "Ohangaron tumani", "Piskent tumani", "Bektemir tumani", "Mirobod tumani",
        "Mirzo Ulug'bek tumani", "Sergeli tumani", "Olmazor tumani", "Uchtepa tumani", "Yashnobod tumani",
        "Chilonzor tumani", "Shayxontohur tumani", "Yunusobod tumani", "Yakkasaroy tumani", "Yangi hayot tumani",
        "Buxoro shahri", "Kogon shahri", "Buxoro tumani", "Vobkent tumani", "Jondor tumani", "Kogon tumani",
        "Olot tumani", "Peshku tumani", "Romitan tumani", "Shofirkon tumani", "Qorako'l tumani",
        "Qorovulbozor tumani", "G'ijduvon tumani", "Samarqand shahri", "Urgut tumani", "Paxtachi tumani",
        "Kattaqo'rg'on tumani", "Samarqand tumani", "Bulung'ur tumani", "Jomboy tumani", "Qo'shrabot tumani",
        "Narpay tumani", "Tayloq tumani", "Pastdarg'om tumani", "Nurobod tumani", "Kattaqo'rg'on shahri",
        "Payariq tumani", "Oqdaryo tumani", "Ishtixon tumani", "Arnasoy tumani", "Baxmal tumani",
        "G'allaorol tumani", "Do'stlik tumani", "Jizzax shahri", "Sharof Rashidov", "Zarbdor tumani",
        "Zafarobod tumani", "Zomin tumani", "Mirzacho'l tumani", "Paxtakor tumani", "Forish tumani",
        "Yangiobod tumani", "Navoiy shahri", "Zarafshon shahri", "Karmana tumani", "Tomdi tumani",
        "Navbahor tumani", "Nurota tumani", "Xatirchi tumani", "Qiziltepa tumani", "Konimex tumani",
        "Uchquduq tumani", "Nukus shahri", "Tahiatosh tumani", "Amudaryo tumani", "Beruniy tumani",
        "Qanliko'l tumani", "Qorao'zak tumani", "Kegeyli tumani", "Qo'ng'irot tumani", "Mo'ynoq tumani",
        "Nukus tumani", "Taxtako'pir tumani", "To'rtko'l tumani", "Xo'jayli tumani", "Chimboy tumani",
        "Shumanay tumani", "Ellikqala tumani", "Bo'zotov tumani", "Guliston shahri", "Yangiyer tumani",
        "Shirin tumani", "Oqoltin tumani", "Boyovut tumani", "Guliston tumani", "Mirzaobod tumani",
        "Sayxunobod tumani", "Sirdaryo tumani", "Xovos tumani", "Termiz shahri", "Termiz tumani",
        "Muzrabot tumani", "Oltinsoy tumani", "Denov tumani", "Sariosiyo tumani", "Qiziriq tumani",
        "Jarqo'rg'on tumani", "Angor tumani", "Qumqo'rg'on tumani", "Boysun tumani", "Sho'rchi tumani",
        "Sherobod tumani", "Uzun tumani", "Bandixon", "Shahrisabz shahri", "Qarshi shahri", "Qarshi tumani",
        "Muborak tumani", "G'uzor tumani", "Qamashi tumani", "Chiroqchi tumani", "Shahrisabz tumani",
        "Kasbi tumani", "Koson tumani", "Kitob tumani", "Nishon tumani", "Mirishkor tumani",
        "Dehqonobod tumani", "Yakkabog' tumani", "Ko'kdala tumani", "Farg'ona shahri", "Marg'ilon shahri",
        "Quvasoy shahri", "Qo'qon shahri", "Bog'dod tumani", "Buvayda tumani", "Dang'ara tumani",
        "Yozyovon tumani", "Oltiariq tumani", "Beshariq tumani", "Qo'shtepa tumani", "Rishton tumani",
        "So'x tumani", "Toshloq tumani", "Uchko'prik tumani", "Farg'ona tumani", "O'zbekiston tumani",
        "Quva tumani", "Furqat tumani"
    ]

    city_names = []


    for name in known_city_names_latin:
        city_names.append(name)
        if "'" in name:
            city_names.append(name.replace("'", ""))

    for name in city_names:
        if name.lower() in address or name.lower() in country:
            return name

    # 5. Topilmasa
    raise Exception(f"Shahar/tuman yoki viloyat nomi topilmadi: {country} / {address}")