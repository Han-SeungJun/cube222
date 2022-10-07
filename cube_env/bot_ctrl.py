import telepot

bot = telepot.Bot(token='') # here put a token
chat_id = '' # here put an id

def control(msg, _object):
    if msg['text'] == 'u':
        _object.upRight()
        spin_U()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "윗면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'U':
        _object.upLeft()
        spin_U()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "윗면을 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'd':
        _object.downRight()
        spin_D()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "아래면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'D':
        _object.downLeft()
        spin_D()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "아래면을 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'r':
        _object.rightRight()
        spin_R()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "오른쪽 면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'R':
        _object.rightLeft()
        spin_R()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "오른쪽 면을 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'l':
        _object.leftRight()
        spin_L()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "왼쪽 면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'L':
        _object.leftLeft()
        spin_L()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "왼쪽 면을 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'f':
        _object.frontRight()
        spin_F()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "앞면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'F':
        _object.frontLeft()
        spin_F()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "앞면을 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'b':
        _object.backRight()
        spin_B()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "뒷면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'B':
        _object.backLeft()
        spin_B()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "뒷면을 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'x':
        _object.xRight()
        spin_All()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "앞면을 기준으로 큐브 전체를 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'X':
        _object.xLeft()
        spin_All()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "앞면을 기준으로 큐브 전체를 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'y':
        _object.yRight()
        spin_All()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "오른쪽 면을 기준으로 큐브 전체를 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'Y':
        _object.yLeft()
        spin_All()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "오른쪽 면을 기준으로 큐브 전체를 반시계방향으로 돌리겠습니다")
    elif msg['text'] == 'z':
        _object.zRight()
        spin_All()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "윗면을 기준으로 큐브 전체를 시계방향으로 돌리겠습니다")
    elif msg['text'] == 'Z':
        _object.zLeft()
        spin_All()
        time.sleep(TIME)
        bot.sendMessage(msg['from']['id'], "윗면을 기준으로 큐브 전체를 반시계방향으로 돌리겠습니다")
        
bot.message_loop(control)
