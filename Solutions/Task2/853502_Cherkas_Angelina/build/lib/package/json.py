def parse_string(_data, index):
    string = ''
    while _data[index] != '"':
        string += _data[index]
        index += 1
    return string, index + 1


def parse_number(_data, index):
    number = ''
    while _data[index] not in (',', ']', '}'):
        number += _data[index]
        index += 1
    if number == 'null':
        number = None
    elif '.' in number:
        number = float(number)
    else:
        number = int(number)
    return number, index


def parse_json(_data, index=0):
    if _data[index] == '[':
        _list = []
        index += 1
        while _data[index] != ']':
            if _data[index] == '"':
                string, index = parse_string(_data, index + 1)
                _list.append(string)
            elif _data[index] in (' ', ','):
                index += 1
            elif _data[index] in ('[', '{'):
                value, index = parse_json(_data, index)
                _list.append(value)
            else:
                number, index = parse_number(_data, index)
                _list.append(number)
        return _list, index + 1
    elif _data[index] == '{':
        _object = {}
        index += 1
        while _data[index] != '}':
            key, index = parse_string(_data, index + 1)
            while _data[index] in (':', ' '):
                index += 1
            if _data[index] in ('{', '['):
                value, index = parse_json(_data, index)
                _object[key] = value
            elif _data[index] == '"':
                value, index = parse_string(_data, index + 1)
                _object[key] = value
            else:
                number, index = parse_number(_data, index)
                _object[key] = number
            while _data[index] in (',', ' '):
                index += 1
        return _object, index + 1


def get_json(py_object):
    json_type = type(py_object)
    if json_type is dict:
        string = '{'
        dict_len = len(py_object)

        for i, (key, val) in enumerate(py_object.items()):
            string += '"{}": {}'.format(key, get_json(val))

            if i < dict_len - 1:
                string += ', '
            else:
                string += '}'

        return string
    elif json_type is list:
        string = '['
        list_len = len(py_object)

        for i, val in enumerate(py_object):
            string += get_json(val)

            if i < list_len - 1:
                string += ', '
            else:
                string += ']'

        return string
    elif json_type is str:
        return '"{}"'.format(py_object)
    elif json_type is bool:
        return 'true' if py_object else 'false'
    elif json_type is None:
        return 'null'

    return str(py_object)


if __name__ == '__main__':
    res = {'glossary': {'title': 'exampleglossary', 'GlossDiv': {'title': 'S', 'GlossList': {
        'GlossEntry': {'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'StandardGeneralizedMarkupLanguage',
                       'Acronym': 'SGML', 'Abbrev': 'ISO8879:1986',
                       'GlossDef': {'para': 'Ameta-markuplanguage,usedtocreatemarkuplanguagessuchasDocBook.',
                                    'GlossSeeAlso': ['GML', 'XML']}, 'GlossSee': 'markup'}}}}}
