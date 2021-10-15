


# The user enters an email
email = input("Please enter your email: ").strip()

# The username starts from the beginning up to the @ symbol
username = email[:email.index("@")]

# print(username)     # display username

# The plus 1 gives me once character
# By adding the colon, that will save the rest of the domain
domain = email[email.index("@") + 1:]

# print(domain)

# Another cool way of displaying the username and email domain
print(f"Your username is {username}")

print(f"Your email is {domain}")