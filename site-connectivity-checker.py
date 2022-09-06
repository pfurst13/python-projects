import urllib.request as urllib

def main(url):
    print("Checking the conectivity...")
    
    response = urllib.urlopen(url)
    
    if response.getcode() == 200:
        print("Connected to", url, "succesfully")
        print("Te response code was:", response.getcode())
    else:
        print("Connevtivity failed")
    

print("This is a site connectivity checker.")
input_url = input("Enter the url: ")

main(input_url)
    