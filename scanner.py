import multiprocessing
from itertools import product
import tqdm
import whois

alphabet = "abcdefghijklmnopqrstuvwxyz"

def availableQuery(x):
    pref = "".join(x)
    domain = pref + ".me"

    try:
        whois.whois(domain)
    except:
        print('Available:', domain)
        return domain + '\n'

if __name__ == '__main__':
    domain_length = 3
    pool = multiprocessing.Pool(8)
    tasks = tuple(product(alphabet, repeat=domain_length))

    for _ in tqdm.tqdm(pool_outputs := pool.imap_unordered(availableQuery, tasks), total=len(tasks)):
        pass

    with open('domain.txt', 'w') as f:
        f.writelines(pool_outputs)

    print("Done!")