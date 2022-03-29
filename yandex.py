import requests

def create_folder(folder_path, token):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {'path': "disk:/vk_backup/" + folder_path}
    headers = {"Content-Type" : "application/json",
            "Authorization" : f"OAuth {token}"}
    response = requests.put(url=url, headers=headers, params=params)
    if response.status_code == 201:
        print(f"Folder {folder_path} created")
    return response.status_code