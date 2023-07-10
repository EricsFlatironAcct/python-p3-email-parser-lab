import re
# your code goes here!
class EmailAddressParser:
   def __init__(self, email_addresses):
      self.all = email_addresses
   def parse(self):
      email_pattern = r"^[A-z][\w]*\.{0,1}[\w]+@[A-z]+.[A-z]+"
      parse_pattern = r"[,]+\s{0,1}|\s{1}"
      email_list = re.split(parse_pattern, self.all)
      email_list = [email for email in email_list if re.fullmatch(email_pattern, email)]
      return sorted(email_list)
