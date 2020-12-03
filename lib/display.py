# -*- coding: utf-8 -*- #
# Blog: www.clownsaw.tk #
# Autor: Clown Saw      #
#########################

from os import system
from time import sleep 
from colorama import Fore 
from random import choice 
from platform import system as platform 
from .const import debug, version, banners


class Display(object):

    def __init__(self):
        self.delay = 1.3
        self.is_shutdown = False 
        self.colors_disabled = True 
        self.cls = 'cls' if platform() == 'Windows' else 'clear'
        
    def clear(self):
        if not debug or self.colors_disabled:
            system(self.cls)

            if self.colors_disabled:
                self.colors_disabled = False 
        else:
            print('\n\n')           
    
    def is_vulner(self, link):
        print('{3}[{0}V{3}] {1}{2}{3} \033[1;30m #Vulnerable'.format(
            Fore.GREEN, Fore.CYAN, link, Fore.YELLOW
        ))
    
    def is_not_vulner(self, link):
        print('{0}[{1}N{0}] {4}{3}{4}'.format(
            Fore.RED, Fore.YELLOW, Fore.WHITE, link, Fore.MAGENTA
        ))
       
    def shutdown(self, total=0):
        if total:
            # print('\n{0}[{1}*{0}] {2}Total found: {3}{4}'.format(
            #     Fore.YELLOW, Fore.GREEN, Fore.WHITE, total, Fore.RESET
            # ))

            self.primary('Total found: ' + str(total) )
        else:
            print('')

        print('{0}[{1}!{0}] {2}Shutting Down ...{3}'.format(
            Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
        ))

        sleep(self.delay)
    
    def info(self, msg):
        print('{0}[{1}i{0}] {2}{3}{4}'.format(
            Fore.YELLOW, Fore.CYAN, Fore.WHITE, msg, Fore.RESET
        ))

        sleep(2.5)
    
    def warning(self, msg):
        print('{0}[{1}!{0}] {1}{2}{3}'.format(
            Fore.YELLOW, Fore.RED, msg, Fore.RESET
        ))

        sleep(self.delay)
    
    def primary(self, data): 
        print('\n\n{0}[{1}*{0}] {2}{3}{4}'.format(
            Fore.YELLOW, Fore.GREEN, Fore.WHITE, data, Fore.RESET
        ))
    
    def banner(self):        
        self.clear() 

        banner = choice(banners)
        color = choice([Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.MAGENTA, Fore.BLUE, Fore.CYAN])

        print(color)
        print(banner.format('{0}UwU{1}{2}'.format(Fore.WHITE, version, Fore.RESET)))