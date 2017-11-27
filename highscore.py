import json


# 保存最高分数到json
def save_json(high_score):
    filename = 'highscore.json'
    with open(filename, 'w') as file_object:
        json.dump(high_score, file_object)


# 从json文件中读取最高分数
def load_json():
    filename = 'highscore.json'
    with open(filename) as file_object:
        return json.load(file_object)
