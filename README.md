# py-geo-location
A simple Geo Location using Python 3

---

# Installation

 ## Linux

```shell
pip3 -r install requirements.txt
```
## Windows

```powershell
pip -r install requirements.txt
```

# Usage

## Linux 

```shell
python3 location.py
```

## Windows

```powershell
python location.py
```

# Options

```bash
1. Test on My IP
2. Test on My IP with detailed information
3. I want to enter an IP
4. I want to enter an IP and detailed information

```

### 1

Take your IP and give you some information

```json
{
    "ip": "190.61.38.0",
    "city": "San Salvador",
    "region": "Departamento de San Salvador",
    "country": "El Salvador"
}
```

### 2

Take your IP and give you detailed information

```json
{
    "ip": "190.61.38.0",
    "city": "San Salvador",
    "region": "Departamento de San Salvador",
    "country": "SV",
    "country_name": "El Salvador",
    "country_capital": "San Salvador",
    "country_tld": ".sv",
    "continent_code": "NA",
    "postal": "",
    "latitude": 13.6806,
    "longitude": -89.1803,
    "timezone": "America/El_Salvador",
    "country_calling_code": "+503",
    "currency": "USD",
    "currency_name": "Dollar",
    "languages": "es-SV",
    "country_population": 6420744
}
```

### 3 

You can enter the ip and gives you the same result as option 1

```json
{
    "ip": "222.174.201.19",
    "city": "Xintai",
    "region": "Shandong",
    "country": "China"
}

```

### 4

Same as third option but more detailed

```json
{
    "ip": "222.174.201.19",
    "city": "Xintai",
    "region": "Shandong",
    "country": "CN",
    "country_name": "China",
    "country_capital": "Beijing",
    "country_tld": ".cn",
    "continent_code": "AS",
    "postal": null,
    "latitude": null,
    "longitude": null,
    "timezone": null,
    "country_calling_code": "+86",
    "currency": "CNY",
    "currency_name": "Yuan Renminbi",
    "languages": "zh-CN,yue,wuu,dta,ug,za",
    "country_population": 1411778724
}

```

