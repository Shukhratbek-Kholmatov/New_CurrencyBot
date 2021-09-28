import requests
key="bc8e244ffc83be150bcb8e62"
def exchange(currency,amount):
    if currency=="UZS-USD":
        currency="UZS"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/USD/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} UZS*\n●Yo'nalish:*UZS-USD*\n⚡️Konvertatsiya:*{r_json['conversion_result']} USD*"
        except:
            response="Xatolik yuz berdi"
    elif currency=="USD-UZS":
        currency="USD"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/UZS/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} USD*\n●Yo'nalish:*USD-UZS*\n⚡️Konvertatsiya:*{r_json['conversion_result']} UZS*"
        except:
           response="Xatolik yuz berdi"
           
    elif currency=="UZS-RUB":
        currency="UZS"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/RUB/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} UZS*\n●Yo'nalish:*UZS-RUB*\n⚡️Konvertatsiya:*{r_json['conversion_result']} RUB*"
        except:
            response="Xatolik yuz berdi"
    elif currency=="RUB-UZS":
        currency="RUB"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/UZS/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} RUB*\n●Yo'nalish:RUB-UZS\n⚡️Konvertatsiya:*{r_json['conversion_result']} UZS*"
        except:
           response="Xatolik yuz berdi"
    elif currency=="USD-RUB":
        currency="USD"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/RUB/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} USD*\n●Yo'nalish:*USD-RUB*\n⚡️Konvertatsiya:*{r_json['conversion_result']} RUB*"
        except:
            response="Xatolik yuz berdi"
    elif currency=="RUB-USD":
        currency="RUB"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/USD/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} RUB*\n●Yo'nalish:*RUB-USD*\n⚡️Konvertatsiya:*{r_json['conversion_result']} USD*"
        except:
            response="Xatolik yuz berdi"
    elif currency=="TRY-USD":
        currency="TRY"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/USD/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} TRY*\n●Yo'nalish:*TRY-USD*\n⚡️Konvertatsiya:*{r_json['conversion_result']} USD*"
        except:
            response="Xatolik yuz berdi"
    elif currency=="USD-TRY":
        currency="USD"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/TRY/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} USD*\nYo'nalish:*USD-TRY*\n⚡️Konvertatsiya:*{r_json['conversion_result']} TRY*"
        except:
            response="Xatolik yuz berdi"
    elif currency=="TRY-RUB":
        currency="TRY"
        Amount=float(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/RUB/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} TRY*\nYo'nalish:*TRY-RUB*\n⚡️Konvertatsiya:*{r_json['conversion_result']} RUB*8"
        except:
            response="Xatolik yuz berdi"
    elif currency=="RUB-TRY":
        currency="RUB"
        Amount=int(amount)
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/{currency}/TRY/{Amount}")
            r_json=r.json()
            response=f"●Miqdor:*{amount} RUB*\n●Yo'nalish:*RUB-TRY*\n⚡️Konvertatsiya:*{r_json['conversion_result']} TRY*"
        except:
            response="Xatolik yuz berdi"
    return response


def get_rate(currency):
    if currency=="USD":
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/USD/UZS")
            r_json=r.json()
            response=f"1 dollar = {r_json['conversion_rate']} so'm"
        except:
            response=" "
    elif currency=="RUB":
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/RUB/UZS")
            r_json=r.json()
            response=f"1 rubl = {r_json['conversion_rate']} so'm"
        except:
            response=" "
    elif currency=="TRY":
        try:
            r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/TRY/UZS")
            r_json=r.json()
            response=f"1 lira = {r_json['conversion_rate']} so'm"
        except:
            response=" "
    return response

  
def get_rates():
            try:
                r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/EUR/UZS")
                r_json=r.json()
                response1=f"1 Yevro = {r_json['conversion_rate']} so'm"
                r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/USD/UZS")
                r_json=r.json()
                response2=f"1 AQSH dollari = {r_json['conversion_rate']} so'm"
                r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/RUB/UZS")
                r_json=r.json()
                response3=f"1 Rossiya rubli = {r_json['conversion_rate']} so'm"
                r=requests.get(f"https://v6.exchangerate-api.com/v6/{key}/pair/TRY/UZS")
                r_json=r.json()
                response4=f"1 Turkiya lirasi = {r_json['conversion_rate']} so'm"
                responses=f"{response1}\n{response2}\n{response3}\n{response4}"
            except:
                responses=" "
    
            return responses 
    