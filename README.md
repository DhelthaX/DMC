DMC ![](https://cdn.discordapp.com/attachments/666990519913807875/728307101633347656/backpropagation_neural_network-64.png)
===
![pythonVer](https://img.shields.io/badge/python-v3.7-blue)
[![Twitter](https://img.shields.io/badge/twitter-@DhtX_-blue.svg)](https://twitter.com/DhtX_)

## Table of Contents

[TOC]

## Beginners Guide

This is a tool to check DMARC records for certain domains.

1. Download the DMC python script
2. Run it with Python3

### Usage
You can use in single domain mode or wordlist mode.
+ To use in domain mode use "-d" flag.
+ To use in wordlist mode use "-w" flag.

Eg:
``` 
python3 DMC.py -d DOMAIN.COM
python3 DMC.py -w /path/to/domainlist
```
![dmcPic](https://cdn.discordapp.com/attachments/666990519913807875/728303836887777331/unknown.png)
```
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        For a Single Domain
  -w WORDLIST, --wordlist WORDLIST
                        For a List of Domains

```

## Appendix and FAQ

:::info
[**Find any bug?** Feel free to submit your issue!](https://github.com/DhelthaX/DMC/issues)
:::

###### tags: `DMARC` `SPF` `DKIM` `EMAIL` `DNS`
