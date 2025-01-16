#dictionary methods
my_info={
    "name":"Neeraj Verma",
    "age": 32,
    "address": ["962/16","jurkovicova","haje","prague",14900],
    "personal_id": (9538365668,"neeraj502@gmail.com"),
    12:15,
    "wife_info": {
    "name":"Sunita Verma",
    "age": 29,
    "address": ["962/16","jurkovicova","haje","prague",14900],
    "personal_id": (971198442,"neeraj502@gmail.com")

    }
}

# print(my_info.keys())
# print(my_info.values())
# print(my_info.items())
print(my_info.get("age"))
my_info.update({"height":456})
print(my_info.items())