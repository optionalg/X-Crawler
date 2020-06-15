# making a more secure password maker (advance)
## Help PWDs == Root Key - anonymous_root
#               anonymous_Key - anonymous_encrypt, anonymous_decryption
from colorama import Fore, Back, Style

words_lst_high = (('q', '0^1'), ('w','0~1'), ('e','130'), ('r','1*0'), ('t', '0:1'), ('y', '0%1'),
                 ('u', '1_0'), ('i', '1!0'), ('o', '001'), ('p', '091'), ('a', '1@0'), ('s', '1$0'),
                 ('d', '0{1'), ('f', '0}1'), ('g', '1(0'), ('h', '1)0'), ('j', '0/1'), ('k', "0\."),
                 ('l', '1|0'), ('z', '0#1'), ('x', '0?1'), ('c', '1=0'), ('v', '1.0'), ('b', '081'),
                 ('n', '0+1'), ('m', '1-0'), ('Q', '0^1'), ('W','0~1'), ('E','130'), ('R','1*0'), ('T', '0:1'), ('Y', '0%1'),
                 ('U', '1_0'), ('I', '1!0'), ('O', '001'), ('P', '091'), ('A', '1@0'), ('S', '1$0'),
                 ('D', '0{1'), ('F', '0}1'), ('G', '1(0'), ('H', '1)0'), ('J', '0/1'), ('K', "0\."),
                 ('L', '1|0'), ('Z', '0#1'), ('X', '0?1'), ('C', '1=0'), ('V', '1.0'), ('B', '081'),
                 ('N', '0+1'), ('M', '1-0'), (' ', ';;'))



words_lst_med = (('q', '^'), ('w','~'), ('e','3'), ('r','*'), ('t', ':'), ('y', '%'),
                 ('u', '_'), ('i', '!'), ('o', '0'), ('p', '9'), ('a', '@'), ('s', '$'),
                 ('d', '{'), ('f', '}'), ('g', '('), ('h', ')'), ('j', '/'), ('k', "\."),
                 ('l', '|'), ('z', '#'), ('x', '?'), ('c', '='), ('v', '.'), ('b', '8'),
                 ('n', '+'), ('m', '-'))


words_lst_low = (('q', 'Q#'), ('w','W#'), ('e','3'), ('r','R#'), ('t', 'T#'), ('y', 'Y#'),
                 ('u', '_'), ('i', '!'), ('o', '0'), ('p', '9'), ('a', '@'), ('s', '$'),
                 ('d', 'D#'), ('f', 'F#'), ('g', 'G#'), ('h', 'H#'), ('j', 'J#'), ('k', "K#"),

                 ('l', '&'), ('z', '1'), ('x', '?'), ('c', 'C#'), ('v', 'V#'), ('b', '8'),
                 ('n', '+'), ('m', '-'), (' ', ';;'))

symbol_list = (('!', '1!'), ('@', '2@'), ('#','3#'),('$', '4$'), ('%', '5%'),
              ('^', '6^'), ('&', '7&'), ('*', '8*'),('(', '9('), (')' ,'0)'))

decryption_high_lst = (('0^1', 'q'), ('0~1','w'), ('130','e'), ('1*0','r'), ('0:1', 't'), ('0%1', 'y'),
                 ('1_0', 'u'), ('1!0', 'i'), ('001', 'o'), ('091', 'p'), ('1@0', 'a'), ('1$0', 's'),
                 ('0{1', 'd'), ('0}1', 'f'), ('1(0', 'g'), ('1)0', 'h'), ('0/1', 'j'), ('0\.', "k"),
                 ('1|0', 'l'), ('0#1', 'z'), ('0?1', 'x'), ('0?1', 'c'), ('1.0', 'v'), ('081', 'b'),
                 ('0+1', 'n'), ('1-0', 'm'), (';;', ' '))

decryption_medium_lst = (('^', 'q'), ('~','w'), ('e','3'), ('*','r'), (':', 't'), ('%', 'y'),
                 ('_', 'u'), ('!', 'i'), ('0', 'o'), ('9', 'p'), ('@', 'a'), ('$', 's'),
                 ('{', 'd'), ('}', 'f'), ('(', 'g'), (')', 'h'), ('/', 'j'), ('\.', "k"),
                 ('|', 'l'), ('#', 'z'), ('?', 'x'), ('=', 'c'), ('.', 'v'), ('8', 'b'),
                 ('+', 'n'), ('-', 'm'))


decryption_low_lst = (('Q#', 'q'), ('W#','w'), ('3','e'), ('R#','r'), ('T#', 't'), ('Y#', 'y'),
                 ('_', 'u'), ('!', 'i'), ('0', 'o'), ('9', 'p'), ('@', 'a'), ('$', 's'),
                 ('D#', 'd'), ('F#', 'f'), ('G#', 'g'), ('H#', 'h'), ('J#', 'j'), ('K#', "k"),

                 ('&', 'l'), ('1', 'z'), ('?', 'x'), ('C#', 'c'), ('V#', 'v'), ('8', 'b'),
                 ('+', 'n'), ('-', 'm'), (';;', ' '))


decryption_symbols_lst = (('1!', '!'), ('2@', '@'), ('3#','#'),('4$', '$'), ('5%', '%'),
              ('6^', '^'), ('7&', '&'), ('8*', '*'),('9(', '('), ('0)' ,')'))

def number_lst():
    number_lst = (('1', '1!q'), ('2', '2@w'), ('3', '3#e'), ('4', '4$r'), ('5', '5%t'), ('6', '6^y'),
                  ('7', '7&u'), ('8', '*i'), ('9', '9(0'), ('0', '0)P'), (' ', ';;'))

    def encryption_of_numbers(usr_pass5):
        for a, b in number_lst:
            usr_pass5 = usr_pass5.replace(a, b)
        return usr_pass5

    def number():

        import time

        # request 4
        for hacker12 in range(1, 2):
            print('{+} Processing your request...1 for Numbers')
            time.sleep(0.3)
            print('{+} Processing your request...2 for Numbers')
            time.sleep(0.3)
            print('{+} Processing your request...3 for Numbers')
            time.sleep(0.3)
            print('{+} Processing your request...4 for Numbers')
            time.sleep(0.3)
            print('{+} Processing your request...5 for Numbers')
            time.sleep(2)

            print('Starting the PWD Encryting System....')

            time.sleep(1)
            print('-------------------+ Numbers_Encryptions +----------------------')
            print('Started!!')
        time.sleep(0.1)
        print('Enter your password to encrypt-')
        usr_pass5 = input('')
        old_len5 = len(usr_pass5)
        old_type5 = type(usr_pass5)
        print(f'The OLD pwd length is:{old_len5}')
        print(f'The OLD pwd type is:{old_type5}')
        usr_pass5 = encryption_of_numbers(usr_pass5)
        print('-------------------------------------------------')
        new_len5 = len(usr_pass5)
        print(f'The NEW pwd length is:{new_len5}')

        print('The NEW secure password is {}'.format(usr_pass5))

        def pass4():
            print('Note: File will be saved as encrypted_numbers.txt')
            destination = input('Do you want to save the encrypted PWD in a file?[1/0]\n')
            if (destination == '1'):
                try:
                    filename_numbers = 'encrypted_numbers.txt'
                    opening = open(filename_numbers, 'w')

                    opening.write(usr_pass5)
                    opening.close()
                except IOError:
                    print('There is No File such as ' + filename_numbers)

                for hack in range(1, 2):
                    print('Saving.....')
                    import time
                    import os
                    time.sleep(1)
                    print('-----------------------------')
                    print('Done!!')
                    get = os.getcwd()
                    print('Saved Path ==> ' + get)


            elif (destination == '0'):
                main()

            else:
                restart10()

        pass4()

        def restart10():
            restart10 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
            if (restart10 == '1'):
                main()

            elif (restart10 == '0'):
                exit()

            else:
                print('Error')
                print('Lol!')
                print('         _       _')
                print('        | |     | |')
                print('        | | ___ | |')
                print('        | |/ _ \| |')
                print('        | | (_) | |')
                print('        |_|\___/|_|')
                exit()
        restart10()




    number()



def encryption_of_passwords(usr_pass):
    for a, b in words_lst_high:
        usr_pass = usr_pass.replace(a,b)
    return usr_pass

def encryption_of_passwords2(usr_pass2):
    for a,b in words_lst_med:
        usr_pass2 = usr_pass2.replace(a,b)
    return usr_pass2

def encryption_of_passwords3(usr_pass3):
    for a, b in words_lst_low:
        usr_pass3 = usr_pass3.replace(a, b)
    return usr_pass3

def encryption_of_symbol(usr_pass4):
    for a,b in symbol_list:
        usr_pass4 = usr_pass4.replace(a, b)
    return usr_pass4


def decryption_high(usr_pass51):
    for a, b in decryption_high_lst:
        usr_pass51 = usr_pass51.replace(a, b)
    return usr_pass51

def decryption_medium(usr_pass52):
    for a, b in decryption_medium_lst:
        usr_pass52 = usr_pass52.replace(a, b)
    return usr_pass52

def decryption_low(usr_pass53):
    for a, b in decryption_low_lst:
        usr_pass53 = usr_pass53.replace(a, b)
    return usr_pass53

def decryption_symbols(usr_pass54):
    for a, b in decryption_symbols_lst:
        usr_pass54 = usr_pass54.replace(a, b)
    return usr_pass54

def decryption_number_lst():
    number_lst = (('1!q', '1'), ('2@w', '2'), ('3#e', '3'), ('4$r', '4'), ('5%t', '5'), ('6^y', '6'),
                  ('7&u', '7'), ('*i', '8'), ('9(0', '9'), ('0)P', '0'), (';;', ' '))

    def decryption_of_numbers(usr_pass55):
        for a, b in number_lst:
            usr_pass55 = usr_pass55.replace(a, b)
        return usr_pass55

    def decryption_number():
        print('Enter your encrypted PWD-')
        usr_pass55 = input('')
        old_len55 = len(usr_pass55)
        old_type55 = type(usr_pass55)
        print(f'The OLD pwd length is:{old_len55}')
        print(f'The OLD pwd type is:{old_type55}')
        usr_pass55 = decryption_of_numbers(usr_pass55)
        print('-------------------------------------------------')
        new_len55 = len(usr_pass55)
        print(f'The NEW pwd length is:{new_len55}')

        print('The NEW secure password is {}'.format(usr_pass55))
        restart11 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
        if (restart11 == '1'):
            main()

        elif (restart11 == '0'):
            exit()

        else:
            print('Error')
            print('Lol!')
            print('         _       _')
            print('        | |     | |')
            print('        | | ___ | |')
            print('        | |/ _ \| |')
            print('        | | (_) | |')
            print('        |_|\___/|_|')
            exit()

    decryption_number()

