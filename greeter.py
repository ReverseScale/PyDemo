import uuid

# 招待员
def greet_user(name='新客人', shop='风俗店'):
    print('欢迎光临' + shop + ', ' + name + '！')
    return '请拿好您的手牌' + voucher() + ', 里面请~' 

# 长度15字符的手牌号
def voucher(length=16):
    temp = uuid.uuid1()
    return str(temp).replace('-', '')[:length]
# 客官选择的类型
def likeType(type='D'):
    numbers = {
        'A' : '客官喜欢瓜子脸的~',
        'B' : '客官喜欢大胸脯的~',
        'C' : '客官喜欢大长腿的~',
        'D' : '给客官找个样样都行的~'
    }

    return numbers.get(type, None)

print(greet_user('老王', '天上人间'))
print(greet_user(name='老李',shop='红浪漫洗浴中心'))
print(greet_user(name='客官'))

while True:
    print('新店大酬宾, 大保健欢迎您，祝您越来越开心！！！')
    customer = input('招待员: 先生请问怎么称呼呢？\n叫我: ')
    like = input('招待员: 喜欢什么类型呢？\n A:瓜子脸 B:大胸脯 C:大长腿 D:小孩子才选择, 我都要\n我选: ')
    print(greet_user(customer))
    print(likeType(like))
    print('---------------------------------->')

