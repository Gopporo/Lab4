class String:

    def __init__(self, value):
        self._valuue = value

    def __str__(self):
        return self._valuue

    def length(self):
        return len(self._valuue)

    def substring(self, start, end):
        return self._valuue[start:end]

    def indexOf(self, substring):
        return self._valuue.find(substring)

    def  replace(self, old_substring, new_substring):
        return self._valuue.replace(old_substring, new_substring)

    def upper(self):
        return self._valuue.upper()

    def lower(self):
        return self._valuue.lower()


s = String("Hello, world!")

print(s.length())
print(s.substring(2, 5))
print(s.indexOf("world"))
print(s.replace("world", "universe"))
print(s.upper())
print(s.lower())
