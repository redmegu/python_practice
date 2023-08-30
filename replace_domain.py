def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
    else:
        new_email = email
    print("Your old email is: " + email)
    print("Your new email is: " + new_email)

replace_domain("deopapa123@ellaclub.com", "ellaclub", "ellafanclub")