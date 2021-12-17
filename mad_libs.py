from tkinter import *

window = Tk()
window.geometry('300x300')
window.title('Mad Libs Generator')
Label(window, text='Mad Libs Generator \n Have Fun', font='arial 30').pack()
Label(window, text='click any one..', font='arial 20 italic').place(x=40, y=80)

# define_functions


def madlib1():
    animal = input('Enter a animal name: ')
    profession = input('Enter a Profession name: ')
    cloths = input('Enter a piece of cloths name: ')
    things = input('Enter a thing name: ')
    name = input('Enter a name of buy or girl: ')
    place = input('Enter a name of a place: ')
    verb = input('input a verb: ')
    food = input('Enter a food name: ')
    print(f'say {food}, the photographer said as the camera flashed! {name} and I had gone to {place} to go/'
          f'our photos token on my {animal}s.Pretending to be a {profession}.when we saw the second photo,it was/'
          f'exactly what I wanted.we both look like {things}s wearing {cloths} and {verb}. --exactly what I had/'
          ' in my mind')


def madlib2():
    adjective = input('Enter an adjective: ')
    color = input('Enter a color name: ')
    thing = input('Enter a thing name: ')
    place = input('Enter a place name: ')
    person = input('Enter a person name: ')
    adjective1 = input('Enter an adjective: ')
    insect = input('Enter an insect name: ')
    food = input('Enter a food name: ')
    verb = input('Enter a verb: ')
    print(f'Last night I dreamed I was a {adjective} butterfly with {color} splocthes that I looked like/'
          f'{thing}.I flew to {place} with my bestfriend and {person} who was a {adjective1} insect. /'
          f'We ate some {food} when we got there and then decided to {verb} and the dream ended when I said/'
          f'--lets {verb}.')


def madlib3():
    person = input('Enter a person name: ')
    color = input('Enter a color name: ')
    foods = input('Enter a food name: ')
    adjective = input('Enter an adjective: ')
    thing = input('Enter a thing name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb: ')
    adverb = input('Enter an adverb: ')
    food = input('Enter a food name: ')
    things = input('Enter a thing name: ')

    print(f"Today we picked apple from {person}'s orchard.I had no idea there were so many different varieties/"
          f"of apples.I ate {color} apples straight off the tree that tasted like {foods}.then there was a /"
          f"{adjective} apple that looked like a {thing}.when our bag were full we went on a free hay ride to/"
          f" {place} and back.it ended at a hay pile were we got to {verb} {adverb}.I can hardly wait to get/"
          f"home and cook with the apples.We are going to make apple {food} and {things} pies!.")


Button(window, text='Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
Button(window, text='Apple and Apple', font='arial 15', command=madlib2, bg='ghost white').place(x=60, y=180)
Button(window, text='the Butterfly', font='arial 15', command=madlib3, bg='ghost white').place(x=60, y=240)

window.mainloop()
