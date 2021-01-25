import requests
from requests.models import parse_header_links
import bs4
import argparse


def get_prizes():
    r = requests.get("http://ketqua.net")
    tree = bs4.BeautifulSoup(markup=r.text)
    prizes = {}
    prizes['special_prize'] = tree.find(attrs={'id': 'rs_0_0'}).text
    prizes['first_prize'] = tree.find(attrs={'id': 'rs_1_0'}).text
    prizes['second_prize'] = [
        tree.find(attrs={'id': 'rs_2_0'}).text, tree.find(attrs={'id': 'rs_2_1'}).text]
    prizes['third_prize'] = [
        tree.find(attrs={'id': 'rs_3_{}'.format(i)}).text for i in range(6)]
    prizes['fourth_prize'] = [
        tree.find(attrs={'id': 'rs_4_{}'.format(i)}).text for i in range(4)]
    prizes['fifth_prize'] = [
        tree.find(attrs={'id': 'rs_5_{}'.format(i)}).text for i in range(6)]
    prizes['sixth_prize'] = [
        tree.find(attrs={'id': 'rs_6_{}'.format(i)}).text for i in range(3)]
    prizes['seventh_prize'] = [
        tree.find(attrs={'id': 'rs_7_{}'.format(i)}).text for i in range(4)]
    return prizes


def check_win(args):
    prizes = get_prizes()
    last_2_prize_nums = []
    for prize_name, prize in prizes.items():
        if isinstance(prize, list) == False:
            last_2_prize_nums.append(prize[-2:])
        else:
            last_2_prize_nums.extend([prize_num[-2:] for prize_num in prize])
    win_numbers = []
    for ticket_num in args:
        if len(str(ticket_num)) < 2:
            print('gia tri {} thieu chu so'.format(ticket_num))
            continue
        elif str(ticket_num)[-2:] in last_2_prize_nums:
            win_numbers.append(ticket_num)
            print('so {} trung giai lo to'.format(ticket_num))
    if win_numbers == []:
        print('chuc ban may man lan sau, cac giai thuong so so lan nay la:')
        for prize_name, prize in prizes.items():
            print(prize_name, ':', prize)


def main():
    parse = argparse.ArgumentParser(description='Enter your lottery number')
    parse.add_argument('prize_num', nargs="*", help='add your lottery numbers')
    prize_nums = parse.parse_args().prize_num
    check_win(prize_nums)


    # print(prize_nums)
if __name__ == '__main__':
    main()
