import json

"""This is the module docstring."""

# LOAD DATA
with open("Data/quran.json", "r", encoding="utf=8") as file:
    _QURAN_DATA = json.load(file)

# GLOBAL VARS
suras_names = [None, 'الفاتحة', 'البقرة', 'آل عمران', 'النساء', 'المائدة', 'الأنعام', 'الأعراف', 'الأنفال',
               'التوبة',
               'يونس', 'هود',
               'يوسف', 'الرعد', 'ابراهيم', 'الحجر', 'النحل', 'الإسراء', 'الكهف', 'مريم', 'طه', 'الأنبياء',
               'الحج',
               'المؤمنون',
               'النور', 'الفرقان', 'الشعراء', 'النمل', 'القصص', 'العنكبوت', 'الروم', 'لقمان', 'السجدة',
               'الأحزاب',
               'سبإ',
               'فاطر', 'يس', 'الصافات', 'ص', 'الزمر', 'غافر', 'فصلت', 'الشورى', 'الزخرف', 'الدخان',
               'الجاثية',
               'الأحقاف',
               'محمد', 'الفتح', 'الحجرات', 'ق', 'الذاريات', 'الطور', 'النجم', 'القمر', 'الرحمن', 'الواقعة',
               'الحديد',
               'المجادلة', 'الحشر', 'الممتحنة', 'الصف', 'الجمعة', 'المنافقون', 'التغابن', 'الطلاق',
               'التحريم',
               'الملك',
               'القلم', 'الحاقة', 'المعارج', 'نوح', 'الجن', 'المزمل', 'المدثر', 'القيامة', 'الانسان',
               'المرسلات',
               'النبإ',
               'النازعات', 'عبس', 'التكوير', 'الإنفطار', 'المطففين', 'الإنشقاق', 'البروج', 'الطارق',
               'الأعلى',
               'الغاشية',
               'الفجر', 'البلد', 'الشمس', 'الليل', 'الضحى', 'الشرح', 'التين', 'العلق', 'القدر', 'البينة',
               'الزلزلة',
               'العاديات', 'القارعة', 'التكاثر', 'العصر', 'الهمزة', 'الفيل', 'قريش', 'الماعون', 'الكوثر',
               'الكافرون', 'النصر',
               'المسد', 'الإخلاص', 'الفلق', 'الناس']
suras_numbers = list(range(1, 115))
suras_dict = {int(i): str(suras_names[i]) for i in range(0, 115)}


# CHECK SURA
def sura_exist(sura):
    """CHECK FOR SURA NAME OR SURA NUMBER"""
    if sura in suras_names and not None or sura in suras_numbers:
        return True
    else:
        return False

# GET SURA
def _get_sura_by_name(sura_name):
    ayat = []
    for s in _QURAN_DATA:
        if s['name'] == sura_name:
            for aya in s['verses']:
                ayat.append(aya['text'])
            return ayat


def _get_sura_by_number(sura_number):
    ayat = []
    numToName = suras_dict[sura_number]
    for s in _QURAN_DATA:
        if s['name'] == numToName:
            for aya in s['verses']:
                ayat.append(aya['text'])
            return ayat


def get_sura(sura_name_or_number):
    """GET SURA BY NAME OR BY NUMBER"""
    temp = sura_name_or_number
    if sura_exist(temp):
        if type(temp) == str:
            return _get_sura_by_name(temp)
        elif type(temp) == int:
            return _get_sura_by_number(temp)
    else:
        return ['لم تقم بتحديد السورة']


# GET SURA INFO
def get_sura_info(sura_name_or_number):
    """GET SURA INFO BY NAME OR BY NUMBER"""
    temp = sura_name_or_number
    if sura_exist(temp):
        if type(temp) == str:
            return _get_sura_info_by_name(temp)
        elif type(temp) == int:
            return _get_sura_info_by_number(temp)
    else:
        print('sura not exist')
        pass


def _get_sura_info_by_name(sura_name):
    info = []
    for s in _QURAN_DATA:
        if s['name'] == sura_name:
            sura = s
            for temp in sura:
                if temp != 'verses':
                    info_tuple = (temp, sura[temp])
                    info.append(info_tuple)
    return info


def _get_sura_info_by_number(sura_number):
    info = []
    numToName = suras_names[sura_number]
    for s in _QURAN_DATA:
        if s['name'] == numToName:
            sura = s
            for temp in sura:
                if temp != 'verses':
                    info_tuple = (temp, sura[temp])
                    info.append(info_tuple)
    return info


def get_sura_number(sura):
    for key, value in suras_dict.items():
        if sura == value:
            return key



def get_sura_from_aya(aya):
    for sura in suras_names:
        s = get_sura(sura)
        try:
            for i in s:
                if i == aya:
                    print(sura)
                    return sura
        except TypeError:
            pass


if __name__ == '__main__':
    print('test')
    temp = sura_exist(0)

    print(temp)

