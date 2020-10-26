from p_tqdm import p_umap
import whois
from itertools import product
import sys
import os

alphabet = "abcdefghijklmnopqrstuvwxyz"

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def availableQuery(x, domain_suff):
    pref = ''.join(x)
    domain = pref + domain_suff
    retries = 0

    while retries < 3:
        try:
            blockPrint()
            response = whois.whois(domain)
            return response
            enablePrint()
            if response == 'Socket not responding':
                retries += 1
            else:
                retries = 3
        except whois.parser.PywhoisError as e:
            print('\n  Available:', domain, '|', str(e).split('\n')[0])
            return domain + '\n'
        except:
            retries += 1


if __name__ == '__main__':
    domain_length = 2
    domain_suff = '.moe'

    print('--------------------Start!--------------------')
    domain_pref = tuple(product(alphabet, repeat=domain_length))
    domain_suff = [domain_suff for _ in domain_pref]

    result = p_umap(availableQuery, domain_pref, domain_suff)

    print('--------------------Done!--------------------')
    print(result)
    result = set(result).remove(None)

    if result:
        with open('domains.txt', 'w') as f:
            f.writelines(result)
    else:
        print('Nothing found!')