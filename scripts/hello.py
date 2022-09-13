#!/usr/bin/env python3
from dev_aberto import hello
from babel.dates import format_date

import gettext
gettext.install('cli', localedir='locale') 

if __name__ == '__main__':
    date, name = hello()
    print(_('Último commit feito em:'), format_date(date), _(' por'), name)
