import pronotepy
from config import user, password, url_webhook, url_redirection, ent
from discord_webhook import DiscordWebhook , DiscordEmbed

client = pronotepy.Client(url_redirection,
                          username=user,
                          password=password,
                          ent=ent)

class DiscordTemplate :

    def __init__(self):
        self.url = url_webhook

    def send(self, note, name):
        webhook = DiscordWebhook(url=self.url)

        embed = DiscordEmbed(title=note.subject.name, color='03b2f8',url=url_redirection)
        embed.set_author(name=f'Nouvelle note Pour {name} !')

        embed.set_timestamp()
        embed.add_embed_field(name=f'Note : ?/{note.out_of}', value="\u200b")

        webhook.add_embed(embed)
        response = webhook.execute()
        return response

                        