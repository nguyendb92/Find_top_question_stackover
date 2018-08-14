from requests_html import HTMLSession
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('N', help="Top N questions on stackoverflow", type=int)
parser.add_argument('label', help="tag of question on page", type=str)
args = parser.parse_args()

session = HTMLSession()
url = 'https://api.stackexchange.com/2.2/questions?'
option = 'pagesize={}&order=desc&sort=votes&tagged={}&site=stackoverflow'

resp = session.get(url+option.format(args.N, args.label))
resp = resp.json()
print(resp['items'][0]['title'], '\n', resp['items'][0]['link'])
