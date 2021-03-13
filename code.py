import random

def generate_ege_task_01():
    left1, right1 = random.randint(250, 260), random.randint(250, 260)
    left2, right2 = random.randint(260, 270), random.randint(260, 270)
    left3, right3 = random.randint(270, 280), random.randint(270, 280)
    answer = 0
    if left1 > right1:
        answer += 1
    if left2 > right2:
        answer += 1
    if left3 > right3:
        answer += 1
    task_text = '''Сколь­ко вер­ных не­ра­венств среди пе­ре­чис­лен­ных:
\t{} > {};
\t{} > {};
\t{} > {}.'''.format(left1, str(bin(right1))[2:], left2, str(bin(right2))[2:], left3, str(bin(right3))[2:])
    return task_text, str(answer)

text, answer = generate_ege_task_01()
print(text)
print(answer)
