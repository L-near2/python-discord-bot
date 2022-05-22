import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in Successfully')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '```[>Start```':
            await message.channel.send("[Digital root](https://en.wikipedia.org/wiki/Digital_root) is the _recursive sum of all the digits in a number._\n\nGiven `n`, take the sum of the digits of `n`. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.\n\n## Examples\n```\n    16  --\u003e  1 + 6 = 7\n   942  --\u003e  9 + 4 + 2 = 15  --\u003e  1 + 5 = 6\n132189  --\u003e  1 + 3 + 2 + 1 + 8 + 9 = 24  --\u003e  2 + 4 = 6\n493193  --\u003e  4 + 9 + 3 + 1 + 9 + 3 = 29  --\u003e  2 + 9 = 11  --\u003e  1 + 1 = 2\n```\n")

client = MyClient()
client.run('OTc3NjQzOTE4NDkxNTI5MzI2.G7jTcC.p7hJBH1Ugl76D6GW7ft9WsxCFtPPsbtw_OypLQ')