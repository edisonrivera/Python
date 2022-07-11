import socket


def get_domain(dns: str):
    name, alias, adresslist = socket.gethostbyaddr(dns)
    return name

if __name__ == "__main__":
    dns = input("-> DNS: ")
    domain = get_domain(dns)
    print ("Domain:", domain)