def main():
    import time
    if __name__ == '__main__':
        print('\033[33m                                 ++++ Welcome To The\033[00m'+' \033[41m X-Crawler!!\033[00m'+ '\033[33m ++++\033[00m')
        time.sleep(0.1)
        print('  \033[33m                                 {{--Coded By:\033[00m'+' Kamaldeep Singh'+'\033[33m--}}\n\033[00m')

        from time import sleep

        print('         .------\ /------.')
        print('         |       -       |')
        print('         |               |')
        print('       _______________________')
        print('      ===========.===========')

        print('       ./ ~~~~~     ~~~~  \.')
        print('\033[31m       | ./| 0   |   0 |\. |   ---> I SEE YOU! <--\033[00m')
        
        sleep(0.5)
        print("\033[35m       |   --   / \  --    |      ----> Do you wanna use Network Scanner?[1/0]\033[00m")
        sleep(0.2)
        print('\033[35m       \.      |o o|      ./       ----> For Anonymous_Web_mailer {111}\033[00m')
        sleep(0.2)
        print('\033[35m        |                 |         ----> For YouTube Bot {222}\033[00m')
        sleep(0.2)
        print('\033[35m        \    #########    /          ----> For Facebook Auto_liker {333}\033[00m')
        print('         \  ## ----- ##  /                     ')
        print('          \##    __   ##/')
        sleep(0.9)
        ask2 = input('\033[31m           \___________/--> Pls Enter Here ==>\033[00m ')




        if (ask2 == '1'):
            print('--------------------------+ Welcome to the Network Scanner! +--------------------------')
            import scapy.all as scapy
            request = scapy.ARP()
            print('Note: By Default is 192.168.1.1/24')
            print('Do you wanna enter the Network Range Manually?[Y/N]')
            inp = input('==> ')
            if (inp == 'y' or inp == 'Y' or inp == '1'):
                res = input('Enter the Network Range:\n')
                request.pdst = res

                broadcast = scapy.Ether()
                broadcast.dst = 'ff:ff:ff:ff:ff:ff'

                broadcast_request = broadcast / request
                responses = scapy.srp(broadcast_request, timeout=1)[0]
                print('Network had been scanned Successfully!')
                sleep(0.5)
                print('Following are the Results:')
                sleep(1)
                for element in responses:
                    print(element[1].psrc + '     ' + element[1].hwsrc)
                    exit()
            elif (inp == 'n' or inp == 'N' or inp == '0'):
                request = scapy.ARP()  # creating arp packet
                request.pdst = '192.168.1.1/24'  # pdst is the target protocol address

                broadcast = scapy.Ether()  # creating MAC address packet
                broadcast.dst = 'ff:ff:ff:ff:ff:ff'  # dst is the target hardware address

                broadcast_request = broadcast / request  # combining
                responses = scapy.srp(broadcast_request, timeout=1)[0]  # srp is used to send & recieve packets
                print('Network had been scanned Successfully!')
                sleep(0.5)
                print('Following are the Results:')
                sleep(1)
                for element in responses:
                    print(element[1].psrc + ' ' + element[1].hwsrc)
                    exit()
            else:
                print('Lol!')
                print('         _       _')
                print('        | |     | |')
                print('        | | ___ | |')
                print('        | |/ _ \| |')
                print('        | | (_) | |')
                print('        |_|\___/|_|')
                exit()

        elif (ask2 == '333'):
            facebook()

        elif (ask2== '111'):
            anony_mailer()



        elif (ask2 == '222'):
            youtube()

        elif (ask2 == '0'):
            sleep(0.8)
            print('\033[32m {-} Exiting.....\033[00m')
            sleep(1)
        else:
            print('Lol!')
            print('         _       _')
            print('        | |     | |')
            print('        | | ___ | |')
            print('        | |/ _ \| |')
            print('        | | (_) | |')
            print('        |_|\___/|_|')
            exit()

        import requests
        # <Response [200]>
        import time
        import requests
        from time import sleep
        print('------------------------------------------\n')
        print('        /      \ ')
        print('\033[31m     \  \  ,,  /  /       ----> Do you wanna Run URL info Dumper?[1/0]\033[00m')
        print("      '-.`\()/`.-' ")
        print("     .--_'(  )'_-. ")
        print('    / /` /`""`\ `\ \.')
        print('     |  |  ><  |  |  ')
        print('     \  \      /  /  ')
        submission = input("\033[31m         '.__.'    --> Pls Enter Here ==>\033[00m ")


        if (submission == '1'):
            print('\033[33mWelcome to the URL Dumper!\033[00m')
            print('Note: By Default is "1"')
            define = input('\033[31mPress 1 for https and 0 for http URL:\n\033[00m')

            if (define == '1'):

                def url1():
                    try:
                        print('Note: https is selected!')
                        https = ('https://')
                        print('Enter the URL/Site to dump:')
                        res = input('')
                        full = (https + res)
                        response = requests.get(https + res)
                        sleep(0.5)
                        print('{+} Sending the request Packets to ' + res)
                        sleep(0.5)
                        print('\033[93m{+} Send1.....\033[00m')
                        sleep(0.3)
                        print('\033[93m{+} Send2.....\033[00m')
                        sleep(0.3)
                        print('\033[93m{+} Send3.....\033[00m')
                        print('-----------------------------------------')
                        sleep(1)
                        print('{-} Fetching the response! from ' + res)
                        sleep(0.5)
                        print('\033[35m{++} Done!!!\033[00m')
                        sleep(0.3)
                        print('\033[93m* Status of the URL is:\033[00m')
                        print(response.status_code)
                        print('\033[31m!Error: \033[00m')
                        print(response.raise_for_status)
                        sleep(0.5)
                        print('\033[31m* Time Elapsed: \033[00m')
                        print(response.elapsed)
                        sleep(0.5)
                        print("\033[93m* Header's info: \033[00m")
                        print(response.headers)
                        sleep(0.5)
                        print('\033[93m# Type of Encoding used: \033[00m' + response.encoding)
                        sleep(0.5)
                        print('\033[93m* Info in the form of Bytes: \033[00m')
                        print(response.content)
                        sleep(0.5)
                        print('\033[93m* History of the URL: \033[00m')
                        print(response.history)
                        sleep(0.5)
                        print('\033[31m* True & False Responses:-\033[00m')
                        sleep(1)
                        print('--------------------------------------')
                        sleep(0.8)
                        print('\033[93m* Site is Responsive?\033[00m')
                        sleep(0.3)
                        print(response.ok)
                        sleep(0.5)
                        print('\033[93m* Response is Permanent?\033[00m')
                        sleep(0.3)
                        print(response.is_permanent_redirect)
                        sleep(0.5)
                        print('\033[93m* Responses are Redirected?\033[00m')
                        sleep(0.3)
                        print(response.is_redirect)
                        sleep(0.5)
                        print('\033[93m* Does it contains a JavaScript(JS) Element?\033[00m')
                        sleep(0.3)
                        print(response.json)
                        sleep(1)
                        print('\033[31m----------------------++ Closing the Connection! ++----------------------\033[00m')
                        print('\033[34mFor Restart Press 777 OR To Quit Press 0: \033[00m')
                        ask = input('==> ')
                        if (ask == '777'):
                            url1()
                        elif (ask == '0'):
                            for hacker3 in range(1, 5):
                                print('\033[93m{-} Closing......\033[00m')
                                sleep(2)
                            print('\033[32m{-} Exiting....\033[00m')
                            exit()

                        else:
                            print("you didn't read earlier..")
                            print('Lol!')
                            print('         _       _')
                            print('        | |     | |')
                            print('        | | ___ | |')
                            print('        | |/ _ \| |')
                            print('        | | (_) | |')
                            print('        |_|\___/|_|')
                            exit()







                    except requests.ConnectionError:

                        print('Error in Requesting the URL: ' + full)
                        print('Reason: Error in requesting the site or invalid URL/Site')
                        print('To Try Again Enter "1":')
                        yes = input('==> ')
                        if (yes == '1'):
                            url1()
                        else:
                            exit()

                url1()

            elif (define == '0'):
                def url2():
                    try:
                        print('Note: http is selected!')
                        https = ('http://')
                        print('Enter the URL/Site to dump:')
                        res = input('')
                        full = (https + res)
                        response = requests.get(https + res)
                        sleep(0.5)
                        print('{+} Sending the request Packets to ' + res)
                        sleep(0.5)
                        print('{+} Send1.....')
                        sleep(0.3)
                        print('{+} Send2.....')
                        sleep(0.3)
                        print('{+} Send3.....')
                        print('-----------------------------------------')
                        sleep(1)
                        print('{-} Fetching the response! from ' + res)
                        sleep(0.5)
                        print('{++} Done!!!')
                        sleep(0.3)
                        print('* Status of the URL is:')
                        print(response.status_code)
                        print('# Error: ')
                        print(response.raise_for_status)
                        sleep(0.5)
                        print('* Time Elapsed: ')
                        print(response.elapsed)
                        sleep(0.5)
                        print("* Header's info: ")
                        print(response.headers)
                        sleep(0.5)
                        print('* Type of Encoding used: ' + response.encoding)
                        sleep(0.5)
                        print('* Info in the form of Bytes: ')
                        print(response.content)
                        sleep(0.5)
                        print('* History of the URL: ')
                        print(response.history)
                        sleep(0.5)
                        print('* True & False Responses:-')
                        sleep(1)
                        print('--------------------------------------')
                        sleep(0.8)
                        print('* Site is Responsive?')
                        sleep(0.3)
                        print(response.ok)
                        sleep(0.5)
                        print('* Response is Permanent?')
                        sleep(0.3)
                        print(response.is_permanent_redirect)
                        sleep(0.5)
                        print('* Responses are Redirected?')
                        sleep(0.3)
                        print(response.is_redirect)
                        sleep(0.5)
                        print('* Does it contains a JavaScript(JS) Element?')
                        sleep(0.3)
                        print(response.json)
                        sleep(1)
                        print('----------------------++ Closing the Connection! ++----------------------')
                        print('For Restart Press 777 OR To Quit Press 0: ')
                        ask = input('==> ')
                        if (ask == '777'):
                            url2()
                        elif (ask == '0'):
                            for hacker3 in range(1, 5):
                                print('{-} Closing......\033[00m')
                                sleep(2)
                            print('\033[32m{-} Exiting....\033[00m')
                            exit()

                        else:
                            print("you didn't read earlier..")
                            print('Lol!')
                            print('         _       _')
                            print('        | |     | |')
                            print('        | | ___ | |')
                            print('        | |/ _ \| |')
                            print('        | | (_) | |')
                            print('        |_|\___/|_|')
                            exit()
                    except requests.ConnectionError:

                        print('Error in Requesting the URL: ' + full)
                        print('Reason: Error in requesting the site or invalid URL/Site')
                        print('To Try Again Enter "1":')
                        yes = input('==> ')
                        if (yes == '1'):
                            url2()
                        else:
                            exit()

                url2()
            else:
                def url3():
                    try:
                        print('Note: By Default! https is now selected!')

                        https = ('https://')
                        print('Enter the URL/Site to dump:')
                        res = input('')
                        full = (https + res)
                        response = requests.get(https + res)
                        sleep(0.5)
                        print('{+} Sending the request Packets to ' + res)
                        sleep(0.5)
                        print('{+} Send1.....')
                        sleep(0.3)
                        print('{+} Send2.....')
                        sleep(0.3)
                        print('{+} Send3.....')
                        print('-----------------------------------------')
                        sleep(1)
                        print('{-} Fetching the response! from ' + res)
                        sleep(0.5)
                        print('{++} Done!!!')
                        sleep(0.3)
                        print('* Status of the URL is:')
                        print(response.status_code)
                        print('# Error: ')
                        print(response.raise_for_status)
                        sleep(0.5)
                        print('* Time Elapsed: ')
                        print(response.elapsed)
                        sleep(0.5)
                        print("* Header's info: ")
                        print(response.headers)
                        sleep(0.5)
                        print('* Type of Encoding used: ' + response.encoding)
                        sleep(0.5)
                        print('* Info in the form of Bytes: ')
                        print(response.content)
                        sleep(0.5)
                        print('* History of the URL: ')
                        print(response.history)
                        sleep(0.5)
                        print('* True & False Responses:-')
                        sleep(1)
                        print('--------------------------------------')
                        sleep(0.8)
                        print('* Site is Responsive?')
                        sleep(0.3)
                        print(response.ok)
                        sleep(0.5)
                        print('* Response is Permanent?')
                        sleep(0.3)
                        print(response.is_permanent_redirect)
                        sleep(0.5)
                        print('* Responses are Redirected?')
                        sleep(0.3)
                        print(response.is_redirect)
                        sleep(0.5)
                        print('* Does it contains a JavaScript(JS) Element?')
                        sleep(0.3)
                        print(response.json)
                        sleep(1)
                        print('----------------------++ Closing the Connection! ++----------------------')
                        print('For Restart Press 777 OR To Quit Press 0: ')
                        ask = input('==> ')
                        if (ask == '777'):
                            url3()
                        elif (ask == '0'):
                            for hacker3 in range(1, 5):
                                print('\033[32m{-} Closing......\033[00m')
                                sleep(2)
                            print('\033[32m{-} Exiting....\033[00m')
                            exit()

                        else:
                            print("you didn't read earlier..")
                            print('Lol!')
                            print('         _       _')
                            print('        | |     | |')
                            print('        | | ___ | |')
                            print('        | |/ _ \| |')
                            print('        | | (_) | |')
                            print('        |_|\___/|_|')
                            exit()

                    except requests.ConnectionError:

                        print('Error in Requesting the URL: ' + full)
                        print('Reason: Error in requesting the site or invalid URL/Site')
                        print('To Try Again Enter "1":')
                        yes = input('==> ')
                        if (yes == '1'):
                            url3()
                        else:
                            exit()

                url3()


        elif (submission == '0'):
            print('\033[32m{-} Leaving.........\033[00m')
            sleep(1)
            print('\033[31m{+} Entering to Self PWD Program!\033[00m')
            sleep(0.5)
            print('-----------------------------------')
            sleep(0.3)


        else:
            print("you didn't read earlier..")
            print('Lol!')
            print('         _       _')
            print('        | |     | |')
            print('        | | ___ | |')
            print('        | |/ _ \| |')
            print('        | | (_) | |')
            print('        |_|\___/|_|')
            exit()



        def main4():

            print('         .\.\.\.\.')
            print('          |^   ^|')
            print('          |O   O|')
            print('\033[31m          |  ~ * ---> Do you want to check your Internet Access?[1/0]\033[00m')
            print('           \ O /')
            input1 = input('\033[31m            | |--> Pls Enter Here ==>\033[00m ')



            if (input1 == '1'):
                try:
                    request = requests.get('https://www.google.com')
                    if request:
                        print('---------Active!---------')
                        time.sleep(0.3)
                        print('{+} Starting the Program........')
                        time.sleep(0.3)
                        print('{++} Started!')
                        time.sleep(0.3)
                        print('-----------------------------------------')
                        time.sleep(0.4)

                except requests.ConnectionError:
                    print('No Internet Access!')
                    time.sleep(0.5)
                    print('{+} Starting offline Program.......')
                    time.sleep(1)
            elif (input1 == '0'):
                time.sleep(0.2)
                print('{+} Starting Program Without IA Startup....')
                time.sleep(0.2)
                print('---------------------------------')
                time.sleep(0.7)

            else:
                print('Error')
                print('Lol!')
                print('         _       _')
                print('        | |     | |')
                print('        | | ___ | |')
                print('        | |/ _ \| |')
                print('        | | (_) | |')
                print('        |_|\___/|_|')
                exit()

            def main3():
                print("\033[35m           ____\033[00m")
                print("\033[35m         ,'    `.          --- Welcome to the self PWD Encrypter & Decrypter(root)\033[00m")
                print("\033[35m        /        \.          -- Use Anonymous Key to meet US\033[00m")
                print("\033[35m        \ ()  () /             - We Are Anonymous!\033[00m")
                print("\033[35m         `. /\ ,'                -We Are Legion\033[00m")
                print("\033[35m      8====| "" |====8\033[00m")
                print("\033[35m        ('`LLLU`')\033[00m")
                print('\033[31mDo you have Root Privileges Key?[1/0]\033[00m')

                ask = input('==> ')
                if (ask == '1'):
                    print('Enter the Root Key:')

                    password = input('==> ')

                    if (password == 'anonymous_root'):
                        name = input('Enter your name to interact with Chat Bot:\n')
                        from time import sleep
                        for hacker in range(1, 2):
                            print('Initializing..../')
                            sleep(2)
                            for hacker in range(1, 2):
                                print('{+} Checking for Root Privileges....// for ' + name)
                                sleep(2)
                                print('{+} Reading Databases....//')
                                sleep(1)
                                print('{+} Creating a session for ' + name + ' .....//')
                                sleep(1)
                                print('{-} Accessing.1')
                                sleep(1)
                                print('{+} Done!')
                                sleep(1)
                                print('{-} Accessing.2')
                                sleep(1)
                                print('{+} Done!')
                                sleep(1)
                                print('{-} Accessing.3')
                                sleep(4)
                                print('{+} Done!')
                                sleep(1)
                                print('\n')

                        print('Access Granted! ' + name)
                        print('Now ' + name + ' is root')
                        sleep(1)

                        print('         .-.')
                        print('\033[33m   Boo! (o o)  ---- Welcome ' + name + '!, i am your Bot\033[00m')
                        print('\033[33m       \| O \.   --- You are using a Root Access ' + name + '!!\033[00m')
                        print('         \   \.')
                        print("          `~~~'")
                        sleep(1)

                        do_agree = input('Do you agree?[1/0]')
                        sleep(1)
                        if (do_agree == '1'):
                            print('         .-.')
                            print('\033[33m        (o o)  _---- Welcome To The Decryption World ' + name + '!!!\033[00m')
                            print('\033[33m       \| O \./   --- Enter 777 PIN to start Decryptions!\033[00m')
                            print('\033[33m         \   \.     -- By 777 i will take ' + name + ' to Baby_decrypter\033[00m')
                            print("          `~~~'")
                            decry = input('PIN:\n')

                            if (decry == '777'):
                                print(' \033[95m                         ,=""=,   --- i can Help You !!!  \033[00m')
                                print(' \033[95m                        c , _,{    -- i am a Baby_decrypter!\033[00m')
                                print('                         /\  @ )                 __')
                                print("                        /  ^~~^\          <=.,__/ '}=")
                                print('                       (_/ ,, ,,)          \_ _>_/~')
                                print("                        ~\_(/-\)'-,_,_,_,-'(_)-(_)")
                                print('\n')
                                sleep(1)

                                print('Select the decryption option:')
                                sleep(1)
                                print('high = 1, Medium = 2, Low = 3, symbols = 4, PIN = 5')
                                option = input('')

                                if (option == '1'):
                                    for i in range(1, 2):
                                        print('Processing Decryption Database....')
                                        sleep(0.2)
                                        print('Reading the Databases....')
                                        sleep(0.2)
                                        print('Extracting Decrytion Lst....')
                                        sleep(0.2)
                                        print('-----------------------------------')
                                        sleep(1)

                                    print('Welcome to the High decryption!')
                                    usr_pass51 = input('Enter the encrypted PWD-\n')
                                    old_len5 = len(usr_pass51)

                                    print(f'The OLD encrypted pwd length is:{old_len5}')

                                    old_type5 = type(usr_pass51)

                                    print(f'The OLD encrypted pwd type is:{old_type5}')
                                    print('-------------------------------------------------')
                                    new_len5 = len(usr_pass51)
                                    print(f'The NEW decrypted pwd length is:{new_len5}')
                                    usr_pass51 = decryption_high(usr_pass51)
                                    print('The decrypted PWD is: {}'.format(usr_pass51))
                                    restart5 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                    if (restart5 == '1'):
                                        main()

                                    elif (restart5 == '0'):
                                        exit()

                                    else:
                                        print('Error')
                                        print('Lol!')
                                        print('         _       _')
                                        print('        | |     | |')
                                        print('        | | ___ | |')
                                        print('        | |/ _ \| |')
                                        print('        | | (_) | |')
                                        print('        |_|\___/|_|')
                                        exit()

                                elif (option == '5'):
                                    decryption_number_lst()

                                elif (option == '2'):
                                    print('Welcome to the Medium decryption!')
                                    usr_pass52 = input('Enter the encrypted PWD-\n')
                                    old_len6 = len(usr_pass52)

                                    print(f'The OLD encrypted pwd length is:{old_len6}')

                                    old_type6 = type(usr_pass52)

                                    print(f'The OLD encrypted pwd type is:{old_type6}')
                                    print('-------------------------------------------------')
                                    new_len6 = len(usr_pass52)
                                    print(f'The NEW decrypted pwd length is:{new_len6}')
                                    usr_pass52 = decryption_medium(usr_pass52)
                                    print('The decrypted PWD is: {}'.format(usr_pass52))
                                    restart6 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                    if (restart6 == '1'):
                                        main()

                                    elif (restart6 == '0'):
                                        exit()

                                    else:
                                        print('Error')
                                        print('Lol!')
                                        print('         _       _')
                                        print('        | |     | |')
                                        print('        | | ___ | |')
                                        print('        | |/ _ \| |')
                                        print('        | | (_) | |')
                                        print('        |_|\___/|_|')
                                        exit()

                                elif (option == '3'):
                                    print('Welcome to the Low decryption!')
                                    usr_pass53 = input('Enter the encrypted PWD-\n')
                                    old_len7 = len(usr_pass53)

                                    print(f'The OLD encrypted pwd length is:{old_len7}')

                                    old_type7 = type(usr_pass53)

                                    print(f'The OLD encrypted pwd type is:{old_type7}')
                                    print('-------------------------------------------------')
                                    new_len7 = len(usr_pass53)
                                    print(f'The NEW decrypted pwd length is:{new_len7}')
                                    usr_pass53 = decryption_low(usr_pass53)
                                    print('The decrypted PWD is: {}'.format(usr_pass53))
                                    restart7 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                    if (restart7 == '1'):
                                        main()

                                    elif (restart7 == '0'):
                                        exit()

                                    else:
                                        print('Error')
                                        print('Lol!')
                                        print('         _       _')
                                        print('        | |     | |')
                                        print('        | | ___ | |')
                                        print('        | |/ _ \| |')
                                        print('        | | (_) | |')
                                        print('        |_|\___/|_|')
                                        exit()

                                elif (option == '4'):
                                    print('Welcome to the symbols decryption!')
                                    usr_pass54 = input('Enter the encrypted PWD-\n')
                                    old_len8 = len(usr_pass54)

                                    print(f'The OLD encrypted pwd length is:{old_len8}')

                                    old_type8 = type(usr_pass54)

                                    print(f'The OLD encrypted pwd type is:{old_type8}')
                                    print('-------------------------------------------------')
                                    new_len8 = len(usr_pass54)
                                    print(f'The NEW decrypted pwd length is:{new_len8}')
                                    usr_pass54 = decryption_symbols(usr_pass54)
                                    print('The decrypted PWD is: {}'.format(usr_pass54))

                                    def restart8():
                                        restart8 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                        if (restart8 == '1'):
                                            main()

                                        elif (restart8 == '0'):
                                            exit()

                                        else:
                                            print('Error')
                                            print('Lol!')
                                            print('         _       _')
                                            print('        | |     | |')
                                            print('        | | ___ | |')
                                            print('        | |/ _ \| |')
                                            print('        | | (_) | |')
                                            print('        |_|\___/|_|')
                                            exit()

                                    restart8()



                                else:
                                    print('Error')
                                    print('Lol!')
                                    print('         _       _')
                                    print('        | |     | |')
                                    print('        | | ___ | |')
                                    print('        | |/ _ \| |')
                                    print('        | | (_) | |')
                                    print('        |_|\___/|_|')
                                    exit()





                            else:
                                print('         .-.')
                                print('\033[33m  Trash (o o)  _---- It seems You Entered Invalid syntax!\33[00m' + name)
                                print('\033[33m       \| O \./  --- ??\033[00m')
                                print('         \   \.')
                                restart10 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                if (restart10 == '1'):
                                    main()

                                elif (restart10 == '0'):
                                    exit()

                                else:
                                    print('Error')
                                    print('Lol!')
                                    print('         _       _')
                                    print('        | |     | |')
                                    print('        | | ___ | |')
                                    print('        | |/ _ \| |')
                                    print('        | | (_) | |')
                                    print('        |_|\___/|_|')
                                    exit()




                elif (ask == '0' or ask == ''):
                    print('\033[31mDo You have a Key for Anonymous Route?[1/0]\033[00m')

                    key = input('==> ')
                    if (key == '1'):
                        enter_anony = input('Enter the KEY-\n')
                        if (enter_anony == 'anonymous_encrypt'):

                            print('\033[31m                           | || |    ,/  _____  \.  --- i am anonymous\033[00m')
                            print('\033[31m                           \_||_/    ||_/     \_||   -- Welcome!\033[00m')
                            print('                             ||       \_| . . |_/')
                            print('                             ||         |  L  |')
                            print("                            ,||         |`==='|")
                            print("                            |>|      ___`>  -<'___")
                            print("                            |>|\    /             \.")
                            print("                            \>| \  /  ,    .    .  |")
                            print("\033[33m                             ||  \/  /| .  |  . |  |\033[00m")
                            print("                             ||\  ` / | ___|___ |  |")
                            print('\n')
                            print('You are using a Hidden Anonymous route!!!')
                            print("Restrictions- Capital letters & numbers ain't allowed!")

                            print('\033[31mAre you on Anonymous Route???[Y/N]\033[00m')
                            give = input('')
                            if (give == 'y' or give == 'Y'):
                                print('Encrypting Power is set to MAX!')

                                from time import sleep
                                def hacker_encrypted_lst():
                                    hacker_lst = (
                                        ('q', '😂'), ('w', '😄'), ('e', '😃'), ('r', '😀'), ('t', '😊'), ('y', '😉'),
                                        ('u', '😍'), ('i', '😘'), ('o', '😚'), ('p', '😗'), ('a', '😜'), ('s', '😈'),
                                        ('d', '😇'), ('f', '🤦'), ('g', '💞'), ('h', '🕵️‍♀️'), ('j', '💀'),
                                        ('k', "👀"),

                                        ('l', '🥶'), ('z', '🙈'), ('x', '😹'), ('c', '🏃‍♀️'), ('v', '💋'),
                                        ('b', '👷'),
                                        ('n', '🤕'), ('m', '🤣'), (' ', '🧜‍♂️'))

                                    def hacker_encryption(anony):
                                        for a, b in hacker_lst:
                                            anony = anony.replace(a, b)
                                        return anony

                                    def hacker_en():
                                        print('Enter a PWD to encrypt it to MAX!-')
                                        anony = input('')
                                        old_len0 = len(anony)

                                        print(f'The OLD pwd length is:{old_len0}')

                                        anony = hacker_encryption(anony)
                                        print(
                                            '------------------Processing.............-----///----------///----------------')
                                        new_len0 = len(anony)
                                        print(f'The NEW pwd length is:{new_len0}')

                                        print("          ,    ,    /\   /\.   ")
                                        print(
                                            "\033[31m         /( /\ )\  _\ \_/ /_   ---Wait i am processing your PWD@!..... \033[00m         ")
                                        print(
                                            "         |\_||_/| < \_   _/ >                                     ......")
                                        print(
                                            "\033[31m         \______/  \|0   0|/    -- My eyes are Closed!              .......\033[00m")
                                        print("           _\/_   _(_  ^  _)_")
                                        print('          ( () ) /`\|V"""V|/`\.        ')
                                        print("            {}   \  \_____/  /")
                                        print("            ()   /\   )=(   /\.           ")
                                        print("            {}  /  \_/\=/\_/  \.                 ")
                                        print('\n')
                                        print('{+} Processing.....Pls_wait!')
                                        for i in range(1, 2):
                                            print('{+} Processing.....1')
                                            sleep(3)
                                            for i in range(1, 2):
                                                print('{+} Initializing Database./')
                                                sleep(3)
                                                for i in range(1, 2):
                                                    print('{+} Processing.....2')
                                                    sleep(3)
                                                    for i in range(1, 2):
                                                        print('{+} Processing.....3')
                                                        sleep(3)
                                                        for i in range(1, 2):
                                                            print('{+} Processing.....4')
                                                            sleep(3)
                                                            for i in range(1, 2):
                                                                print('{+} Processing.....5')
                                                                print('{++} Done!!')
                                                                sleep(3)

                                        print('\n')
                                        print('\033[32m           ----+  PROCESSED SUCCESSFULLY  +----\033[00m')
                                        sleep(1)
                                        print('\n')

                                        print("          ,    ,    /\   /\.   ")
                                        print("         /( /\ )\  _\ \_/ /_")
                                        print("         |\_||_/| < \_   _/ >")
                                        print("\033[31m         \______/  \|o   o|/           -- My eyes are Open Now!\033[00m")
                                        print("           _\/_   _(_  ^  _)_")
                                        print(
                                            '\033[31m          ( () ) /`\|V"""V|/`\.        ----The NEW secure password is {}\033[00m'.format(
                                                anony))
                                        print("            {}   \  \_____/  /")
                                        print("\033[31m            ()   /\   )=(   /\.            --TO decrypt enter 'Key'\033[00m")
                                        print("\033[31m            {}  /  \_/\=/\_/  \.                 --for Key type HELP\033[00m")

                                        restart0 = input("Press 1 to RESTART or Press 0 to EXIT or Enter a 'Key'\n")
                                        if (restart0 == '1'):
                                            main()

                                        elif (restart0 == 'anonymous_decryption'):

                                            def hacker_decrypted_lst():
                                                hacker_decrypted_lst = (
                                                    ('😂', 'q'), ('😄', 'w'), ('😃', 'e'), ('😀', 'r'), ('😊', 't'),
                                                    ('😉', 'y'),
                                                    ('😍', 'u'), ('😘', 'i'), ('😚', 'o'), ('😗', 'p'), ('😜', 'a'),
                                                    ('😈', 's'),
                                                    ('😇', 'd'), ('🤦', 'f'), ('💞', 'g'), ('🕵️‍♀️', 'h'), ('💀', 'j'),
                                                    ('👀', "k"),
                                                    ('🥶', 'l'), ('🙈', 'z'), ('😹', 'x'), ('🏃‍♀️', 'c'), ('💋', 'v'),
                                                    ('👷', 'b'),
                                                    ('🤕', 'n'), ('🤣', 'm'), ('🧜‍♂️', ' '))

                                                def hacker_decryption(anony1):
                                                    for a, b in hacker_decrypted_lst:
                                                        anony1 = anony1.replace(a, b)
                                                    return anony1

                                                def hacker_de():
                                                    print('Enter a PWD for decryption!-')
                                                    anony1 = input('')
                                                    old_len9 = len(anony1)

                                                    print(f'The OLD pwd length is:{old_len9}')

                                                    anony1 = hacker_decryption(anony1)
                                                    print(
                                                        '------------------Processing.............-----///')
                                                    new_len9 = len(anony1)
                                                    sleep(0.4)
                                                    print(
                                                        '------------------Processing.............-----///----------///')
                                                    sleep(0.4)
                                                    print(
                                                        '------------------Processing.............-----///----------///----------------')

                                                    sleep(1)
                                                    print(f'The NEW pwd length is:{new_len9}')
                                                    print("          ,    ,    /\   /\.   ")
                                                    print("         /( /\ )\  _\ \_/ /_")
                                                    print("         |\_||_/| < \_   _/ >")
                                                    print("         \______/  \|0   o|/")
                                                    print("           _\/_   _(_  ^  _)_")
                                                    print(
                                                        '\033[31m          ( () ) /`\|V"""V|/`\.        ----The decrypted password is {}\033[00m'.format(
                                                            anony1))
                                                    print("            {}   \  \_____/  /")
                                                    print("            ()   /\   )=(   /\.          ")
                                                    print("            {}  /  \_/\=/\_/  \.                 ")

                                                    restart0 = input("Press 1 to RESTART or Press 0 to EXIT-\n")
                                                    if (restart0 == '1'):
                                                        main()
                                                    elif (restart0 == '0'):
                                                        exit()
                                                    else:
                                                        print('  ,  ,  , , ,')
                                                        print(' <(__)> | | |')
                                                        print(' | \/ | \_|_/')
                                                        print(' \^  ^/   |')
                                                        print(' /\--/\  /|')
                                                        print('/  \/  \/ |')
                                                        for i in range(1, 4):
                                                            print('\033[35mYou are Trash!\033[00m')

                                                hacker_de()

                                            hacker_decrypted_lst()





                                        elif (restart0 == '0'):
                                            exit()

                                        elif (restart0 == 'HELP'):
                                            press = input('This means that you wanna decrypt?[Y/N]\n')
                                            if (press == 'y' or press == 'Y'):
                                                print('Key: anonymous_decryption')
                                                main()
                                            else:

                                                for i in range(1, 4):
                                                    print('\033[35mYou are Trash!\033[00m')
                                                    sleep(0.2)
                                                    print('  ,  ,  , , ,')
                                                    print(' <(__)> | | |')
                                                    print(' | \/ | \_|_/')
                                                    print(' \^  ^/   |')
                                                    print(' /\--/\  /|')
                                                    print('/  \/  \/ |')



                                        else:
                                            print('          |_|   ,')
                                            print("         ('.') ///")
                                            print('         <(_)`-/')
                                            print('          <-._/')
                                            for i in range(1, 4):
                                                print('\033[35mYou are looser!!\033[00m')

                                    hacker_en()

                                hacker_encrypted_lst()









                            elif (give == 'n' or give == 'N'):
                                print('Error')
                                print('Lol!')
                                print('         _       _')
                                print('        | |     | |')
                                print('        | | ___ | |')
                                print('        | |/ _ \| |')
                                print('        | | (_) | |')
                                print('        |_|\___/|_|')
                                exit()

                            else:

                                for i in range(1, 10000):
                                    print('You are looser!!')

                        else:

                            print('  ,  ,  , , ,')
                            print(' <(__)> | | |')
                            print(' | \/ | \_|_/')
                            print(' \^  ^/   |')
                            print(' /\--/\  /|')
                            print('/  \/  \/ |')
                            print('\n')
                            print('\033[32mFalse Key Entered!!!\033[00m')

                    elif (key == '0' or key == ''):
                        print('\033[31mDo you want to start the pwd securing process?[Y/N]\033[00m')
                        agree = input('==> ')
                        if (agree == 'Y' or agree == 'y' or agree == '1'):
                            print('Select the Type of PWD -')
                            print('txt = 0, Symbol = 1, PIN = 10')
                            select = input('==> ')
                            if (select == '0' or select == 'TXT' or select == 'txt'):
                                print('Note- Capital letters are only acceptable in "High"!!!')
                                print('Options for Security Level encryption:')
                                print('High (COMPLEX) = 1, Medium (MEMORABLE) = 2, Low (OK-OK) = 3')
                                security_level = input('Enter the pwd security LEVEL-\n')
                                if (security_level == '1'):
                                    import time
                                    # request 1
                                    for hacker12 in range(1, 2):
                                        print('{+} Processing your request...1 for High')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...2 for High')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...3 for High')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...4 for High')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...5 for High')
                                        time.sleep(2)

                                        print('Starting the PWD Encryting System....')

                                        time.sleep(1)
                                        print('-------------------+ High_Encryptions +----------------------')
                                        print('Started!!')
                                    print('Security is set to High')

                                    print("                        .-._")
                                    print("                       / o\ \               \.")
                                    print("\033[31m      i am here! ---- .'   J  \               |\033[00m")
                                    print("\033[31m  High Security!! ----V_._.|  /              /\033[00m")
                                    print("                         | L_/            .-'")
                                    print("                         |    ` --.____.-'(")
                                    print("                        /                 \.")
                                    print("                        |                  |")
                                    print("                         \-. .__.---'""`.  L_")
                                    print("                         ||/            >-. J")
                                    print("                        '-||           '-' ||")
                                    print("                                        '-'')")

                                    print('Enter your password to encrypt-')
                                    usr_pass = input('')
                                    old_len1 = len(usr_pass)
                                    old_type1 = type(usr_pass)
                                    print(f'The OLD pwd length is:{old_len1}')
                                    print(f'The OLD pwd type is:{old_type1}')
                                    print('-------------------------------------------------')
                                    usr_pass = encryption_of_passwords(usr_pass)
                                    new_len1 = len(usr_pass)
                                    print(f'The NEW pwd length is:{new_len1}')

                                    secure = print('The NEW secure password is {}'.format(usr_pass))

                                    def pass1():

                                        destination = input('Do you want to save the encrypted PWD in a file?[1/0]\n')
                                        if (destination == '1'):
                                            print('Note: File will be saved as encrypted.txt')
                                            try:
                                                filename = 'encrypted.txt'
                                                opening = open(filename, 'w')
                                                opening.write(usr_pass)
                                                opening.close()

                                            except IOError:
                                                print('There is No File such as ' + filename)

                                            for hack in range(1, 2):
                                                print('Saving.....')
                                                import time
                                                import os
                                                time.sleep(1)
                                                print('-----------------------------')
                                                print('Done!!')

                                                get = os.getcwd()
                                                print('Saved Path ==> ' + get)



                                        elif (destination == '0'):
                                            main()

                                        else:
                                            restart()

                                    pass1()

                                    def restart():
                                        restart = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                        if (restart == '1'):
                                            main()

                                        elif (restart == '0'):
                                            exit()

                                        else:
                                            print('Error')
                                            print('Lol!')
                                            print('         _       _')
                                            print('        | |     | |')
                                            print('        | | ___ | |')
                                            print('        | |/ _ \| |')
                                            print('        | | (_) | |')
                                            print('        |_|\___/|_|')
                                            exit()

                                    restart()

                                elif (security_level == '2'):
                                    import time

                                    # request 2
                                    for hacker12 in range(1, 2):
                                        print('{+} Processing your request...1 for Medium')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...2 for Medium')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...3 for Medium')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...4 for Medium')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...5 for Medium')
                                        time.sleep(2)

                                        print('Starting the PWD Encryting System....')

                                        time.sleep(1)
                                        print('-------------------+ Medium_Encryptions +----------------------')
                                        print('Started!!')

                                    print('Security is set to Medium')

                                    print("                        .-._")
                                    print("                       / o\ \               \.")
                                    print("\033[31m      i am here! ---- .'   J  \               |\033[00m")
                                    print("\033[31m Medium Security!! ---V_._.|  /              /\033[00m")
                                    print("                         | L_/            .-'")
                                    print("                         |    ` --.____.-'(")
                                    print("                        /                 \.")
                                    print("                        |                  |")
                                    print("                         \-. .__.---'""`.  L_")
                                    print("                         ||/            >-. J")
                                    print("                        '-||           '-' ||")
                                    print("                                        '-'')")

                                    print('Note- Capital letters are not acceptable in Medium!')
                                    agree1 = input('Do you agree?[Y/N]\n')
                                    if (agree1 == 'y' or agree1 == 'Y'):
                                        print('Enter your password to encrypt-')
                                        usr_pass2 = input('')
                                        old_len2 = len(usr_pass2)
                                        old_type2 = type(usr_pass2)
                                        print(f'The OLD pwd length is:{old_len2}')
                                        print(f'The OLD pwd type is:{old_type2}')

                                        usr_pass2 = encryption_of_passwords2(usr_pass2)
                                        print('-------------------------------------------------')
                                        new_len2 = len(usr_pass2)
                                        print(f'The NEW pwd length is:{new_len2}')
                                        print('The NEW secure password is {}'.format(usr_pass2))

                                        def pass2():
                                            print('Note: File will be saved as encrypted_medium.txt')
                                            destination = input(
                                                'Do you want to save the encrypted PWD in a file?[1/0]\n')
                                            if (destination == '1'):

                                                try:
                                                    filename_medium = 'encrypted_medium.txt'
                                                    opening = open(filename_medium, 'w')
                                                    opening.write(usr_pass2)
                                                    opening.close()
                                                except IOError:
                                                    print('There is No File such as ' + filename_medium)

                                                for hack in range(1, 2):
                                                    print('Saving.....')
                                                    import time
                                                    import os
                                                    time.sleep(1)
                                                    print('-----------------------------')
                                                    print('Done!!')
                                                    get = os.getcwd()
                                                    print('Saved Path ==> ' + get)


                                            elif (destination == '0'):
                                                main()

                                            else:
                                                restart2()

                                        pass2()

                                        def restart2():
                                            restart2 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                            if (restart2 == '1'):
                                                main()

                                            elif (restart2 == '0'):
                                                exit()

                                            else:
                                                print('Error')
                                                print('Lol!')
                                                print('         _       _')
                                                print('        | |     | |')
                                                print('        | | ___ | |')
                                                print('        | |/ _ \| |')
                                                print('        | | (_) | |')
                                                print('        |_|\___/|_|')
                                                exit()

                                        restart2()

                                    elif (agree1 == 'n' or agree1 == 'N'):
                                        print("you didn't read earlier..")
                                        print('Lol!')
                                        print('         _       _')
                                        print('        | |     | |')
                                        print('        | | ___ | |')
                                        print('        | |/ _ \| |')
                                        print('        | | (_) | |')
                                        print('        |_|\___/|_|')
                                        exit()



                                elif (security_level == '3'):
                                    import time

                                    # request 3
                                    for hacker12 in range(1, 2):
                                        print('{+} Processing your request...1 for Low')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...2 for Low')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...3 for Low')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...4 for Low')
                                        time.sleep(0.3)
                                        print('{+} Processing your request...5 for Low')
                                        time.sleep(2)

                                        print('Starting the PWD Encryting System....')

                                        time.sleep(1)
                                        print('-------------------+ Low_Encryptions +----------------------')
                                        print('Started!!')
                                    print('Security is set to Low')
                                    print("                        .-._")
                                    print("                       / o\ \               \.")
                                    print("\033[31m      i am here! ---- .'   J  \               |\033[00m")
                                    print("\033[31m  Low Security!! ---- V_._.|  /              /\033[00m")
                                    print("                         | L_/            .-'")
                                    print("                         |    ` --.____.-'(")
                                    print("                        /                 \.")
                                    print("                        |                  |")
                                    print("                         \-. .__.---'""`.  L_")
                                    print("                         ||/            >-. J")
                                    print("                        '-||           '-' ||")
                                    print("                                        '-'')")
                                    print('Note- Capital letters are not acceptable in Low!')

                                    agree1 = input('Do you agree?[Y/N]\n')
                                    if (agree1 == 'y' or agree1 == 'Y'):
                                        print('Enter your password to encrypt-')
                                        usr_pass3 = input('')
                                        old_len3 = len(usr_pass3)
                                        old_type3 = type(usr_pass3)
                                        print(f'The OLD pwd length is:{old_len3}')
                                        print(f'The OLD pwd type is:{old_type3}')
                                        usr_pass3 = encryption_of_passwords3(usr_pass3)
                                        print('-------------------------------------------------')
                                        new_len3 = len(usr_pass3)
                                        print(f'The NEW pwd length is:{new_len3}')

                                        print('The NEW secure password is {}'.format(usr_pass3))

                                        def pass3():
                                            print('Note: File will be saved as encrypted_low.txt')
                                            destination = input(
                                                'Do you want to save the encrypted PWD in a file?[1/0]\n')
                                            if (destination == '1'):
                                                try:
                                                    filename_low = 'encrypted_low.txt'
                                                    opening = open(filename_low, 'w')
                                                    opening.write(usr_pass3)
                                                    opening.close()
                                                except IOError:
                                                    print('There is No File such as ' + filename_low)

                                                for hack in range(1, 2):
                                                    print('Saving.....')
                                                    import time
                                                    import os
                                                    time.sleep(1)
                                                    print('-----------------------------')
                                                    print('Done!!')
                                                    get = os.getcwd()
                                                    print('Saved Path ==> ' + get)


                                            elif (destination == '0'):
                                                main()

                                            else:
                                                restart3()

                                        pass3()

                                        def restart3():
                                            restart3 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                            if (restart3 == '1'):
                                                main()

                                            elif (restart3 == '0'):
                                                exit()

                                            else:
                                                print('Error')
                                                print('Lol!')
                                                print('         _       _')
                                                print('        | |     | |')
                                                print('        | | ___ | |')
                                                print('        | |/ _ \| |')
                                                print('        | | (_) | |')
                                                print('        |_|\___/|_|')
                                                exit()

                                        restart3()

                                    elif (agree1 == 'n' or agree1 == 'N'):
                                        print("you didn't read earlier..")
                                        print('Lol!')
                                        print('         _       _')
                                        print('        | |     | |')
                                        print('        | | ___ | |')
                                        print('        | |/ _ \| |')
                                        print('        | | (_) | |')
                                        print('        |_|\___/|_|')
                                        exit()


                                else:
                                    print('Error!')
                                    print('\033[33mNo security_level detected!\033[00m')

                            elif (select == '10' or select == 'PIN' or select == 'pin'):
                                number_lst()

                            elif (select == '1' or select == 'symbol' or select == 'SYMBOL'):

                                import time

                                # request 3
                                for hacker12 in range(1, 2):
                                    print('{+} Processing your request...1 for Symbol')
                                    time.sleep(0.3)
                                    print('{+} Processing your request...2 for Symbol')
                                    time.sleep(0.3)
                                    print('{+} Processing your request...3 for Symbol')
                                    time.sleep(0.3)
                                    print('{+} Processing your request...4 for Symbol')
                                    time.sleep(0.3)
                                    print('{+} Processing your request...5 for Symbol')
                                    time.sleep(2)

                                    print('Starting the PWD Encryting System....')

                                    time.sleep(1)
                                    print('-------------------+ Symbol_Encryptions +----------------------')
                                    print('Started!!')
                                    time.sleep(0.1)
                                print('Enter your Symbol to encrypt-')
                                usr_pass4 = input('')
                                old_len4 = len(usr_pass4)

                                print(f'The OLD pwd length is:{old_len4}')

                                old_type4 = type(usr_pass4)

                                print(f'The OLD pwd type is:{old_type4}')
                                print('-------------------------------------------------')
                                new_len4 = len(usr_pass4)
                                print(f'The NEW pwd length is:{new_len4}')
                                usr_pass4 = encryption_of_symbol(usr_pass4)

                                print('The NEW secure password is {}'.format(usr_pass4))

                                def pass50():
                                    print('Note: File will be saved as encrypted_symbols.txt')
                                    destination = input('Do you want to save the encrypted PWD in a file?[1/0]\n')
                                    if (destination == '1'):
                                        try:
                                            filename_symbols = 'encrypted_symbols.txt'
                                            opening = open(filename_symbols, 'w')
                                            opening.write(usr_pass4)
                                            opening.close()
                                        except IOError:
                                            print('There is No File such as ' + filename_symbols)

                                        for hack in range(1, 2):
                                            print('Saving.....')
                                            import time
                                            import os
                                            time.sleep(1)
                                            print('-----------------------------')
                                            print('Done!!')
                                            get = os.getcwd()
                                            print('Saved Path ==> ' + get)


                                    elif (destination == '0'):
                                        main()

                                    else:
                                        restart4()

                                pass50()

                                def restart4():
                                    restart4 = input('Press 1 to RESTART or Press 0 to EXIT-\n')
                                    if (restart4 == '1'):
                                        main()

                                    elif (restart4 == '0'):
                                        exit()

                                    else:
                                        print('Error')
                                        print('Lol!')
                                        print('         _       _')
                                        print('        | |     | |')
                                        print('        | | ___ | |')
                                        print('        | |/ _ \| |')
                                        print('        | | (_) | |')
                                        print('        |_|\___/|_|')
                                        exit()

                                restart4()











                        elif (agree == 'N' or agree == 'n'):
                            pwd = 1
                            while (pwd <= 5):
                                print('\033[34mAborting the process......//\033[00m')
                                pwd = pwd + 1







                        else:
                            print('Error')
                            print('Lol!')
                            print('         _       _')
                            print('        | |     | |')
                            print('        | | ___ | |')
                            print('        | |/ _ \| |')
                            print('        | | (_) | |')
                            print('        |_|\___/|_|')
                            exit()

                    else:
                        print('Error')
                        print('Lol!')
                        print('         _       _')
                        print('        | |     | |')
                        print('        | | ___ | |')
                        print('        | |/ _ \| |')
                        print('        | | (_) | |')
                        print('        |_|\___/|_|')
                        exit()



                else:
                    print('Error')
                    print('Lol!')
                    print('         _       _')
                    print('        | |     | |')
                    print('        | | ___ | |')
                    print('        | |/ _ \| |')
                    print('        | | (_) | |')
                    print('        |_|\___/|_|')
                    exit()


            main3()
        main4()



