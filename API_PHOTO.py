import requests  # to get image from the web
import shutil  # to save it locally

x = 0


def get_info():
    global response
    response = requests.get("https://api.thedogapi.com/v1/images/search")
    name = response.json()[x]['breeds'][0]["name"]
    weight_imperial = response.json()[x]['breeds'][0]["weight"]["imperial"]
    weight_metric = response.json()[x]['breeds'][0]["weight"]["metric"]
    height_imperial = response.json()[x]['breeds'][0]["height"]["imperial"]
    height_metric = response.json()[x]['breeds'][0]["height"]["metric"]
    bred_for = response.json()[x]['breeds'][0]["bred_for"]
    breed_group = response.json()[x]['breeds'][0]["breed_group"]
    life_span = response.json()[x]['breeds'][0]["life_span"]
    temperament = response.json()[x]['breeds'][0]["temperament"]



    if response.status_code != 200:
        print("Whoops! Connection Error!")
    else:
        print("Welcome to our breeds of dog's collection! ")
        print(f"This Dog's name is {name}")
        print(f"Its imperial weight is {weight_imperial}")
        print(f"Its metric weight is {weight_metric}")
        print(f"Its imperial height is {height_imperial}")
        print(f"Its metric height is {height_metric}")
        print(f"Its breed is for {bred_for}")
        print(f"Its breed Group is  {breed_group}")
        print(f"Its life span is  {life_span}")
        print(f"And finally its temperament is {temperament}")


def image_download():

    image_url = response.json()[x]["url"]
    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream=True)

    question = str(input("Do u want to download image of this dog? type yes/no : "))
    if question.lower() == "yes":
        if r.status_code == 200:
            r.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')
    elif question.lower() == "no":
        pass
    else:
        print("Please type yes or no correctly!")
        image_download()

def tryGetImage():
    try:
        image_download()
    except:
        print("There is problem in downloading image!")
    finally:
        print("Good job!")

def tryGetInfo():
    try:
        get_info()
        problem = "No problem!"
    except:
        problem = "There is problem in retrieving information!"
        print(problem)
    finally:
        if problem == "There is problem in retrieving information!":
            pass
        else:
            tryGetImage()


tryGetInfo()


