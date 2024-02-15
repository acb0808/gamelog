def get_log(date:str):
    if not isinstance(date, str):
        return ValueError('argument `date` must be str type')
    if len(date) != 8:
        raise ValueError('argument `date` must be 8 letter ex) 20241005')
    log = {
        'game' : [],
        'info' : {}
    }
    with open(f'./log/{date}.log', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        for row in data:
            if row.startswith('#'):
                row = row[1:]
                key, *val = row.replace(' ', '').split(':')
                log['info'][key]= ':'.join(val)
                continue

            game = row.split(' ')
            log['game'].append({
                'champ': game[0],
                'result' : game[1],
                'kda' : game[2],
                'etc' : game[3]
            })
    return log

def save_json(filename, obj):
    import json
    data = json.dumps(obj)
    open(f'./json/{filename}.json', 'w', encoding='utf-8').write(data)
    return

date = '20240216'
data = get_log(date)
save_json(date, data)