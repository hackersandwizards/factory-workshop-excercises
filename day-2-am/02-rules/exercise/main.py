# Simple sample file — used to test that the pirate rule does NOT activate
# when working on .py files (glob: "**/*.md" only).
#
# Bonus: if you build the Python stretch rule, this file has a few intentional
# anti-patterns to flag (mutable default arg, == None, range(len(...)) loop,
# bare except, no type hints).


class Greeter:
    def __init__(self, name, tags=[]):   # mutable default argument
        self.name = name
        self.tags = tags

    def greet(self):
        print("Hello, " + self.name + "!")   # string concat instead of f-string


def main():
    g = Greeter("world")
    g.greet()

    mode = None
    if mode == None:                     # == None instead of `is None`
        print("no mode set")

    nums = [1, 2, 3, 4, 5]
    for i in range(len(nums)):           # range(len(...)) instead of iterating directly
        print(nums[i], end=" ")
    print()

    try:
        result = 10 / 0
    except:                              # bare except
        print("something went wrong")


if __name__ == "__main__":
    main()
