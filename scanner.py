import multiprocessing
from itertools import product
import tqdm
import whois

alphabet = "abcdefghijklmnopqrstuvwxyz"

def availableQuery(x):
    pref = "".join(x)
    domain = pref + ".me"
    retries = 0

    while retries < 3:
        try:
            response = whois.whois(domain)
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
    domain_length = 1
    pool = multiprocessing.Pool(8)
    tasks = tuple(product(alphabet, repeat=domain_length))

    for _ in tqdm.tqdm(pool.imap_unordered(availableQuery, tasks), total=len(tasks)):
        pass

    print("Done!")