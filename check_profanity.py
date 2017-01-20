import urllib

def read_text():
    # here quotes is an instance of class "File".
    quotes = open("C:\PythonProjects\movie_quotes.txt")
    # here read() allows us to read the contents of the above mentioned file.
    contents_of_file = quotes.read()
    #print(contents_of_file)
    # always remember to close() the file after opening.
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    # here "urllib" module helps us get information from the internet.
    # here urlopen(link_to_a_website) helps us by making a connection with the
    # passed in website
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    # here read() is used to rad a response from the website
    output = connection.read()
    #print(output)
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("The document has no curse words")
    else:
        print("Could not scan the document properly!")
    # just like a file always remember to close a connection.
    connection.close()

read_text()
