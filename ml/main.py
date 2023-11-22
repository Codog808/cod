

def main():
    node = 1
    for i in range(0,40):
        try:
            if int(str(i)[-2]) % 2  == 0:
                print(i)
            elif int(str(i)[-2]) % 2 == 1:
                print(i, "odd")
            else:
                print(i, "no i[1]")
        except:
            print(i, "nnn")
    print("sucess")

if __name__ == "__main__":
    main()
