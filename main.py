import pyrebase

firebase_config = {
    
    "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()

ab=str(1)
i = 0
all_files = storage.list_files()

for file in all_files:
    i += 1
    if i == 5:
        break
        exit()
    try:
            print(file.name)
            z=storage.child(file.name).get_url(None)
            storage.child(file.name).download("hello.jpg")
            x=int(ab)
            ab=str(x+1)
    except:
            print('Download Failed')