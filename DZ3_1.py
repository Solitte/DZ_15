import json
import logging
import argparse


FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='items_friends.log.', filemode='a', encoding='utf-8', format=FORMAT, style='{', level=20)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Список вещей у друзей')
parser.add_argument('name_file', metavar='Name', nargs='*', type=str, help='Введите имя файла с вещами')
args = parser.parse_args()


def items_friends(name_file):
    '''
    ✔ Три друга взяли вещи в поход. Сформируйте
    словарь, где ключ — имя друга, а значение —
    кортеж вещей. Ответьте на вопросы:
    ✔ Какие вещи взяли все три друга
    ✔ Какие вещи уникальны, есть только у одного друга
    ✔ Какие вещи есть у всех друзей кроме одного
    и имя того, у кого данная вещь отсутствует
    ✔ Для решения используйте операции
    с множествами. Код должен расширяться
    на любое большее количество друзей.
    '''
    try:
        with open(name_file, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
    except FileNotFoundError as e:
        print(f'Имя {name_file} введено неверно.')
        logger.error(f'Имя {name_file} введено неверно.')
        return None
    item = set(list(my_dict.values())[0])
    for i in range(len(my_dict)):
        item = item & set(list(my_dict.values())[i])
    logger.info(f'Вещи {tuple(item)} взяли все друзья')
    for i in range(len(my_dict)):
        item = set(list(my_dict.values())[i])
        for j in range(len(my_dict)):
            if i != j:
                item = item - set(list(my_dict.values())[j])
        logger.info(f'{list(my_dict.keys())[i]} имеет уникальные вещи {tuple(item)}')

    for i in range(len(my_dict)):
        item = set()
        for j in range(len(my_dict)):
            if i != j and len(item) == 0:
                item = set(list(my_dict.values())[j])
            elif i != j:
                item = item & set(list(my_dict.values())[j])
        item = item - set(list(my_dict.values())[i])
        logger.info(f'{list(my_dict.keys())[i]} не имеет {tuple(item)}')


if __name__ == '__main__':
    if args.name_file:
        items_friends(args.name_file[0])
    else:
        items_friends('items.json')