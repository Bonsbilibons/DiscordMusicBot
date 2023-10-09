import discord

def usual_responses(message):
    r_massage = message.lower()

    if r_massage == "!help":
        return '!play + usl of music (now support only YouTube) !stop !pause !resume'

    elif r_massage == '!stop':
        return 'The composition is stopped'

    elif r_massage == '!pause':
        return 'The composition is on a paused'

    elif r_massage == '!resume':
        return 'The composition is continue playing'

    else:
        return 'Ти їбанувся?'