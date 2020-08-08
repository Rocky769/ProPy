import random

print('Welcome to my Password Picker')
adjectives=['Bitter','Spicy','Sweet','Delicious','Tangy','Fruity','Salty','Tasty','Sour','Yummy','Filthy','Dry','Painful','Icy','Sticky','Smooth','Faint',
            'Quiet','Noisy','Mute','Soft','Loud','Large','Scrawny','Chubby','Small','Giant','Fat','Flat','Low','Deep','Eternal','Quick','New','Old','Odd']
nouns=['apple','banana','fruit','paper','hole','dinosaur','donkey','teacher','boy','girl','lady','man','tummy','pic','ruler','curve']
punctuations=['!','@','#','$','%','^','&','*','-','+','?','~','.',',',';',':','|']

def picker(adjectives=adjectives,nouns=nouns,punctuations=punctuations):
    repeat='y'
    while repeat.lower()=='y':
        n=int(input('How many passwords do you want ??\n'))
        adj,noun,punct,num=0,0,0,0
        for var in range(n):
            adj,noun,punct=adjectives[random.randint(0,len(adjectives)-1)],nouns[random.randint(0,len(nouns)-1)],punctuations[random.randint(0,len(punctuations)-1)]
            num=random.randint(0,99)
            print(adj+noun+punct+str(num))
        repeat=input('Want more ?? (y/n) ')
    return

if __name__ == '__main__':
    picker()
