
app_ids = ['1589315738', '1579386373']
def get_app_id():
    with open('applist.txt') as f:
        lines = f.readlines()
        app_id = []
        for line in lines:
            if len(line) < 15:
                app_id.append(line.strip())
    return app_id

def get_play_id():
    with open('applist.txt') as f:
        lines = f.readlines()
        play_id = []
        for line in lines:
            if len(line) > 15:
                play_id.append(line.strip())
    return play_id
