# def online_count(statuses):
#     npo = 0
#     for x, y in statuses.items():
#         if y == "online":
#             npo += 1;
#     return npo

# print(online_count({"Alice": "online", 
#               "Bob": "offline", 
#               "Eve": "online"}))

# long version
# def online_count(people):
#     count = 0
#     for person, status in people.items():
#         if status == "online":
#             count += 1
#     return count

# # short version
def online_count(people):
    return len([p for p in people if people[p] == "online"])

print(online_count({"Alice": "online", 
              "Bob": "offline", 
              "Eve": "online"}))