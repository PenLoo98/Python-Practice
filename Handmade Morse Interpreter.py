#  Q16
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z', '':' '
}

a = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
b = a.split(' ')
c = []
for i in b:
    c += dic[i]
d = ''.join(c)
print(d)