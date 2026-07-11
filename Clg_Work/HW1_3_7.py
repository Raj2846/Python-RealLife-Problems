"""The Spam Detector (Search in Stream) linear Search 
A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against a blacklist of known spam sender IDs. The blacklist has no order.
"""

black_list=[
    "spam123@gmail.com",
    "offers@fakebank.com",
    "winner@lottery.com",
    "ads@spam.com",
    "scam@fraud.com"
]

rec_email=input("Enter the sender email :")

found=False
if rec_email in black_list:
    print("Spam detected! Sender is blacklisted.")
else:
    print("Safe email. Sender not found in blacklist.")