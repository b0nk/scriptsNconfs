__module_name__ = "Hexchat Slap Plugin"
__module_version__ = "0.1"
__module_description__ = "A variety of slaps"
__author__ = "b0nk"

import xchat as XC
from random import choice

slapList = []
slapList.append("slaps %s around a bit with a large trout")
slapList.append("strikes down upon %s with great vengeance and furious anger!")
slapList.append("slaps %s's shit")
slapList.append("slaps %s around a bit with a 200kg tuna")
slapList.append("slaps %s across the channel")
slapList.append("shitslapped %s")
slapList.append("slaps %s with a bag of dicks")
slapList.append("shits down %s's throat")
slapList.append("pisses down %s's throat")
slapList.append("rips out %s's intestins and slaps him/her with them")
slapList.append("enables the backdoor feature for IRC and steals all %s's nude pics")
slapList.append("slaps %s into 1955")
slapList.append("slaps %s with an educational video about science and astro physics!")
slapList.append("pimp slaps %s")
slapList.append("slaps %s with a freezer")
slapList.append("slaps %s with a telephone pole!")
slapList.append("slaps %s around a bit with a large Cod")
slapList.append("slaps %s with an alarm clock")
slapList.append("slaps %s with a very large banana")
slapList.append("slaps %s with his very own hand")
slapList.append("smacks %s in the eye with a large HOT sausage")
slapList.append("throws a keyboard at %s")
slapList.append("discovers %s's picture at uglypeople.com")
slapList.append("smacks %s with a PC screen")
slapList.append("slaps %s around the head with a big dummy!")
slapList.append("sneezes in %s's face")
slapList.append("gets his gun out and points it at %s")
slapList.append("follows %s into a dark avenue. \"Hey, test my crowbar!\"")
slapList.append("hits %s in the head with a frying pan *WHAM*!")
slapList.append("sets %s's clothes on fire")
slapList.append("throws a custard pie at %s")
slapList.append("puts jelly in %s's hot god")
slapList.append("slaps %s around a bit with a large pig")
slapList.append("slaps %s around a bit with a large horse")
slapList.append("slaps %s around a bit with a large cat")
slapList.append("slaps %s around a bit with a Big Mac")
slapList.append("slaps %s around a bit with a large dog")
slapList.append("slaps %s around a bit with a computer")
slapList.append("slaps %s around a bit with a stolen car")
slapList.append("slaps %s with a brick")
slapList.append("can't wait for %s to be a useless piece of shit all day and play all those games")
slapList.append("slaps %s around a bit with a Whopper")
slapList.append("slaps %s around a bit with a bucket of fried chicken")
slapList.append("exposes %s to a radioactive ebola virus")
slapList.append("slaps %s around a bit with a Double Whopper")
slapList.append("slaps %s with the strength of a thousand suns")
slapList.append("coughs in %s's face")
slapList.append("cockslaps %s's face")
slapList.append("beats %s to death with a 12inch black dildo")
slapList.append("stabs %s with a spoon")
slapList.append("slaps a large trout around a bit with %s, now you know how it feels.")
slapList.append("drops an Acme Anvil on %s")
slapList.append("grabs %s's underwear, pulls it over its head... Now you look much better. The brown stain accentuates the shoes")
slapList.append("thinks the only way %s can look better is with a bottle of vodka and a joint")
slapList.append("thinks that %s REALLY needs a BATH... :)")
slapList.append("whips %s with a wet noodle")
slapList.append("hits %s in the head with a sledge hammer and then hands it an Aspirin")
slapList.append("slaps %s's face so hard, it has to walk backwards from now on to see where its going")
slapList.append("slaps some sense into %s with a red brick")
slapList.append("warns %s: Don't make the same mistake your parents did... use birth control")
slapList.append("rams a fork up %s's nose")
slapList.append("slaps %s with a huge law suit")
slapList.append("slaps %s with a great big, wet, 100% rubber DUCK!")
slapList.append("pees on %s's leg")
slapList.append("whips %s's ass really hard!")
slapList.append("rips %s's arm off and beat him/her with it")
slapList.append("asks %s: Do you feel lucky? Well do ya.. punk?")
slapList.append("doesn't think %s knows who they are messing with")
slapList.append("sneaks into %s's place & replaces the computer with an 8088 processor with no sound card, no CD-Rom drive, a 20 Meg HD, 512k RAM, 1200 baud modem & a monochrome monitor")
slapList.append("sneakes over to %s's house and puts some LSD into its glass of Coke")
slapList.append("slaps %s with a large dildo")
slapList.append("Poem for %s: Roses are red, violets are blue.. I was made beautiful, what the fuck happened to you?")
slapList.append("tells %s, the only difference between your mother and a subway is that not EVERYBODY has ridden a subway")
slapList.append("says your mom is like an elevator %s, if you push the right button she'll go down on you")
slapList.append("says your mom is like a shotgun %s, one cock and she's ready to blow")
slapList.append("says your mom is like a racecar %s, she can burn four rubbers in one night but she is going to have to pay me")
slapList.append("says Yo moma is so fat %s anyone can turn her on")
slapList.append("tells %s when I see a christmas card that says \"Ho-Ho-Ho!\", I know to address it to your mom")
slapList.append("asks if that is an accent %s, or is that your mouth just full of sperm")
slapList.append("says if I would had 10 bucks %s, I could have been your dad, but the guy in front of me had exact change")
slapList.append("says you're like a light switch %s, even a little kid can turn you on")
slapList.append("says to %s, your mom is so fat that she had to get baptized at sea world")
slapList.append("tells %s, your mom is so fat that she's got more chins than a chinese phone book")
slapList.append("says your mom is so fat %s that you gotta grease the tub to get her in the bath")
slapList.append("shreds %s with a chainsaw")
slapList.append("slaps %s with the Windows 2000 buglist")
slapList.append("bitchslaps %s")
slapList.append("before %s could attack, banged his staff down in to the ground shattering the earth and shouted \"YOU SHALL NOT PASS!\"")
slapList.append("curses %s in the deepest pits of hell")
slapList.append("slaps %s with a long lariat")

def slaps(word, word_eol, userdata):
  try:
    slap = choice(slapList)
    XC.command('me ' + slap % word[1])
  except:
    print 'error'

XC.hook_command("slap", slaps, help="/slap <nick>")
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
