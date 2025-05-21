## Looping Through An Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


## Doing More Work Withi A For Loop

magicians = ['alice','david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


## Doing Someting After A For Loop

magicians = ['alice','david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")


## Avoiding Identation Errors

magicians = ['alice', 'david','carolina']
for magician in magicians:
    print(magician)


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")



## Indenting Unnecessarily After the loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")