import logging
import argparse

FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='transnum.log.', filemode='a', encoding='utf-8', format=FORMAT, style='{', level=20)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Перевод числа в другую сиситему исчесления')
parser.add_argument('numbers', metavar='N', type=str, nargs='*', help='Введите целые числа с положительным основанием')
args = parser.parse_args()


def transnum(number, osn) -> str:
    '''
    Программа получает целое число и возвращает его шестнадцатеричное/восьмеричное/двоичное строковое представление.
    '''

    number_old = number
    digits = []
    digits_letter = {}
    for key, value in enumerate(range(ord('a'), ord('z') + 1), 10):
        digits_letter.update({key: chr(value)})
    if number.isnumeric() and osn.isnumeric() and int(osn) > 0:
        number = int(number)
        osn = int(osn)
        while number != 0:
            if number % osn > 9:
                digits.insert(0, digits_letter[number % osn])
            else:
                digits.insert(0, str(number % osn))
            number = number // osn
        result = ''.join(digits)
        logger.info(f'Целое число {number_old} преобразованно в {result} по основанию {osn}')
        return result
    else:
        logger.error(f'Введите целые числа с положительным основанием')
        return f'Числа должны быть с положительным основанием'


if __name__ == '__main__':
    if args.numbers:
        print(transnum(*args.numbers))
    else:
        print(transnum(input('Input integer number - '), input('Input osnovanie - ')))
