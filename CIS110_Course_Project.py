#introduction greeeting
print('Hello, welcome to the interactice Super Serious Story of Current Affairs Q1 2023')
print('To get started I\'ll ask you several questions.')
print('Simply type your response and press enter')
print('Let us begin....')
input('Come on, press enter to begin.')

#questions for story customization (mad lib components)
name = input('What is your name? :  ')
while len(name) < 1:
    name = input('What is your name? :  ')
vp = input('Who is your favorite cartoon character?:  ')
while len(vp) < 1:
    vp = input('Who is your favorite cartoon character?:  ')
gender = input('Do you identify as male, female, or other?:  ')
while gender.lower() not in ('male', 'female', 'other'):
    gender = input('Do you identify as male, female, or other?:  ')
num = input('What day of the month were you born?: ')
while not num.isdigit():
    num = input('What day of the month were you born?:  ')
upOrDown = input('Up or down?:  ')
while upOrDown.lower() not in ('up', 'down'):
    upOrDown = input('Up or down?:  ')