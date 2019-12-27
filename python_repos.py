import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

print('Status code:', r.status_code)

requests_dict = r.json()

print(requests_dict.keys())

print('Total: ' + str(requests_dict['total_count']))

repo_dicts = requests_dict['items']

print('Repositories returned: ', len(repo_dicts))

