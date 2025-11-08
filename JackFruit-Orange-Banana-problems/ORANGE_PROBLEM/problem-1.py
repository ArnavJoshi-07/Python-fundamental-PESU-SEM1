def create_address_book(names_txt_file: str, phone_txt_file: str):
    ''' Creates address book'''
    contacts_dict = {}
    with (open(names_txt_file,'r') as f1, ## file with names
        open(phone_txt_file,'r') as f2):  ## file with phone numbers

        names = [line.strip() for line in f1.readlines()]
        phones = [line.strip() for line in f2.readlines()]

        for i in range(len(names)):
            name = names[i]
            phone = phones[i]
            contacts_dict[name] = phone
        # print("Contacts Dictionary:",contacts_dict)

    return contacts_dict
# print(contacts_dict)


def filter_dict(contacts_dict: dict) -> dict: 
    '''Check if name starts with vowel'''
    starting_vowels = "AEIOU"
    filtered_dict = {key:values for (key,values) in contacts_dict.items() if (key.upper()[0] in starting_vowels)} 

    return filtered_dict

def reverse_encrypt_phno(filtered_dict: dict) -> dict:
    ''' Reverse and encrypt'''
    reversed_phno = {key:values[::-1] for (key, values) in filtered_dict.items()}
    # encrypt_phno = {key:"*"*8+values[-2:] for (key, values) in reversed_phno.items()}
    encrypt_phno = {key:values[-2:].rjust(10,'*') for (key, values) in reversed_phno.items()}
    return encrypt_phno


def sort_contacts_dict(encypted_phno: dict, contacts_sec_file):
    sorted_contacts_dict = dict(sorted(encypted_phno.items())) # sorted dict

    with open(contacts_sec_file,'w') as f:
        for (k,v) in sorted_contacts_dict.items():
            f.write(k + ' : '+ v + "\n")
    return sorted_contacts_dict
    
def vowel_count(sorted_contact_dict:dict)-> dict:
    vowels='AEIOU'
    count_dict = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    for k in sorted_contact_dict.keys():
        if k.upper()[0] in vowels:
            count_dict[k.upper()[0]] += 1
    print(count_dict)


### Function calls : 

contacts_dict = create_address_book("JackFruit-Orange-Banana-problems\\ORANGE PROBLEM\\names.txt",
                    "JackFruit-Orange-Banana-problems\\ORANGE PROBLEM\\phones.txt")

filtered_dict = filter_dict(contacts_dict)
encypted_phno = reverse_encrypt_phno(filtered_dict)
sorted_contact_dict = sort_contacts_dict(encypted_phno, "secure_contacts.txt")
vowel_count(sorted_contact_dict)


# print(reversed_phno)


