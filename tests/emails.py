from app import emails

def run():
    email = open('tests/email_list.txt').read()
    assert emails.ListEmail().matches(email)

    email = open('tests/email_confirm_subscribe.txt').read()
    assert emails.ConfirmSubscribeEmail().matches(email)

    email = open('tests/email_confirm_unsubscribe.txt').read()
    assert emails.ConfirmUnsubscribeEmail().matches(email)
    
