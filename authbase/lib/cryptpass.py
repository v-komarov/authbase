#!/usr/bin/env python
#coding:utf-8
from Crypto.Cipher import AES
import base64
from cryptkey	import	Key

# размер блока шифрования
BLOCK_SIZE = 32

# символ, использующийся для дополнения шифруемых данных
# до размера, кратного 32 байтам
PADDING = '{'

# функция дополнения
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# функции шифрования и расшифрования
# результат дополнительно обертывается в base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# ключ
#secret = 'him eyes enomous'
secret = Key()


# создаем объект
cipher = AES.new(secret)


# шифруем строку
def	Encoded(string):

    return EncodeAES(cipher, string)


# расшифровываем строку
def	Decoded(string):

    return DecodeAES(cipher, string)

