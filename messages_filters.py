"Messages Filters"


def are_mentions_allowed(channel):
    'Checks if the channel allows mentions'

    channel = str(channel)
    return channel == 'spam' or channel == 'spam-menzioni'


def are_embeds_allowed(channel):
    'Checks if the channel allows embeds'

    channel = str(channel)
    return channel == 'spam'


def are_attachments_allowed(channel):
    'Checks if the channel allows attachments'

    channel = str(channel)
    return channel == 'spam'


def check_embeds(embeds):
    'Checks if message contains embeds'

    for embed in embeds:
        if embed:
            return True
    return False


def check_attachments(attachments):
    'Checks if message contains attachments'

    for attachment in attachments:
        if attachment:
            return True
    return False


def check_mentions(mentions):
    'Checks if message contains mentions'

    for mention in mentions:
        if mention:
            return True
    return False
