## ZEUS Tracker   
https://zeustracker.abuse.ch/blocklist.php

### Overview

ZeuS Tracker provides you the possibility to track ZeuS Command & Control servers (C&C) and malicious hosts which are hosting ZeuS files around the world and
provides you a domain and a IP-blocklist. ZeuS tracker captures and tracks ZeuS hosts as well as the associated config files, binaries and dropezones. 
The main focus is to provide system administrators the possibility to block well-known ZeuS hosts and to avoid and detect ZeuS infections in their networks.

Normally, a ZeuS host consists of three components / URIs:
- a config file (mostly with file extension *.bin)
- a binary file which contains the newest version of the ZeuS trojan
- a dropzone (mostly a php file)

Some features of ZeuS are:
- Capture credentials out of HTTP-, HTTPS-, FTP- and POP3-traffic or out of the bot's protected storage (PStore).
- Group the infected clients into different botnets
- Integrated SOCKS-Proxy
- Web form to search the captured credentials
- Encrypted config file
- Function to kill the Operating System (see abuse.ch: "When a Botmaster goes REALLY mad")

ZeuS Tracker API  recommends the following three blocklists (recommended blocklists):


### ZeuS Tracker Domain Feeds (BadDomains)
ZeuS domain blocklist (BadDomains)
If you want to block domain names used by the ZeuS trojan, you should use this list. 
The ZeuS domain blocklist (BadDomains) is the recommended blocklist if you want to block only ZeuS domain names.
It excludes domain names that ZeuS Tracker believes to be hijacked (level 2). Hence the false positive rate should be much lower compared to the standard ZeuS domain blocklist.

For more information on this feed go to: https://zeustracker.abuse.ch/blocklist.php?download=baddomains

### ZeuS Tracker IP Feeds (BadIPs)
This blocklists only includes IPv4 addresses that are used by the ZeuS trojan. It is the recommened blocklist if you want to block only ZeuS IPs.
It excludes IP addresses that ZeuS Tracker believes to be hijacked (level 2) or belong to a free web hosting provider (level 3).
Hence the false postive rate should be much lower compared to the standard ZeuS IP blocklist.

For more information on this feed go to: https://zeustracker.abuse.ch/blocklist.php?download=badips

### ZeuS Tracker Compromised URL Blocklist
This blocklist only contains compromised / hijacked websites (level 2) which are being abused by cybercriminals to host a ZeuS botnet controller. Since blocking the FQDN or IP address of compromised host would cause a lot of false positives, the ZeuS compromised URL blocklist contains the full URL to the ZeuS 
config, dropzone or malware binary instead of the FQDN / IP address.

For more information on this feed go to: https://zeustracker.abuse.ch/blocklist.php?download=compromised

### PRE-REQUISITES to use ZeuS Tracker feeds and DNIF  
Outbound access required to request ZeuS Tracker feeds API

| Protocol   | Source IP  | Source Port  | Direction	 | Destination Domain | Destination Port  |  
|:------------- |:-------------|:-------------|:-------------|:-------------|:-------------|  
| TCP | AD,A10 | Any | Egress	| github.com | 443 |
| TCP | AD,A10 | Any | Egress	| zeustracker.abuse.ch | 443 | 


### Using the Zeus Tracker feeds API
 The Zeus Tracker feeds API is found on github at

https://github.com/dnif/enrich-zeustracker

#### Getting started with Zeus Tracker feeds API

1. #####    Login to your AD, A10 containers  
   ACCESS DNIF CONTAINER VIA SSH : [Click To Know How](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. #####    Move to the ‘/dnif/<Deployment-key/enrichment_plugin’ folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/enrichment_plugin/
```
3. #####   Clone using the following command  
```  
git clone https://github.com/dnif/enrich-zeustracker.git zeustracker
```
### API feed output structure
  | Fields        | Description  |
| ------------- |:-------------:|
| EvtType      | An IP/Domain/URL |
| EvtName      | The IOC      |
| IntelRef | Feed Name      |
| IntelRefURL | Feed URL      |
| ThreatType | DNIF Feed Identification Name |      

An example of API feed output
```
{'EvtType': 'URL',
'EvtName': 'www.basecinco.com.ar/alumno309/images/secure.php', 
'AddFields': {
'IntelRef': ['ZUESTRACKER'],
'IntelRefURL': ['https://zeustracker.abuse.ch/blocklist.php?download=compromised'], 
'ThreatType': ['ZuesC&C']
}}
```
