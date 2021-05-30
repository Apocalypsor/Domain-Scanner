from Check.check import check

from p_tqdm import p_map
from itertools import product
import sys
import os

alphabet = "abcdefghijklmnopqrstuvwxyz"

if __name__ == "__main__":
    domain_length = (4, 5, 6)
    domain_suff = ".com"

    if isinstance(domain_length, int):
        domain_length = domain_length

    for length in domain_length:
        print(
            f"--------------------Start for {length} alphabet(s)!--------------------"
        )
        domain_pref = tuple(product(alphabet, repeat=length))
        domain = ["".join(pref) + domain_suff for pref in domain_pref]

        result = p_map(check, domain)

        print(
            "----------------------------------Done!----------------------------------"
        )
