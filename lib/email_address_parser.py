import re

class EmailAddressParser:
  """
  Parses a string of email addresses into a list.
  """

  def __init__(self, email_addresses):
    """
    Initializes the parser with a string of email addresses.
    """
    self.email_addresses = email_addresses.strip()  # Remove leading/trailing whitespace

  def parse(self):
    """
    Parses the email addresses string into a list of unique, sorted email addresses.
    """
    # Split the string using commas or whitespace as delimiters
    emails = re.split(r",\s*|\s+", self.email_addresses)

    # Remove empty entries and filter out non-email strings
    emails = [email for email in emails if email and re.match(r"^[^@]+@[^@]+\.[^@]+$", email)]

    # Convert to a set to get unique values
    unique_emails = set(emails)

    # Convert back to a list and sort alphabetically
    return sorted(list(unique_emails))
