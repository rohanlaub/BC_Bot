import discord
import responses

student_prefix = 'bc_'
src_prefix = 'src_'
technical_prefix = 'tech_'


# Controls student access to commands
async def send_student_message(message, user_message, private):
    try:
        response = responses.handle_student_response(user_message)
        await message.author.send(response) if private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Controls SRC | Technical exclusive commands
async def send_tech_message(message, user_message, private):
    try:
        response = responses.handle_technical_response(user_message)
        await message.author.send(response) if private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Controls access to SRC exclusive commands
async def send_src_message(message, user_message, private):
    try:
        response = responses.handle_src_response(user_message)
        await message.author.send(response) if private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)

    messages = {
        ""
    }

    # Output bot is online
    @client.event
    async def on_ready():
        print(f'{client.user} is ready')

    @client.event
    async def on_member_join(member):
        channel = client.get_channel(1069988373856534611)
        await channel.send(f'{member.mention} welcome to the Belgium Campus Discord.\n\n'
                           f'Please navigate to <#1069989154961768549> to read and accept the rules for the server.\n'
                           f'Once you accept the rules you will be granted the necessary roles to navigate the server.\n'
                           f'________________________________________________________________')

    # Respond to messages
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said \'{user_message}\' : {channel}')

        # TODO: ? impend free speech (profanity filter)

        # BC Students
        if (user_message[0:len(student_prefix)] == student_prefix) and (channel == 'support'):
            user_message = user_message[len(student_prefix):]
            await send_student_message(message, user_message, private=False)

        # SRC
        elif (user_message[0:len(src_prefix)] == src_prefix) and (channel == 'src-support'):
            user_message = user_message[len(src_prefix):]
            await send_src_message(message, user_message, private=False)

        # Technical
        elif user_message[0:len(technical_prefix)] == technical_prefix and \
                (username == 'chkn#3704') or (username == 'Strix#2261'):
            if user_message == 'tech_clear':
                await message.channel.purge()
            else:
                user_message = user_message[len(technical_prefix):]
                await send_tech_message(message, user_message, private=False)

    # Reaction Roles (add / remove)
    @client.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id

        # Verification role
        if message_id == 1074745907507118250:
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            if payload.emoji.name == 'checked':
                role = discord.utils.get(guild.roles, name='verified')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print(f'{member.display_name}#{member.discriminator} has been given the {role} role.')
                else:
                    print('Member not found.')
            else:
                print(f'role not found.')

        # Student Year and club roles
        elif message_id == 1070000699859009566:
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            # role assignments based on emojis
            if payload.emoji.name == 'one':
                role = discord.utils.get(guild.roles, name='1st Year')
            elif payload.emoji.name == 'two':
                role = discord.utils.get(guild.roles, name='2nd Year')
            elif payload.emoji.name == 'three':
                role = discord.utils.get(guild.roles, name='3rd Year')
            elif payload.emoji.name == 'four':
                role = discord.utils.get(guild.roles, name='4th Year')

            elif payload.emoji.name == 'Chess_club':
                role = discord.utils.get(guild.roles, name='Chess club')
            elif payload.emoji.name == 'Book_club':
                role = discord.utils.get(guild.roles, name='Book club')
            elif payload.emoji.name == 'Cybersecurity_club':
                role = discord.utils.get(guild.roles, name='Cybersecurity club')
            elif payload.emoji.name == 'Media_club':
                role = discord.utils.get(guild.roles, name='Media club')
            elif payload.emoji.name == 'Music_and_Dance_club':
                role = discord.utils.get(guild.roles, name='Music & Dance club')
            elif payload.emoji.name == 'Photography_club':
                role = discord.utils.get(guild.roles, name='Photography club')
            elif payload.emoji.name == 'SASL_club':
                role = discord.utils.get(guild.roles, name='SASL club')
            elif payload.emoji.name == 'Software_club':
                role = discord.utils.get(guild.roles, name='Software club')
            elif payload.emoji.name == 'Gaming_club':
                role = discord.utils.get(guild.roles, name='Gaming club')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print(f'{member.display_name}#{member.discriminator} has been given the {role} role.')
                else:
                    print('Member not found.')
            else:
                print(f'role {role} not found.')

        # SRC roles
        elif message_id == 1071063035717890062:
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            if payload.emoji.name == 'SRC_Presidents':
                role = discord.utils.get(guild.roles, name='SRC | President')
            elif payload.emoji.name == 'SRC_Admin':
                role = discord.utils.get(guild.roles, name='SRC | Admin')
            elif payload.emoji.name == 'SRC_Clubs':
                role = discord.utils.get(guild.roles, name='SRC | Clubs')
            elif payload.emoji.name == 'SRC_Discipline':
                role = discord.utils.get(guild.roles, name='SRC | Discipline')
            elif payload.emoji.name == 'SRC_Events':
                role = discord.utils.get(guild.roles, name='SRC | Events')
            elif payload.emoji.name == 'SRC_Finance':
                role = discord.utils.get(guild.roles, name='SRC | Finance')
            elif payload.emoji.name == 'SRC_Marketing':
                role = discord.utils.get(guild.roles, name='SRC | Marketing')
            elif payload.emoji.name == 'SRC_Outreach':
                role = discord.utils.get(guild.roles, name='SRC | Outreach')
            elif payload.emoji.name == 'SRC_Res_Reps':
                role = discord.utils.get(guild.roles, name='SRC | Res Rep')
            elif payload.emoji.name == 'SRC_Sport':
                role = discord.utils.get(guild.roles, name='SRC | Sport')
            elif payload.emoji.name == 'SRC_Student_Relations':
                role = discord.utils.get(guild.roles, name='SRC | Student Relations')
            elif payload.emoji.name == 'Software_club':
                role = discord.utils.get(guild.roles, name='SRC | Technical')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print(f'{member.display_name}#{member.discriminator} has been given the {role} role.')
                else:
                    print('Member not found.')
            else:
                print(f'role {role} not found.')

    @client.event
    async def on_raw_reaction_remove(payload):
        message_id = payload.message_id

        # Verification role
        if message_id == 1074745907507118250:
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            if payload.emoji.name == 'checked':
                role = discord.utils.get(guild.roles, name='verified')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.edit(roles=[])
                    print(f'{role} has been revoked from {member.display_name}#{member.discriminator}.')
                else:
                    print('Member not found.')
            else:
                print(f'role not found.')

        # Student Year and club roles
        if message_id == 1070000699859009566:
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            # role assignments based on emojis
            if payload.emoji.name == 'one':
                role = discord.utils.get(guild.roles, name='1st Year')
            elif payload.emoji.name == 'two':
                role = discord.utils.get(guild.roles, name='2nd Year')
            elif payload.emoji.name == 'three':
                role = discord.utils.get(guild.roles, name='3rd Year')
            elif payload.emoji.name == 'four':
                role = discord.utils.get(guild.roles, name='4th Year')

            elif payload.emoji.name == 'Chess_club':
                role = discord.utils.get(guild.roles, name='Chess club')
            elif payload.emoji.name == 'Book_club':
                role = discord.utils.get(guild.roles, name='Book club')
            elif payload.emoji.name == 'Cybersecurity_club':
                role = discord.utils.get(guild.roles, name='Cybersecurity club')
            elif payload.emoji.name == 'Media_club':
                role = discord.utils.get(guild.roles, name='Media club')
            elif payload.emoji.name == 'Music_and_Dance_club':
                role = discord.utils.get(guild.roles, name='Music & Dance club')
            elif payload.emoji.name == 'Photography_club':
                role = discord.utils.get(guild.roles, name='Photography club')
            elif payload.emoji.name == 'SASL_club':
                role = discord.utils.get(guild.roles, name='SASL club')
            elif payload.emoji.name == 'Software_club':
                role = discord.utils.get(guild.roles, name='Software club')
            elif payload.emoji.name == 'Gaming_club':
                role = discord.utils.get(guild.roles, name='Gaming club')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(f'{role} has been revoked from {member.display_name}#{member.discriminator}.')
                else:
                    print('Member not found.')
            else:
                print(f'role: {role} not found.')

        # SRC roles
        elif message_id == 1071063035717890062:
            guild = discord.utils.find(lambda g: g.id == payload.guild_id, client.guilds)

            if payload.emoji.name == 'SRC_Presidents':
                role = discord.utils.get(guild.roles, name='SRC | President')
            elif payload.emoji.name == 'SRC_Admin':
                role = discord.utils.get(guild.roles, name='SRC | Admin')
            elif payload.emoji.name == 'SRC_Clubs':
                role = discord.utils.get(guild.roles, name='SRC | Clubs')
            elif payload.emoji.name == 'SRC_Discipline':
                role = discord.utils.get(guild.roles, name='SRC | Discipline')
            elif payload.emoji.name == 'SRC_Events':
                role = discord.utils.get(guild.roles, name='SRC | Events')
            elif payload.emoji.name == 'SRC_Finance':
                role = discord.utils.get(guild.roles, name='SRC | Finance')
            elif payload.emoji.name == 'SRC_Marketing':
                role = discord.utils.get(guild.roles, name='SRC | Marketing')
            elif payload.emoji.name == 'SRC_Outreach':
                role = discord.utils.get(guild.roles, name='SRC | Outreach')
            elif payload.emoji.name == 'SRC_Res_Reps':
                role = discord.utils.get(guild.roles, name='SRC | Res Rep')
            elif payload.emoji.name == 'SRC_Sport':
                role = discord.utils.get(guild.roles, name='SRC | Sport')
            elif payload.emoji.name == 'SRC_Student_Relations':
                role = discord.utils.get(guild.roles, name='SRC | Student Relations')
            elif payload.emoji.name == 'Software_club':
                role = discord.utils.get(guild.roles, name='SRC | Technical')
            else:
                role = None

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(f'{role} has been revoked from {member.display_name}#{member.discriminator}')
                else:
                    print('Member not found.')
            else:
                print('role not found.')
                
    TOKEN = os.getenv("TOKEN")
    client.run(TOKEN)
