# Errdisable Interfaces

You may notice that the DCI is not functioning. There is an issue in the lab envrionment where interfaces (typically on the borderleafs) go into errdisable mode. You can resolve this simply by doing a `shut` and then `no shut`. 

You can identify the interfaces with `show ip interface brief`

```
➜  project ssh borderleaf1
The authenticity of host 'borderleaf1 (192.168.0.25)' can't be established.
ECDSA key fingerprint is SHA256:xn450X81ZJjfSp503NQ5D/5RT0bV8B7nH12c341JQrw.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'borderleaf1,192.168.0.25' (ECDSA) to the list of known hosts.
borderleaf1#show ip interface brief 
                                                                                  Address
Interface         IP Address              Status       Protocol            MTU    Owner  
----------------- ----------------------- ------------ -------------- ----------- -------
Ethernet1         192.168.99.0/31         up           up                 1500           
Ethernet2         192.168.99.2/31         up           up                 1500           
Ethernet3         192.168.103.17/31       down         down               1500           
Ethernet4         192.168.103.19/31       down         down               1500          
```

In this case Ethernet3 and Ethernet4 are in errdisable.

```
borderleaf1#conf
borderleaf1(config)#int e3-4
borderleaf1(config-if-Et3-4)#shutdown 
borderleaf1(config-if-Et3-4)#no shutdown 
borderleaf1(config-if-Et3-4)#
```


