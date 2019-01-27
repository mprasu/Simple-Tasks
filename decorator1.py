def first(func):
    def second():
        print("i am in second ")
        func()
    return second
@first
def third():
    print("i am in third")
#third()



