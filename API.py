
import requests
import json
def getmethod(link):
    response = requests.get(link)
    return response.status_code,response.json()

def postmethod(link,myobj,headers):
    print(myobj)
    print(type(myobj))
    x = requests.post(link, data = json.dumps(myobj), headers=headers)
    print(x)
    print(x.text)

def deletemethod(link):
    # print(myobj)
    # print(type(myobj))
    x = requests.delete(link)
    print(x)
    print(x.text)


def get_to_do_list():
    number = input("enter any random number from to do list :")
    fetch_url = 'http://jsonplaceholder.typicode.com/todos/'+number
    a,b = getmethod(fetch_url)
    print(a)
    if(a == 200):
        print(b)
    else:
        print("error in fetching data!!!!!!!!!!!!")

def update_add_to_do_list():
    # number = input("eneter id number above 100 :")
    post_url = 'https://jsonplaceholder.typicode.com/posts'#+number
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
    }


    myobj = {
        "userId": 1,
        # "id": 1,
        "title": "title test",
        "body": "foooooo"
        }
    # myobj = "{title: 'foo',body: 'bar',userId: 1}"
    postmethod(post_url,myobj,headers)

def delete_to_do_list():
    number = input("enter any delete to do list with id:")
    fetch_url = 'http://jsonplaceholder.typicode.com/todos/'+number
    deletemethod(fetch_url)
    
while True:
    print("--------------------Main Menu--------------------")
    Action_to_perform = input("Enter any option you want to perform\nG or g to get the to Do list\nA or a to add new list\nD or d to delete the list\nEnter any action:")
    if(Action_to_perform == 'G' or Action_to_perform == 'g'):
        get_to_do_list()
    elif(Action_to_perform == 'A' or Action_to_perform == 'a'):
        update_add_to_do_list()
    elif(Action_to_perform == 'D' or Action_to_perform == 'd'):
        delete_to_do_list()
        print("123")
    else:
        print("enter valid data")
    