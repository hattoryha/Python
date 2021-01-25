import requests
import bs4
import argparse
def get_questions(N, tag):
#     tag = 'python'
    url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=votes&tagged={}&site=stackoverflow'.format(tag)
    r = requests.get(url)
    api_data = r.json()
    api_item = api_data['items']
#     N = 1000
    questions = []
    for question_index in range(N):
        try:
            questions.append(api_item[question_index]['title'])
            print(api_item[question_index]['title'])
        except IndexError:
            print('there are only {} questions related to the tag'.format(len(api_item)).upper())
            break
def main():
    parser = argparse.ArgumentParser(description='Enter N and tag to find N the highest voted questions with this tag')
    parser.add_argument("N", type=int)
    parser.add_argument("tag", type=str)
    N = parser.parse_args().N
    tag = parser.parse_args().tag
    get_questions(N, tag)
if __name__ == "__main__":
    main()