from requests import get, post, delete, put

'''
# нет json
print(post('http://localhost:5000/api/jobs').json())

# нехватка аргументов
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1}).json())

# неверный аргумент
print(post('http://localhost:5000/api/jobs',
           json={'title': 'Заголовок'}).json())

# id уже есть
print(post('http://localhost:5000/api/jobs',
           json={'id': 1, 'team_leader': 1, 'job': 'test', 'work_size': 15, 'collaborators': '3, 4', 'hazard': 2, 'is_finished': False}).json())

# всё верно
print(post('http://localhost:5000/api/jobs',
           json={'id': 5, 'team_leader': 1, 'job': 'test', 'work_size': 15, 'collaborators': '3, 4', 'hazard': 2, 'is_finished': False}).json())

# проверка добавки
print(get('http://localhost:5000/api/jobs').json())
'''

# верно
print(put('http://localhost:5000/api/jobs',
           json={'id': 1, 'team_leader': 1, 'job': 'test_changed', 'work_size': 17, 'collaborators': '3, 4', 'hazard': 2, 'is_finished': False}).json())

# нет id
print(put('http://localhost:5000/api/jobs',
           json={'id': 5, 'team_leader': 1, 'job': 'test_сhanged', 'work_size': 15, 'collaborators': '3, 4', 'hazard': 2, 'is_finished': False}).json())

print(get('http://localhost:5000/api/jobs').json())