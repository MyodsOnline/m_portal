letters_dict = {
    u'а': u'a',
    u'б': u'b',
    u'в': u'v',
    u'г': u'g',
    u'д': u'd',
    u'е': u'e',
    u'ё': u'e',
    u'ж': u'zh',
    u'з': u'z',
    u'и': u'i',
    u'й': u'i',
    u'к': u'k',
    u'л': u'l',
    u'м': u'm',
    u'н': u'h',
    u'о': u'o',
    u'п': u'p',
    u'р': u'r',
    u'с': u's',
    u'т': u't',
    u'у': u'y',
    u'ф': u'f',
    u'х': u'h',
    u'ц': u'ts',
    u'ш': u'sh',
    u'щ': u'sh',
    u'ь': u'',
    u'ъ': u'',
    u'э': u'e',
    u'ю': u'yu',
    u'я': u'ya',
}

def from_cyr_to_eng(text: str):
    text = text.replace(' ', '_').lower()
    tmp = ''
    for char in text:
        tmp += letters_dict.get(char, char)
    return tmp
