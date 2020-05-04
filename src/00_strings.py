# Print "Hello, world!" to your terminal
s = "Hello World!"
print(s)

print("uppercase", s.upper())
print("lowercase", s.lower())
print("swap", s.swapcase())
print("length", len(s))
print("replace", s.replace("World", "everyone"))
print("count", s.count("l"))
print("starts with", s.startswith("Hello"))
print("ends with", s.endswith("rld!"))
print("split", s.split())
print("find index", s.find("r"))
print("is alphanumeric", s.isalnum())
print("is alphabetic", s.isalpha())  # no spaces and no punctuation
n = "10"
print("is numeric", n.isnumeric())
