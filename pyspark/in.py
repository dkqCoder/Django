#encoding=utf-8
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import base64
import urllib2
import json
import requests
import re

def decrypt_rsa():
    print "start_rsa_key1"
    ase_key1='lymhrorVVWRZFGPM+uhJc9+xLxWKLYLigwqiuYFeQUj1OY78VaGL/IgOhCfIrX8laF5GLsLO5Y9fvXmfATzWhF0TUekrhRWZu+7RuLOnJNoVaVYw/Q/3rBtu+BIsMHFgU50TTx2iCK9eIDAD8oR1Cw5Sy2P8B6BtS+4eIZnYM9g='
    decryptor = RSA.importKey(open("./rsa_private_key.pem", "r").read())
    aes_key2=decryptor.decrypt(base64.b64decode(ase_key1))
    return aes_key2

def decrypt_aes(key, encrypt_text):
    print "start_rsa_text"
    cryptor = AES.new(key)
    return cryptor.decrypt(base64.b64decode(encrypt_text))

def get_data():
    # file ='./message1.txt'
    # with open(file,'r') as f:
    #     for line in f :
    #         print type(line),len(list(line)),line
    # pagehandler=urllib2.urlopen("http://paydayloan-10000035.file.myqcloud.com/cos/2017/01/13/message1.txt")
    pagehandler=urllib2.urlopen("http://paydayloanv4-1251122539.cossh.myqcloud.com/2017/11/07/1107_140822_2acfe8ff-4d1d-4de7-a5b6-9e55cc774e3c.txt")
    data=pagehandler.read()
    # print type(data),data
    return data
    # print requests.get("http://paydayloanv4-1251122539.cossh.myqcloud.com/2017/11/07/1107_140822_2acfe8ff-4d1d-4de7-a5b6-9e55cc774e3c.txt").content
    # print "get_data_success"

if __name__=='__main__':
    aes_key2=decrypt_rsa()
    data=get_data()
    print type(data),data
    d = decrypt_aes(aes_key2,data)

    print type(d), len(d) ,len(d.strip()), d
    l = len(d)
    print l
    print l-200
    print d.index("}]\"}")
    ll = d.index("}]\"}") + 2
    print ll
    s1 = d[9:ll].replace("\\","")
    print s1
    evd = eval(s1)
    print type(evd),evd,len(evd)
    for i in evd:
        print i['address'],i['body']

    # c = {"Data":"[{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日14:07完成支付宝人民币-900.00，人民币余额11.23。\",\"date\":\"2017-11-07 02:07:08\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日14:05完成转支人民币-661.14，人民币余额911.23。\",\"date\":\"2017-11-07 02:05:56\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"1069089786401\",\"body\":\"【马上消费金融】泄露验证码有信息被盗风险!9932为本次操作的验证码。您正在进行实名认证，如有疑问请联系4000368876。\",\"date\":\"2017-11-07 02:05:36\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日14:00完成银联代收人民币-2180.00，人民币余额1572.37。\",\"date\":\"2017-11-07 02:00:58\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日13:24完成代付人民币3500.00，人民币余额3752.37。\",\"date\":\"2017-11-07 01:24:37\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日11:54完成银联代收人民币-3970.30，人民币余额252.37。\",\"date\":\"2017-11-07 11:55:19\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日11:54完成支付宝发人民币2600.07，人民币余额4222.67。\",\"date\":\"2017-11-07 11:54:11\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日11:52完成代付人民币1436.00，人民币余额1622.60。\",\"date\":\"2017-11-07 11:52:12\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日10:52完成支付宝人民币-800.00，人民币余额186.60。\",\"date\":\"2017-11-07 10:52:32\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日10:49完成连连付款人民币810.00，人民币余额986.60。\",\"date\":\"2017-11-07 10:50:04\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"106902994991\",\"body\":\"【秒借贷】后天为您的（单号：201710281740131795213）还款日，需还1240.00元，记得登录还款哦。\",\"date\":\"2017-11-07 10:17:25\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"10690010293188027753\",\"body\":\"【花钱月上】您的账单今日到期，请登录花钱月上客户端进行处理，保持良好信用记录，谢谢您的配合。\",\"date\":\"2017-11-07 10:13:36\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"1069103829541\",\"body\":\"【意真金融】\\u003c指尖钱包\\u003e尊敬的唐太昌:您的借款于两天后到期,请及时登录指尖钱包APP还款,逾期将产生高额滞纳金哦!待还金额1500元,最后还款日2017-11-09.如已全额还款,请忽略此消息.\",\"date\":\"2017-11-07 09:14:58\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月07日00:59完成支付宝人民币-1800.00，人民币余额176.60。\",\"date\":\"2017-11-07 12:59:54\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日23:15完成代付人民币1425.00，人民币余额1976.60。\",\"date\":\"2017-11-06 11:15:46\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日23:07完成消费人民币-1500.00，人民币余额551.60。\",\"date\":\"2017-11-06 11:08:04\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日22:59完成消费人民币-1500.00，人民币余额2051.60。\",\"date\":\"2017-11-06 10:59:55\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日21:24完成微信零 X人民币2998.00，人民币余额3551.60。\",\"date\":\"2017-11-06 09:24:25\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日21:21完成财付通人民币-3000.00，人民币余额553.60。\",\"date\":\"2017-11-06 09:22:00\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日21:08完成支付宝发人民币500.00，人民币余额3553.60。\",\"date\":\"2017-11-06 09:08:42\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"},{\"address\":\"95599\",\"body\":\"【中国农业银行】您尾号9675账户11月06日21:05完成支付宝发人民币1098.90，人民币余额3053.60。\",\"date\":\"2017-11-06 09:05:30\",\"person\":\"\",\"read\":\"1\",\"status\":\"-1\",\"type\":\"1\"}]"}
    # print type(c)

    s2 = d[0:ll+2]
    print type(s2),s2
    s3 = json.loads(s2)
    print type(s3),s3['Data']
    # print eval(d.strip())[0]
    # print json.dumps(eval(d.strip()))

    # dd = re.compile("(Data['\"]?: *['\"])(.+)(['\"],)")
    # ddd = dd.search(d).group(2)
    # dddd = dd.sub(r"\1\3",d)
    # print type(dddd),dddd
    # for d in ev:
    #     print d['body']

    # ddd = json.loads(dd)
    # print type(ddd),ddd[0]
