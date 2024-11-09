# Define
def main():
    convert(input("Enter Text - " ))

def convert(faces):
    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")
    print(faces)

# Input
main()