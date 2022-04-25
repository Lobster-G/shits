import re


def print_result(pattern, string, _type):
    port = re.search(pattern, string).groups()[5]
    if port is not None:
        print(f"{_type}, Port: {port}")
    else:
        print(f"{_type}")


check = str(input("Введите данные: "))

ipv4 = re.compile(r"^([01]?\d\d?|2[0-4]\d|25[0-5])\."
                  r"([01]?\d\d?|2[0-4]\d|25[0-5])\."
                  r"([01]?\d\d?|2[0-4]\d|25[0-5])\."
                  r"([01]?\d\d?|2[0-4]\d|25[0-5])"
                  r"(:((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|"
                  r"(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4})))?$",
                  re.UNICODE)

OKATO = re.compile(r"(\d{2})\."
                   r"(\d{3})\."
                   r"(\d{3})\."
                   r"(\d{3})"
                   r"(:((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|"
                   r"([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4})))?$",
                   re.UNICODE)

if re.match(OKATO, check):
    print_result(OKATO, check, "OKATO")
elif re.match(ipv4, check):
    print_result(ipv4, check, "IP")
else:
    print("Некорректные даныне")
