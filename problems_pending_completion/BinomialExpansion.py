def expand(expr):
	pass

print(expand("(x+1)^2"))
print(expand("(x+1)^2"))      # returns "x^2+2x+1"
print(expand("(p-1)^3"))      # returns "p^3-3p^2+3p-1"
print(expand("(2f+4)^6"))     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
print(expand("(-2a-4)^0"))    # returns "1"
print(expand("(-12t+43)^2"))  # returns "144t^2-1032t+1849"
print(expand("(r+0)^203"))    # returns "r^203"
print(expand("(-x-1)^2"))     # returns "x^2+2x+1"