def lol():
    print('Error')
    print('Lol!')
    print('         _       _')
    print('        | |     | |')
    print('        | | ___ | |')
    print('        | |/ _ \| |')
    print('        | | (_) | |')
    print('        |_|\___/|_|')
    exit()




# Facebook Auto liker
# +12522282703

# C:/Program Files (x86)/Google/Chrome/chromedriver.exe

def facebook():
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    import time
    import requests
    print('-----------------------------------------------------------------------')
    print('\033[43m Note: This script needs Active Internet Access!\033[00m')
    print('\033[31m Do you have Internet Access?[1/0]\033[00m')
    internet = input('==> ')
    if (internet == '1'):

        try:
            request = requests.get('https://www.google.com')
            if request:
                print('\033[33m---------Active!---------\033[00m')
                time.sleep(0.3)
                print('{+} Starting the Script........')
                time.sleep(0.3)
                print('{++} Started!')
                time.sleep(0.3)
                print('-----------------------------------------')
                time.sleep(0.4)

        except requests.ConnectionError:
            print('No Internet Access!')
            time.sleep(0.5)
            facebook()


    elif (internet == '0'):
        facebook()
    else:
        lol()

    print(
        '\033[41m--------------------------------+ Welcome TO The Facebook Auto_Liker+Lover Bot! +--------------------------------\033[00m')
    print('\033[31m                :Disclaimer:\033[00m')
    print('                    /"\.')
    print('\033[95m                   |\./|      *----Only Chrome Browser is Compatible!\033[00m')

    print("\033[35m                   |   |                 --> Don't use excess of Automation!\033[00m")
    print('\033[35m                   |>*<|                 --> Use correct Credentials to login!\033[00m')
    print('\033[35m                   |   |                 --> Use correct FB_id!\033[00m')
    print("\033[35m                /'\|   |/'\.             --> Give an interval of 15 min after one USE!\033[00m")
    print("\033[35m            /'\|   |   |   |             {*} Fill the Captcha asked in between!\033[00m")
    print('           |   |   |   |   | \.')
    print('           |   |   |   |   | \.')
    print('           | *   *   *   * |>  >')
    print('           |                  /')
    print('           |               /')
    print('           |            /')
    print('            \          |')
    question = input('\033[31m             |         |  ---> Do you agree?[1/0]==> \033[00m')



    if (question == '1'):
        print('Enter your Credentials Carefully:')
        number_usr = str(input('Enter the Usr_name or Number:\n==> '))
        pwd = input('Enter the PWD:\n==> ')
        id = str(input('Enter the Facebook_Post id:\n'))
        option = input('For like = 1, Love = 2\n==> ')
        print('{+} Starting the Automation..........')
        sleep(0.5)
        print('{++} Started!')

        # Like
        if (option == '1'):
            class liker():
                def __init__(self, username, password, id):
                    protocol = 'https://'
                    stable2 = (protocol+'tin')

                    like_ask = input('Enter the path of Webdriver:\n')
                    stable = (stable2 + 'yurl.com')
                    from selenium.webdriver.chrome.options import Options
                    chrome_options = Options()
                    chrome_options.add_argument("--window-size=1024,768")



                    self.driver = webdriver.Chrome(
                        executable_path=like_ask, options = chrome_options)


                    url = (stable+'/y8c5wla8')
                    self.driver.get(url)

                    sleep(1)
                    self.click = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/h4/a[1]')
                    sleep(0.5)
                    self.click.click()
                    self.usr = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/input[1]')
                    self.usr.send_keys(username)
                    sleep(0.5)
                    self.pwd = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/input[2]')
                    self.pwd.send_keys(password)
                    sleep(1)
                    self.generate_token = self.driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div/div/div/div/button')
                    self.generate_token.click()
                    sleep(3)
                    self.txt = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p/div/iframe')
                    sleep(3)
                    self.txt.click()
                    sleep(1)
                    self.txt.send_keys(Keys.CONTROL + 'a')
                    sleep(1)
                    self.txt.send_keys(Keys.CONTROL + 'c')
                    sleep(3)
                    self.back = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p/div/a')
                    self.back.click()
                    sleep(2)
                    self.login = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/input[1]')
                    self.login.send_keys(Keys.CONTROL + 'v')
                    sleep(2)
                    self.login_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/input[3]')
                    self.login_button.click()
                    sleep(3)
                    self.post = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/center/a[1]')
                    sleep(1)
                    self.post.click()
                    sleep(5)


                    self.login_entry = self.driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div/div/div/div/form/input[1]')
                    sleep(0.5)
                    self.login_entry.send_keys(id)
                    sleep(0.5)
                    self.driver.maximize_window()
                    sleep(30)



                    self.submit = self.driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div/div/div/div/form/input[3]')
                    sleep(0.5)
                    self.submit.click()
                    sleep(20)


            liker(number_usr, pwd, id)

        # love

        elif (option == '2'):

            class love():
                def __init__(self, username, password, id):
                    love_ask = input('Enter the path of Webdriver:\n')
                    from selenium.webdriver.chrome.options import Options
                    chrome_options = Options()
                    chrome_options.add_argument("--window-size=1024,768")
                    self.driver = webdriver.Chrome(
                        executable_path=love_ask, options = chrome_options)

                    url = 'https://yolikers.com/'
                    self.driver.get(url)

                    sleep(1)
                    self.click = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/h4/a[1]')
                    sleep(0.5)
                    self.click.click()
                    self.usr = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/input[1]')
                    self.usr.send_keys(username)
                    sleep(0.5)
                    self.pwd = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/input[2]')
                    self.pwd.send_keys(password)
                    sleep(1)
                    self.generate_token = self.driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div/div/div/div/button')
                    self.generate_token.click()
                    sleep(3)
                    self.txt = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p/div/iframe')
                    sleep(3)
                    self.txt.click()
                    sleep(1)
                    self.txt.send_keys(Keys.CONTROL + 'a')
                    sleep(1)
                    self.txt.send_keys(Keys.CONTROL + 'c')
                    sleep(3)
                    self.back = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/p/div/a')
                    self.back.click()
                    sleep(2)
                    self.login = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/input[1]')
                    self.login.send_keys(Keys.CONTROL + 'v')
                    sleep(2)
                    self.login_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/input[3]')
                    self.login_button.click()
                    sleep(3)
                    self.post = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/center/a[1]')
                    sleep(1)
                    self.post.click()
                    sleep(5)
                    self.driver.maximize_window()
                    sleep(30)
                    self.login_entry = self.driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div/div/div/div/form/input[1]')
                    sleep(0.5)
                    self.login_entry.send_keys(id)
                    sleep(0.5)
                    self.love = self.driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div/div/div/div/form/label[2]/input')
                    self.love.click()
                    sleep(0.5)
                    self.driver.maximize_window()
                    sleep(30)


                    self.submit = self.driver.find_element_by_xpath(
                        '/html/body/div[6]/div/div/div/div/div/form/input[3]')
                    sleep(0.5)
                    self.submit.click()
                    sleep(20)


            love(number_usr, pwd, id)
        else:
            lol()
    elif (question == '0'):
        print('Kindly Agree The terms and Conditions\n'
              'Before proceeding!!')
        ask09 = input('OK?[1/0]')
        if (ask09 == '1'):
            facebook()
        else:
            lol()

    else:
        lol()












