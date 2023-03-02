import json_filehandler as db

# TODO: Decide if any private messaging is necessary and apply

# TODO: add commands (get suggestions from src)
# TODO: JSON file for FAQ

# TODO: Add ticket system
# ?TODO: add nickname command limited uses
# ?TODO: textfile log


# SRC
def handle_src_response(message: str) -> str:
  p_message = message.lower()

  if p_message == 'help':
    return '```' \
           '<src_help> : Gives you this list.\n' \
           '<src_members <Optional: "Department">> : Gives you the contact info of all src members.\n' \
           '<src_search "SRC name"> : Gives you the contact details of a specific SRC Member.\n' \
           '<src_add faq> : Gives you the link to add a FAQ.\n' \
           '<src_request poster> : Gives you the link to request a poster from Marketing.\n' \
           '```'

  if p_message[:6] == 'search':
    try:
      output = ''
      member_found = db.Search_member(p_message[7:], search_field='name')
      output += f'{member_found["department"]} - __{member_found["name"]}__ - *{member_found["contact"]}*\n'

      return output
    except Exception as e:
      print(e)
      return ':exclamation:`Member not found`'

  if p_message[:7] == 'members':
    try:
      output = ''
      if p_message[8:] == '':
        for obj in db.gib('members'):
          if not obj["hod"]:
            output += f'{obj["department"]} - __{obj["name"]}__ - *{obj["contact"]}*\n'
          else:
            output += f'\n**(HOD) {obj["department"]}** - __{obj["name"]}__ - *{obj["contact"]}*\n'

        return output
      else:
        for obj in db.Search_department(p_message[8:]):
          if not obj["hod"]:
            output += f'{obj["department"]} - __{obj["name"]}__ - *{obj["contact"]}*\n'
          else:
            output += f'\n**(HOD) {obj["department"]}** - __{obj["name"]}__ - *{obj["contact"]}*\n'

        return output
    except Exception as e:
      print(e)
      return f':exclamation: Error fetching members'

  if p_message == 'request poster':
    return 'Request a Poster from Marketing: https://forms.office.com/r/7xgCU5DvCF'

  if p_message == 'add faq':
    return 'Request to add a FAQ: https://forms.office.com/r/3nZ5GgzEyD'

  # default response
  return ':exclamation: Command not found, try src_help for a list of commands.'


# Technical
def handle_technical_response(message: str) -> str:
  p_message = message.lower()

  if p_message == 'help':
    return '```' \
           '<tech_help> : Prints this list.\n' \
           '<tech_email "message"> : Sends an email to the technical team.\n' \
           '<tech_clear> : Clears messages in the current channel.\n' \
           '<tech_rules> : Prints a list of server rules.\n' \
           '<tech_ticket_text> : Prints the instructions to create a ticket.' \
           '```'

  if p_message == 'rules':
    return '''1. Always be respectful.
2. Do not ping unnecessarily :exclamation: DO NOT @everyone ping.
3. No racism, sexism, homophobic etc comments.
4. Be mindful of working/studying hours when messaging SRC members.
5. Don’t encourage conflict.
6. Don't spam messages.
7. No NSFW content will be tolerated.
8. Do not post false / misleading information.
9. Don't share viruses or malicious software.

React to this message with <:checked:1074744678697680966> to verify that you've read and agree to follow these rules'''

  if p_message == 'ticket_text':
    return '**Creating a Ticket**\n\n' \
           'coming soon...'

  return ':exclamation: Command not found, try tech_help for a list of commands.'
  pass


# Students
def handle_student_response(message: str) -> str:
  p_message = message.lower()

  if p_message == 'help':
    return '```' \
           '<bc_help> : This command returns this list.\n' \
           '<bc_hello> : This command returns a friendly message.\n' \
           '<bc_src <Optional: "Department">> : This command gives you a list of all the SRC members, their department and their contact information.\n' \
           '<bc_faq> : This command gives you a list of frequently asked questions with their answers.\n' \
           '<bc_nick "Your Name and Surname"> : This command changes your server nickname.\n' \
           '<bc_events <Optional: "Event name">> : This command returns a list of the information for all planned events' \
           '```'

  if p_message == 'hello':
    return 'Hello there, I\'m the SRC bot for the BC Discord Server. How can I help?'

  if p_message[:3] == 'src':
    try:
      output = ''
      if p_message[4:] == '':
        for obj in db.gib('members'):
          if not obj["hod"]:
            output += f'{obj["department"]} - __{obj["name"]}__ - *{obj["contact"]}*\n'
          else:
            output += f'\n**(HOD) {obj["department"]}** - __{obj["name"]}__ - *{obj["contact"]}*\n'

        return output
      else:
        for obj in db.Search_department(p_message[4:]):
          if not obj["hod"]:
            output += f'{obj["department"]} - __{obj["name"]}__ - *{obj["contact"]}*\n'
          else:
            output += f'\n**(HOD) {obj["department"]}** - __{obj["name"]}__ - *{obj["contact"]}*\n'

        return output
    except Exception as e:
      print(e)
      return f':exclamation: Error fetching members'

  if p_message == 'faq':
    output_string = ''
        for faq in db.gib('faq'):
            output_string += f'"{faq["q"]}"\nDepartment: {faq[faq["department"]]}\n```{faq["a"]}```'
        
        print(output_string)
        return output_string

  if p_message[:4] == 'nick':
    return 'coming soon...'

  if p_message[:6] == 'events':
    output_string = ''
    search = p_message[7:]

    for event in db.gib('events'):
      if len(search) == 0:
        output_string += f'**{event["department"]}** | _{event["title"]}_\n' \
                  f'**{event["date"]}** : {event["time"]}\n' \
                  f'```{event["description"]}```\n'
      elif search == event["title"]:
        output_string += f'**{event["department"]}** | _{event["title"]}_\n' \
                  f'**{event["date"]}** : {event["time"]}\n' \
                  f'```{event["description"]}```\n'
    return output_string

  # default response
  return 'Command not found, try bc_help for a list of commands.'
