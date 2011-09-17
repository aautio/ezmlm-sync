from app import events

def run():
    email = open('tests/email_confirm_subscribe.txt').read()
    assert events.ConfirmSubscribeEvent().matches(email)

