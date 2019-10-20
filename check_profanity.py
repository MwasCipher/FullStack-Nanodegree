import urllib3
def read_text():
    document = open("/home/mufasa/Desktop/testDocument")
    file_contents = document.read()
    print(file_contents)
    document.close()
    check_profanity(file_contents)

def check_profanity(text_to_check):
    connection = urllib3.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("Profane Word Found!!!!")

    elif "false" in output:
        print("No Curse Word Found")

    else:
        print("Could Not Scan Document Properly")


read_text()