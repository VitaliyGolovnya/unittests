documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def document_numbers(doc_list=directories):
    doc_nums = []
    for documents in doc_list.values():
        for document in documents:
            doc_nums.append(document)
    return doc_nums


def person_id(doc_num: str, documents_list=documents):
    print("Following documents are currently on shelves: ")
    print()
    doc_nums = document_numbers()
    print("\n".join(doc_nums))
    print()
    for document in documents_list:
        if doc_num == document["number"]:
            return document["name"]
    return "There is no such document number."


def shelf_id(doc_num: str, shelves_list=directories):
    print("Following documents are currently on shelves: ")
    print()
    doc_nums = document_numbers()
    print("\n".join(doc_nums))
    print()
    for shelf in shelves_list:
        if doc_num in shelves_list[shelf]:
            return f"The document in on shelf No.{shelf}."
    return "There is no such document number."


def full_list(documents_list=documents):
    for document in documents_list:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
    return documents_list


def new_document(shelf: str, doc_type: str, doc_no: str, doc_name: str):
    document = {}
    document["type"] = doc_type
    document["number"] = doc_no
    document["name"] = doc_name
    documents.append(document)
    shelves = ", ".join(list(directories.keys()))
    print(f"Available shelves are: {shelves}")
    while True:
        if shelf in directories.keys():
            print("Success")
            directories[shelf].append(document["number"])
            break
        elif shelf == "q":
            break
        else:
            print("There is no such shelf. Try again or quit by pressing \"q\"")
            continue
    return document


def delete_document(remove_doc: str):
    print("Following documents are currently on shelves: ")
    print()
    doc_nums = document_numbers()
    print("\n".join(doc_nums))
    print()
    while True:
        if remove_doc in doc_nums:
            for documents in directories.values():
                if remove_doc in documents:
                    documents.remove(remove_doc)
                    print("Document has been successfully deleted")
            break
        elif remove_doc == "q":
            break
        else:
            print("There is no such document")
            break
    return None

def move_document(move_doc: str, shelf: str):
    print("Following documents are currently on shelves: ")
    print()
    doc_nums = document_numbers()
    print("\n".join(doc_nums))
    print()
    while True:
        if move_doc in doc_nums:
            for documents in directories.values():
                if move_doc in documents:
                    shelves = ", ".join(list(directories.keys()))
                    print(f"Available shelves are: {shelves}")
                    while True:
                        if shelf in directories.keys():
                            print("Success")
                            documents.remove(move_doc)
                            directories[shelf].append(move_doc)
                            return None
                        elif shelf == "q":
                            break
                        else:
                            print("There is no such shelf")
                            return None
            break
        elif move_doc == "q":
            return None
        else:
            print("There is no such document")
            return None


def new_shelf(shelf: str):
    if shelf not in directories.keys():
        directories[shelf] = list()
        print("Success")
        return False
    else:
        print("Shelf already exists")
        return True

