run = ''
while run != 'no':
    #introduction greeeting
    print('Hello, welcome to the interactive Super Serious Story of Current Affairs Q1 2023')
    print('To get started I\'ll ask you several questions.')
    print('Simply type your response and press enter')
    print('Let us begin....')
    input('\nCome on, press enter to begin.')

    #questions for story customization (mad lib components)
    name = input('\nWhat is your name? :  ')
    while len(name) < 1:
        name = input('What is your name? :  ')
    vp = input('Who is your favorite cartoon character?:  ')
    while len(vp) < 1:
        vp = input('Who is your favorite cartoon character?:  ')
    gender = input('Do you identify as male, female, or other?:  ').lower()
    while gender not in ('male', 'female', 'other'):
        gender = input('Do you identify as male, female, or other?:  ')
    num = input('What day of the month were you born?: ')
    while not num.isdigit():
        num = input('What day of the month were you born?:  ')
    upOrDown = input('Up or down?:  ').lower()
    while upOrDown not in ('up', 'down'):
        upOrDown = input('Up or down?:  ')

    #other variables based on qustions for story customization 
    prefix = 'Mr.'
    if gender == 'female':
        prefix = 'Ms.'
    if gender == 'other':
        prefix = 'Mx.'
    underOverPar = 'over' if upOrDown == 'up' else 'under'
    increaseOrDecrease = 'increase' if upOrDown == 'up' else 'decrease'
    opposite = 'decrease' if upOrDown == 'up' else 'increase'

    #beginning of story
    print('\nYou are the president of the United States')
    print('It is the year 2023, some time in February.')
    print('From every corner of the globe, the world is at peace and the economy is better than it\'s ever been.')
    print(f'You and vice president {vp} are at the White House contemplating countless global issues.')
    print(f'You both get bored and agree you might need a break.')
    print(f'Vice president {vp} asks if you want to go play 18 holes of golf.')

    #decision 1
    golfOrNot = input(f'\nWill you play golf with {vp} (yes) or continue your presidential duty (no)?  Type yes or no:  ').lower()
    while golfOrNot not in ('yes', 'no'):
        golfOrNot = input('Will you play golf with {vp} (yes) or continue your presidential duty (no)?  Type yes or no:  ').lower()
    if golfOrNot == 'yes':
        print(f'''\n
        You and VP {vp} fly in your private helicopters to the Pohick Bay golf course, and you end
        up playing the best 18-hole game of your life: {num} {underOverPar} par, but you draw 
        heavy criticism on the news for playing golf without wearing a mask.''')
    else:
        print(f'''\n
        Instead of playing golf, you continue contemplating global issues and decide the best course 
        of action is to blow up an undersea gas pipeline to save the environment. It turns out; subsequently,
        you also make a bunch of money.''')

    cont = input('\npress enter to continue...')
    # decision 2
    print(f'\nYou get a phone call: “{prefix} president, there is a gigantic super-secret spooky spy balloon floating over the country! What are your orders {prefix} president?”')
    shootOrNot = input('\nWill you order it to be shot down? Type yes or no:  ').lower()
    while shootOrNot not in ('yes', 'no'):
        shootOrNot = input('Will you order it to be shot down? Type yes or no:  ').lower()
    if shootOrNot == 'yes':
        print('''\n
        The military carries out your orders and shoots down the gigantic super-secret spooky spy balloon 
        with a high-explosive missile so that they can have a much easier time recovering pieces of 
        wreckage from the ocean floor for the intelligence, of course.''')
    else:
        print('''\n
        The gigantic super-secret spooky spy balloon continues its precisely charted course and finally 
        makes it to its destination, where it just hovers mysteriously for no apparent reason.''')

    cont = input('\npress enter to continue...')
    #ending 1
    if golfOrNot == 'yes' and shootOrNot == 'yes':
        print(f'''\n
        While focusing all of your attention on the gigantic super-secret spooky spy balloon and your golf game,
        some aliens arrive in their weird car-sized octagonal-shaped spacecraft and warn you that your planet 
        will only last for another {num} years if you maintain your current course. They say your only hope is 
        to {increaseOrDecrease} your budget for military spending and {opposite} your budget for social security 
        and education.''')
    #ending 2
    elif golfOrNot == 'no' and shootOrNot == 'no':
        print(f'''\n
        While hovering over Scotland, the gigantic super-secret spooky spy balloon successfully summons a creature 
        of the deep. While a bunch of elites are meeting in Davos, someone knocks on the door. Will Bates opens the 
        door and says: “what do you want?” and receives the answer, “Tree Fiddy.” It was then that he realized it 
        was an eight-story tall creature from the Mesozoic era. Bates says: “Oh, okay, no problem, I'm uber-rich; 
        anything else?” The Loch Ness Monster Responds: “Oh, yeah, and can you tell president {name} that they owe 
        me {num} million for stinking up the water? Sheesh.” You then pay all your newly made profits to the 
        Loch Ness Monster and decide you should retire and just play more golf.''')
    #ending 3
    else:
        print(f'''\n
        While a bunch of elites are meeting in Davos, someone knocks on the door. Will Bates opens the door and says: 
        “what do you want?” and receives the answer, “Tree Fiddy.” It was then that he realized it was an eight-story
        tall creature from the Mesozoic era. Bates says: “Oh, okay, no problem I'm uber-rich; anything else?” 
        The Loch Ness Monster Responds: “Oh, yeah, can you tell president {name} they need to come to clean their 
        garbage out of our water? My wife cut her tail the other day, and she is not happy! Happy she happy sea, 
        am I right?” Will bates slams the door.''')
    run = input('\nWould you you like to run it agian? yes or no:  ').lower()
    while run != 'yes' and run != 'no':
        run = input('Must type yes or no:  ')