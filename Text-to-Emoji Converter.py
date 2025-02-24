#Text-to-Emoji Converter
#We can hardcode a dictionary mapping words to emojis which is the method I am going to use but also the inbuilt library of windows too maybe but I am not sure how to
d={"love":"❤️","happy":'😊',"pizza":'🍕',"ok":'👍',"nice":'👌'}
n=input()
l=n.split(" ")
for i in range(len(l)):
    if l[i].lower() in d:
        l[i]=d[l[i].lower()]
x=''
for i in l:
    x=x+i+' '
print(x)