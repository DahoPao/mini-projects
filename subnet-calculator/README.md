# subnet calculator

Type an ip with a cidr and get the subnet info you'd normally work out by
hand during CCNA practice.

```
ip/cidr> 192.168.1.77/26

ip address:      192.168.1.77/26
subnet mask:     255.255.255.192
wildcard mask:   0.0.0.63
network:         192.168.1.64
broadcast:       192.168.1.127
first host:      192.168.1.65
last host:       192.168.1.126
usable hosts:    62
```

Also accepts a normal mask instead of /number, which is handy when a
question gives you `255.255.255.192` instead of `/26`:

```
ip/cidr> 10.0.0.5/255.255.255.192
```

The math is done with bit operations (ip & mask for the network address),
not a library, so I'd actually understand what's happening underneath.
