class Phone:
    color = 'black'
    features = ['camera','waterproof','ram 8gb']
    def call(self):
        print('ring ring ring')
    def send_sms(self,number,text):
        sms = f'sending {text} to {number}'
        return sms
    
my_phone = Phone()
my_phone.call()
print(my_phone.send_sms('01316','abcd'))