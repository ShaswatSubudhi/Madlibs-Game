def rep(data):
    words=["adjective","animal","verb","place","object","creature","exclamation","verd_past_tense","person","name","thing","color"]
    mod_data=data
    for word in words:
        if word in data:
            w=input( f"Enter a {word}: ")
            mod_data=mod_data.replace(word,w)
    return mod_data
def main():
    mo_data=[]

    print("Madlibs Game")
    print("1. The Great Escape\n2. The Mysterious Treasure\n3. A Day at the Park")
    choice=input("Enter which story you want to play Madlibs with: ")
    if choice=="1":
        file="MadlibsGame\\The Great Escape.txt"
    elif choice=="2":
        file="MadlibsGame\\The Mysterious Treasure.txt"
    elif choice=="3":
        file="MadlibsGame\\A Day at the Park.txt"
    else:
        print("Invalid choice")
        return
    
    with open(file, "r") as f:
        data = f.readline()
        while data:
            mo_data.append(rep(data))
            data = f.readline()
    
    with open("MadlibsGame\\Conclusion.txt", "w+") as f:
        for line in mo_data:
            f.write(line)
        f.seek(0)
        print("==============================================================")
        print(f.read())
        print("==============================================================")
main()