# Auto_Viewer_Bot -

def youtube():

    from time import sleep

    print('\033[41m--------------------------------+ Welcome TO The YouTube Auto_viewer Bot! +--------------------------------\033[00m')


    print('           ,,,,,,,,,,,')
    print('          //////// \\\\.')
    print('        // ==     == \\.')
    sleep(0.5)
    print('\033[31m          (  o    0  )\\.     ---->\033[00m' +' Enter'+'\033[04m 1 for Chrome\033[00m' +' and'+'\033[04m 2 for Firefox!\033[00m')
    sleep(0.5)
    print('           (    L    )\.')
    print('            (  ___  )\\.')
    print('             \_____/\\.')
    print('               |   |\\.')
    print('        ------/  ^  \----')
    print('       /     ~~~o~~~~    \.')
    print('      I         o         I')
    print('     I    I     o     I    I')
    print('     I   II     o     II   I')
    sleep(0.5)
    choose = input('\033[31m      I__II%%%%%%@%%%%II__I| Pls Enter Here ==> \033[00m')




    if (choose == '1'):
        print('Chrome Automation is selected!' )
        sleep(0.5)
        print('Choose 1 of the Option below:')
        sleep(0.5)
        print('For Auto_configuration: 1')
        sleep(0.2)
        print('For Manual_configuration: 0')
        take = input('==> ')
        if (take == '1'):
            print('Setting up the Auto_configuration!')
            sleep(1)
            print('-------------------------------------------------')
            sleep(0.5)
            print('Enter the url for the Auto_viewer:')
            urlx = input('==> ')
            print('{+} Checking for the Webdriver.............')
            sleep(1)

            print('Note: For HELP Press "5"!')
            take1 = input('Enter the Path of the WebDriver:\n')
            print('Select the Window mode:')
            print('Max_window = 1, Default_window = 2, Min_window = 3')

            ask = input('')
            if (ask == '1'):
                def yes_max1():
                    from selenium import webdriver
                    from time import sleep
                    link1 = 'https://'

                    browser = webdriver.Chrome(executable_path=take1)
                    browser.maximize_window()

                    url = link1 + urlx
                    browser.get(url)

                    refresh_rate = int(50)


                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_max1()

            elif (ask == '2'):
                def yes_default1():
                    from selenium import webdriver
                    from time import sleep
                    link1 = 'https://'

                    browser = webdriver.Chrome(executable_path=take1)

                    url = link1 + urlx
                    browser.get(url)

                    refresh_rate = int(50)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()

                yes_default1()

            elif (ask == '3'):
                def yes_min1():
                    from selenium import webdriver
                    from time import sleep
                    link1 = 'https://'

                    browser = webdriver.Chrome(executable_path=take1)
                    browser.minimize_window()

                    url = link1 + urlx
                    browser.get(url)

                    refresh_rate = int(50)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()

                yes_min1()
            else:
                lol()
            if (take1 == '5'):
                print('Recommended is Chrome for better Automation!')
                print('For Chrome = 1, For Firefox = 0')

                take3 = input('==> ')
                if (take3 == '1'):
                    print('By Default Paths for chromedriver.exe:')
                    print('Windows: C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
                    print('Linux: /usr/bin/google-chrome/chromedriver.exe')
                    print('Mac: /Applications/Google\Chrome.app/Contents/MacOS/Google\Chrome/chromedriver.exe')
                    print('Note: To download the driver visit: https://chromedriver.chromium.org/downloads')
                    print('Do you wanna Continue?[1/0]')
                    take5 = input('==> ')
                    if (take5 == ' 1'):
                        youtube()
                    elif (take5 == '0'):
                        exit()
                    else:
                        lol()


                elif (take3 == '0'):
                    print('By Default Paths for geckodriver.exe:')
                    print('Note: To download the driver visit: https://github.com/mozilla/geckodriver/releases/tag/v0.26.0')
                    print('Do you wanna Continue?[1/0]')
                    take5 = input('==> ')
                    if (take5 == ' 1'):
                        youtube()
                    elif (take5 == '0'):
                        exit()
                    else:
                        lol()
                else:
                    print('Error')
                    print('Lol!')
                    print('         _       _')
                    print('        | |     | |')
                    print('        | | ___ | |')
                    print('        | |/ _ \| |')
                    print('        | | (_) | |')
                    print('        |_|\___/|_|')
                    exit()


        elif (take == '0'):

            print('Setting up the Manual_configuration!')
            sleep(1)
            print('-------------------------------------------------')
            sleep(0.5)
            print('Note: Use https:// or http:// before url!')
            sleep(1)
            print('Enter the url for the Auto_viewer:')
            urlx = input('==> ')
            print('{+} Checking for the Webdriver.............')
            sleep(1)

            print('Note: For HELP Press "5"!')
            take1 = input('Enter the Path of the WebDriver:\n')
            print('Select the Window mode:')
            print('Max_window = 1, Default_window = 2, Min_window = 3')

            ask = input('')
            rate = input('Enter The Refresh_Rate Speed:\n')


            if (ask == '1'):
                def yes_max1():
                    from selenium import webdriver
                    from time import sleep


                    browser = webdriver.Chrome(executable_path=take1)
                    browser.maximize_window()

                    url = urlx
                    browser.get(url)

                    refresh_rate = int(rate)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()




                yes_max1()

            elif (ask == '2'):
                def yes_default1():
                    from selenium import webdriver
                    from time import sleep


                    browser = webdriver.Chrome(executable_path=take1)

                    url = urlx
                    browser.get(url)

                    refresh_rate = int(50)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_default1()

            elif (ask == '3'):
                def yes_min1():
                    from selenium import webdriver
                    from time import sleep


                    browser = webdriver.Chrome(executable_path=take1)
                    browser.minimize_window()

                    url = urlx
                    browser.get(url)

                    refresh_rate = int(rate)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_min1()
            else:
                lol()
            if (take1 == '5'):
                print('Recommended is Chrome for better Automation!')
                print('For Chrome = 1, For Firefox = 0')

                take3 = input('==> ')
                if (take3 == '1'):
                    print('By Default Paths for chromedriver.exe:')
                    print('Windows: C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
                    print('Linux: /usr/bin/google-chrome/chromedriver.exe')
                    print('Mac: /Applications/Google\Chrome.app/Contents/MacOS/Google\Chrome/chromedriver.exe')
                    print('Note: To download the driver visit: https://chromedriver.chromium.org/downloads')
                    print('Do you wanna Continue?[1/0]')
                    take5 = input('==> ')
                    if (take5 == ' 1'):
                        youtube()
                    elif (take5 == '0'):
                        exit()
                    else:
                        lol()


                elif (take3 == '0'):
                    print('By Default Paths for geckodriver.exe:')
                    print(
                        'Note: To download the driver visit: https://github.com/mozilla/geckodriver/releases/tag/v0.26.0')
                    print('Do you wanna Continue?[1/0]')
                    take5 = input('==> ')
                    if (take5 == ' 1'):
                        youtube()
                    elif (take5 == '0'):
                        exit()
                    else:
                        lol()
                else:
                    print('Error')
                    print('Lol!')
                    print('         _       _')
                    print('        | |     | |')
                    print('        | | ___ | |')
                    print('        | |/ _ \| |')
                    print('        | | (_) | |')
                    print('        |_|\___/|_|')
                    exit()




        else:
            lol()



    elif (choose == '2'):
        print('FireFox Automation is selected!')


        sleep(0.5)
        print('Choose 1 of the Option below:')
        sleep(0.5)
        print('For Auto_configuration: 1')
        sleep(0.2)
        print('For Manual_configuration: 0')
        take = input('==> ')
        if (take == '1'):
            print('Setting up the Auto_configuration!')
            sleep(1)
            print('-------------------------------------------------')
            sleep(0.5)
            print('Enter the url for the Auto_viewer:')
            urlx = input('==> ')
            print('{+} Checking for the webdriver.............')
            sleep(1)

            print('Note: For HELP Press "5"!')
            take1 = input('Enter the Path of the geckodriver:\n')
            print('Select the Window mode:')
            print('Max_window = 1, Default_window = 2, Min_window = 3')

            ask = input('')


            if (ask == '1'):
                def yes_max1():
                    from selenium import webdriver
                    from time import sleep


                    browser = webdriver.Firefox(executable_path=take1)
                    browser.maximize_window()
                    link1 = 'https://'

                    url = link1+urlx
                    browser.get(url)

                    refresh_rate = int(rate)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_max1()

            elif (ask == '2'):
                def yes_default1():
                    from selenium import webdriver
                    from time import sleep
                    link1 = 'https://'

                    browser = webdriver.Firefox(executable_path=take1)

                    url = link1 + urlx
                    browser.get(url)

                    refresh_rate = int(50)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()

                yes_default1()

            elif (ask == '3'):
                def yes_min1():
                    from selenium import webdriver
                    from time import sleep
                    link1 = 'https://'

                    browser = webdriver.Firefox(executable_path=take1)
                    browser.minimize_window()

                    url = link1 + urlx
                    browser.get(url)

                    refresh_rate = int(50)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()

                yes_min1()
            else:
                lol()
            if (take1 == '5'):
                print('Recommended is Chrome for better Automation!')
                print('For Chrome = 1, For Firefox = 0')

                take3 = input('==> ')
                if (take3 == '1'):
                    print('By Default Paths for chromedriver.exe:')
                    print('Windows: C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
                    print('Linux: /usr/bin/google-chrome/chromedriver.exe')
                    print('Mac: /Applications/Google\Chrome.app/Contents/MacOS/Google\Chrome/chromedriver.exe')
                    print('Note: To download the driver visit: https://chromedriver.chromium.org/downloads')
                    print('Do you wanna Continue?[1/0]')
                    take5 = input('==> ')
                    if (take5 == ' 1'):
                        youtube()
                    elif (take5 == '0'):
                        exit()
                    else:
                        lol()


                elif (take3 == '0'):
                    print('By Default Paths for geckodriver.exe:')
                    print('Note: To download the driver visit: https://github.com/mozilla/geckodriver/releases/tag/v0.26.0')
                    print('Do you wanna Continue?[1/0]')
                    take5 = input('==> ')
                    if (take5 == ' 1'):
                        youtube()
                    elif (take5 == '0'):
                        exit()
                    else:
                        lol()

                else:
                    print('Error')
                    print('Lol!')
                    print('         _       _')
                    print('        | |     | |')
                    print('        | | ___ | |')
                    print('        | |/ _ \| |')
                    print('        | | (_) | |')
                    print('        |_|\___/|_|')
                    exit()

        elif (take == '0'):

            print('Setting up the Manual_configuration!')
            sleep(1)
            print('-------------------------------------------------')
            sleep(0.5)
            print('Note: Use https:// or http:// before url!')
            sleep(1)
            print('Enter the url for the Auto_viewer:')
            urlx = input('==> ')
            print('{+} Checking for the Webdriver.............')
            sleep(1)

            print('Note: For HELP Press "5"!')
            take1 = input('Enter the Path of the WebDriver:\n')
            print('Select the Window mode:')
            print('Max_window = 1, Default_window = 2, Min_window = 3')

            ask = input('')
            rate = input('Enter The Refresh_Rate Speed:\n')


            if (ask == '1'):
                def yes_max1():
                    from selenium import webdriver
                    from time import sleep

                    browser = webdriver.Firefox(executable_path=take1)
                    browser.maximize_window()

                    url = urlx
                    browser.get(url)

                    refresh_rate = int(rate)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_max1()

            elif (ask == '2'):
                def yes_default1():
                    from selenium import webdriver
                    from time import sleep

                    browser = webdriver.Firefox(executable_path=take1)

                    url = urlx
                    browser.get(url)

                    refresh_rate = int(50)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_default1()

            elif (ask == '3'):
                def yes_min1():
                    from selenium import webdriver
                    from time import sleep

                    browser = webdriver.Firefox(executable_path=take1)
                    browser.minimize_window()

                    url = urlx
                    browser.get(url)

                    refresh_rate = int(rate)

                    while True:
                        sleep(refresh_rate)
                        browser.refresh()


                yes_min1()


        else:
            lol()

        def yes():
            from selenium import webdriver
            from time import sleep
            link2 = 'https://'

            browser = webdriver.Firefox(executable_path=link2+take1)

            url = link2+urlx
            browser.get(url)

            refresh_rate = int(50)

            while True:
                sleep(refresh_rate)
                browser.refresh()

        yes()


    else:
        print('Error')
        print('Lol!')
        print('         _       _')
        print('        | |     | |')
        print('        | | ___ | |')
        print('        | |/ _ \| |')
        print('        | | (_) | |')
        print('        |_|\___/|_|')
        exit()


# Anonymous Web mailer
def anony_mailer():

    import time
    import requests
    print('-----------------------------------------------------------------------')
    print('\033[43m Note: This script needs Active Internet Access!\033[00m')
    print('\033[31m Do you have Internet Access?[1/0]\033[00m')
    internet = input('==> ')
    if (internet == '1'):

        try:
            request = requests.get('https://www.google.com')
            if request:
                print('\033[33m---------Active!---------\033[00m')
                time.sleep(0.3)
                print('{+} Starting the Script........')
                time.sleep(0.3)
                print('{++} Started!')
                time.sleep(0.3)
                print('-----------------------------------------')
                time.sleep(0.4)

        except requests.ConnectionError:
            print('No Internet Access!')
            time.sleep(0.5)
            anony_mailer()

    elif (internet == '0'):
        anony_mailer()
    else:
        lol()

    def anonymous_mailer():

        from selenium import webdriver
        from time import sleep
        from selenium.webdriver.chrome.options import Options

        print(
            '\033[45m--------------------------------+ Welcome TO The Anonymous_Web_Mailer! +--------------------------------\033[00m')
        print('\033[91m                               ------> USE IT- AT YOUR OWN RISK!<------\033[00m')

        print('    .-""""-.')
        print('   / -   -  \.')
        print('  |  .-. .- |')
        print('\033[31m  |  \o| |o (        ----> Disclaimer:\033[00m')
        print('\033[95m  \     ^    \.                  [*] You are requested not to misuse this Tool!\033[00m')
        print(
            "\033[95m  |'.  )--'  /|                  [*] Any illegal activities done by this tool can harm you only!\033[00m")
        print("\033[95m / / '-. .-'`\ \.                [*] Do not attempt to violate the law with anything contained here!\033[00m")
        print("\033[95m/ /'---` `---'\ \.               [*] If this is your intention, then LEAVE NOW!\033[00m")
        print("\033[95m'.__.       .__.'                {*} There are no Limitations in Hacking Field!\033[00m")
        print("\033[95m     \      '--.                 {*} Hacking is a skill which you had to develop on your own!\033[00m")
        print("\033[95m      '.        \.               {*} Stay Anonymous Always!!!\033[00m")
        print("\033[95m        `'---.   |               {-} USE VPN or Tor service while Using Bulker                                      \033[00m")
        print("\033[31m           ,__) /                                                     ~Kamaldeep Singh\033[00m")
        question2 = input("\033[31m            `..----> Do you agree?[1/0] ==>\033[00m ")

        if (question2 == '1'):
            print('----------------------------------------------------------')
            print('Select One Of The Following:-')
            print('\033[31m{+} For Anonymous_Web_mailing: 1\033[00m')
            print('\033[31m{+} For Bulk Anonymous_Web_mailing: 2\033[00m')

            question3 = input('==> ')
            if (question3 == '1'):
                print('Anonymous_Web_Mailer is Selected Now!')
                sleep(0.3)
                print('{+} Loading the Components.........')
                sleep(0.5)
                print('{+} Getting the Databases ready...........')
                sleep(0.5)
                print('{+} Getting the Web_Server_ready.................')
                sleep(0.5)
                print('{++} Done!')
                sleep(0.5)
                print('-------------------------------------------------------')
                print('Enter The Details Below:-')
                print(
                    '\033[31mNote: Invalid Details Will not snd the emails!!!\033[00m\nYou can specify any valid spoof address!\nTO avoid Spam Folder USE RECOMMENDATIONS TABLE-')

                print('               +------------------+------------+--------------+----------+--+--+--+')
                print(
                    '\033[31m               | Anonymous_Emails |  domain1   |   domain2    | domain3  |  |  |  |\033[00m')
                print('               +------------------+------------+--------------+----------+--+--+--+')
                print(
                    '\033[92m               | hacker9821       | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | anonymous        | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | anony541         | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | khacker1024      | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | hacker101        | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | titanhacker      | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print('               +------------------+------------+--------------+----------+--+--+--+\n')

                # driver path
                driver12 = str(input('Enter the Path of Chrome_Web_Driver: '))

                from_name = input('From Anonymous_Name: ')
                from_email = input('From Anonymous_Email: ')
                To = input('Victim_Email/TO: ')
                subject1 = input('Subject: ')
                TXT = input('Enter the Text/Body:\n')
                print('READY TO SND?[1/0]')
                ready = input('==> ')
                if (ready == '1'):
                    print('{+} Triggering Your Request {+}')
                    sleep(0.2)
                    print('Requesting the Web_Server.............')
                    sleep(0.2)
                    print('Pls wait until it Stops!')

                    class web_mailer():
                        def __init__(self, name, email, to, subject, text):
                            reiun = 'ti'
                            chrome_options = Options()
                            nil = 'https://'
                            chrome_options.add_argument('--headless')
                            nil2 = (reiun + 'nyu')

                            self.browser = webdriver.Chrome(
                                executable_path=driver12, options = chrome_options)
                            domain = 'com'
                            path = (nil + nil2 + 'rl.' + domain + '/3bl8pw6')

                            self.browser.get(path)
                            import time
                            start_time = time.time()

                            self.name = self.browser.find_element_by_xpath(
                                '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input')
                            sleep(1)
                            self.name.click()
                            print('\033[93m{+} Snding the from_name to Server...........\033[00m')
                            self.name.send_keys(name)

                            sleep(0.5)
                            self.email = self.browser.find_element_by_xpath(
                                '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[2]/td[2]/input')
                            sleep(0.5)
                            print('\033[93m{+} Snding the from_email to Server...........\033[00m')
                            self.email.send_keys(email)

                            sleep(0.5)
                            self.to = self.browser.find_element_by_xpath(
                                '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[3]/td[2]/input')
                            sleep(0.5)
                            print('\033[93m{+} Snding the Victim_email to Server...........\033[00m')
                            self.to.send_keys(to)

                            sleep(0.5)
                            self.subject = self.browser.find_element_by_xpath(
                                '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[4]/td[2]/input')
                            sleep(0.5)
                            print('\033[93m{+} Snding the Subject to Server...........\033[00m')
                            self.subject.send_keys(subject)

                            self.text = self.browser.find_element_by_xpath(
                                '/html/body/div[2]/div[2]/form/table[3]/tbody/tr[2]/td[2]/textarea')
                            sleep(0.5)
                            self.text.click()
                            print('\033[93m{+} Snding the TXT to Server...........\033[00m')
                            self.text.send_keys(text)
                            sleep(0.5)
                            self.send = self.browser.find_element_by_xpath(
                                '/html/body/div[2]/div[2]/form/table[3]/tbody/tr[4]/td[2]/input[2]')
                            print('\033[31m{++} SENDING...........\033[00m')
                            self.send.click()

                            self.browser.close()
                            end_time = time.time()
                            total = float((end_time - start_time))

                            print('\033[33m{+}  Successfully Snded Your Anonymous_Mail TO \033[00m' + To)
                            sleep(0.2)
                            print('Time Elapsed:- ')
                            print(total)
                            sleep(1)
                            print('-----------------------------------------------------------')
                            sleep(0.1)
                            print('Exiting.........')
                            print('Do You Wanna Continue?[1/0]')
                            continue1 = input('==> ')
                            if (continue1 == '1'):
                                anonymous_mailer()
                            else:
                                exit()


                    web_mailer(from_name, from_email, To, subject1, TXT)

                else:
                    lol()

            elif (question3 == '2'):

                print('Bulk Anonymous_Web_Mailer is Selected Now!')
                sleep(0.3)
                print('{+} Loading the Components.........')
                sleep(0.5)
                print('{+} Getting the Databases ready...........')
                sleep(0.5)
                print('{+} Getting the Web_Server_ready.................')
                sleep(0.5)
                print('{++} Done!')
                sleep(0.5)
                print('-------------------------------------------------------')
                print('Enter The Details Below:-')
                print(
                    '\033[31mNote: Invalid Details Will not snd the emails!!!\033[00m\nYou can specify any valid spoof address!\nTO avoid Spam Folder USE RECOMMENDATIONS TABLE-')

                print('               +------------------+------------+--------------+----------+--+--+--+')
                print(
                    '\033[31m               | Anonymous_Emails |  domain1   |   domain2    | domain3  |  |  |  |\033[00m')
                print('               +------------------+------------+--------------+----------+--+--+--+')
                print(
                    '\033[92m               | hacker9821       | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | anonymous        | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | anony541         | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | khacker1024      | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | hacker101        | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m')
                print(
                    '\033[92m               | titanhacker      | @gmail.com |   @yahoo.com |  .in/.co |  |  |  |\033[00m11')
                print('               +------------------+------------+--------------+----------+--+--+--+\n')

                # driver path
                driver12 = str(input('Enter the Path of Chrome_Web_Driver: '))

                from_name = input('From Anonymous_Name: ')
                from_email = input('From Anonymous_Email: ')
                To = input('Victim_Email/TO: ')
                subject1 = input('Subject: ')
                TXT = input('Enter the Text/Body:\n')
                number = int(input('\033[92mEnter the Number of times you wanna SND:-\n\033[00m'))
                print('READY TO SND?[1/0]')
                ready = input('==> ')
                if (ready == '1'):
                    print('{+} Triggering Your Request {+}')
                    sleep(0.2)
                    print('Requesting the Web_Server.............')
                    sleep(0.2)
                    print('Pls wait until it Stops!')

                    class web_mailer1():
                        def __init__(self, name, email, to, subject, text):
                            for i in range(1, number + 1):
                                sleep(0.3)
                                print('\033[31mThis Process Will Be Repeated as per your demand!\033[00m')
                                reiun = 'ti'
                                chrome_options = Options()
                                nil = 'https://'
                                chrome_options.add_argument('--headless')
                                nil2 = (reiun + 'nyu')

                                self.browser = webdriver.Chrome(
                                    executable_path=driver12, options = chrome_options)
                                domain = 'com'
                                path = (nil + nil2 + 'rl.' + domain + '/3bl8pw6')

                                self.browser.get(path)
                                import time
                                start_time = time.time()

                                self.name = self.browser.find_element_by_xpath(
                                    '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[1]/td[2]/input')
                                sleep(0.5)
                                self.name.click()
                                print('\033[93m{+} Snding the from_name to Server...........\033[00m')
                                self.name.send_keys(name)

                                sleep(0.5)
                                self.email = self.browser.find_element_by_xpath(
                                    '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[2]/td[2]/input')
                                sleep(0.5)
                                print('\033[93m{+} Snding the from_email to Server...........\033[00m')
                                self.email.send_keys(email)

                                sleep(0.5)
                                self.to = self.browser.find_element_by_xpath(
                                    '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[3]/td[2]/input')
                                sleep(0.5)
                                print('\033[93m{+} Snding the Victim_email to Server...........\033[00m')
                                self.to.send_keys(to)

                                sleep(0.5)
                                self.subject = self.browser.find_element_by_xpath(
                                    '/html/body/div[2]/div[2]/form/table[1]/tbody/tr[4]/td[2]/input')
                                sleep(0.5)
                                print('\033[93m{+} Snding the Subject to Server...........\033[00m')
                                self.subject.send_keys(subject)

                                self.text = self.browser.find_element_by_xpath(
                                    '/html/body/div[2]/div[2]/form/table[3]/tbody/tr[2]/td[2]/textarea')
                                sleep(0.5)
                                self.text.click()
                                print('\033[93m{+} Snding the TXT to Server...........\033[00m')
                                self.text.send_keys(text)
                                sleep(0.5)
                                self.send = self.browser.find_element_by_xpath(
                                    '/html/body/div[2]/div[2]/form/table[3]/tbody/tr[4]/td[2]/input[2]')
                                print('\033[31m{++} SENDING...........\033[00m')
                                self.send.click()
                                sleep(0.5)
                                self.browser.close()
                                end_time = time.time()
                                total = (end_time - start_time)

                                print('\033[33m{+}  Successfully Snded Your Anonymous_Mail TO \033[00m' + To)
                                sleep(0.5)
                                print('Time Elapsed:- ')
                                print(total)
                                sleep(0.4)
                                print('-----------------------------------------------------------')
                                sleep(0.1)
                                print('Exiting.........')


                    web_mailer1(from_name, from_email, To, subject1, TXT)
                    exit()




                else:
                    lol()




            else:
                lol()







        elif (question2 == '0'):
            anony_mailer()
        else:
            lol()




    anonymous_mailer()







main()











