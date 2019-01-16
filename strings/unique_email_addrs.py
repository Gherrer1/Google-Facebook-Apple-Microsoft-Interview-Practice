# 929. Unique Email Addresses
def get_num_unique_email_addresses(emails):        
    email_exists = {}
    num_unique_emails = 0
    for email in emails:
        local_name, domain_name = email.split('@')
        std_local_name = ''.join(local_name.split('+')[0].split('.'))
        email = std_local_name + '@' + domain_name
        if not email in email_exists:
            email_exists[email] = True
            num_unique_emails += 1
    return num_unique_emails