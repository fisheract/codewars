def maskify(cc):
	if cc == None:
		return str(cc)
	else:
		if len(cc) > 4:
			cc_replace = cc[:-4]
			cc = cc[-4:]
			cc_len = len(cc_replace)
			print(cc_len)
			return "#" * cc_len + cc
		else:
			return cc        

cc="SF$SDfgsd2eA"
print(maskify(cc))