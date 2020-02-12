# About Printjack
Printers are common devices whose networked use is vastly unsecured, perhaps due to an enrooted assumption that their services are somewhat negligible and, as such, unworthy of protection.

This repository contains the code shown in the article article "You Overtrust Your Printer" [[Article]](https://link.springer.com/chapter/10.1007/978-3-030-26250-1_21) 
The article evaluates some of the possible consequences of the use of raw 9100 port printing.

### Printjack 2 attack: paper DoS
By looking at it from the inside out, we see a loop that sends each line, stored in textlines, of a bot ASCII file bot.txt, stored in textfile, to a printer for a thousand times. The bot file could contain anything that the attacker may want to print in order to process and spoil paper sheets. The printer is identified via its IP address, and a socket connects to its 9100 port. The outermost loop ranges on the target IP addresses, which are read from file IPs.txt.