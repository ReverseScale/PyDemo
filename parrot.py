# import parrot_core
from parrot_core import parrotcore as bad_bird


# 鹦鹉学舌
active = True
while active:
    # parrot = '鹦鹉: 主人，跟我说一句话，然后我学给你听！'
    # master = '\n主人: '
    # message = input(parrot + master)
    # print('鹦鹉: ' + message + '~')

    # parrot_core.parrotcore()
    bad_bird()

    quit_order = input('鹦鹉: 主人，还玩不玩了' + '\n(玩/不玩)')
    if (quit_order != '不玩') & (quit_order != '不玩了'):
        active = True
    else:
        active = False