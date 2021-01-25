import requests

def read_key():
    with open('/home/nearha/myprivvacy/DESIRE/python.vn/ex9/api_keys.txt') as f:
        return f.readline()[:-1]
def read_token():
    with open('/home/nearha/myprivvacy/DESIRE/python.vn/ex9/token.txt') as f:
        return f.readline()[:-1]

class Board:
    def __init__(self ,key, token, name):
        self.name = name
        self.key = key
        self.token = token
        url = "https://api.trello.com/1/boards/"
        query = {
           'key': self.key,
           'token': self.token,
            'name': self.name
        }
        self.response = requests.request(
           "POST",
           url,
           params=query
        )
    def take_id(self):
        return self.response.json()['id']
class List:
    def __init__(self ,key, token, name, idBoard):
        self.name = name
        self.key = key
        self.token = token
        self.idBoard = idBoard
        url = "https://api.trello.com/1/lists"

        query = {
           'key': self.key,
           'token': self.token,
           'name': self.name,
           'idBoard': self.idBoard
        }

        self.response = requests.request(
           "POST",
           url,
           params=query
        )


    def take_id(self):
        return self.response.json()['id']
class Card:
    def __init__(self ,key, token, name, idList, dueTime):
        self.name = name
        self.key = key
        self.token = token
        self.idList = idList
        self.dueTime = dueTime
        url = "https://api.trello.com/1/cards"

        query = {
           'key': self.key,
           'token': self.token,
           'name': self.name,
           'idList': self.idList,
            'due': dueTime
        }

        self.response = requests.request(
           "POST",
           url,
           params=query
        )


    def take_id(self):
        return self.response.json()['id']
def due_date_format(date_time):
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return month_list[date_time.month - 1] + date_time.strftime(" %d, %Y")
def main():
    key = read_key()
    token = read_token()
    board = Board(key, token, 'my_class3')
    id_board = board.take_id()
    thu3_list = List(key, token, 'Thu 3', id_board)
    thu5_list = List(key, token, 'Thu 5', id_board)
    starting_date = datetime.date(2020, 6, 25)
    for lession_number in range(1, 13):
        date_time = starting_date if lession_number == 1 else date_time + datetime.timedelta(days = 5)
        due_time = due_date_format(date_time)
        if lession_number % 2 == 0:
            id_list = thu3_list.take_id()
        else:
            id_list = thu5_list.take_id()
        name = 'Bai {}'.format(lession_number)
        card = Card(key, token, name, id_list, due_time)

if __name__ == '__main__':
    main()