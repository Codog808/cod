import os

def main():
    packages_to_add_to_path = [d for d in os.listdir() if os.path.isdir(d)]
    packages_count = len(packages_to_add_to_path)
    po = []
    for p in packages_to_add_to_path:
        if not "." in p:
            po.append(p)
    packages_to_add_to_path = po

    for package in po:
        directories_in_package = [d for d in os.listdir(package) if os.path.isdir(os.path.join(package, d))]
        if "bin" in directories_in_package:
            # print(package + "bin")
            absolute_path = os.path.abspath(f"{package}/bin")
            print(absolute_path) 


    # for package in packages_to_add_to_path:
    #    print(package)
    # print("Sucess")
    return True

if __name__ == '__main__':
    main()
