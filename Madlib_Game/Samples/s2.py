def madlib():
    Boy_name = input("Boy_name: ")
    type_of_Dinosaur = input("type_of_Dinosaur: ")
    noise = input("noise: ")
    animal = input("animal: ")
    body_part = input("body_part: ")
    color = input("color: ")
    something_stinky = input("something_stinky: ")
    number = input("number: ")
    game = input("game: ")
    emotion = input("emotion: ")

    madlib = f"{Boy_name} was a mighty {type_of_Dinosaur} \
He would stomp around the jungle with a loud \
{noise}! The other dinosaurs thought he \
was good at hunting {animal} and had a \
very scary {body_part}.He lived in a \
{color} cave that smelled like {something_stinky}.\
He had {number} friends that always played \
{game} with him.He was a very \
{emotion} dinosaur!"
    print(madlib)
