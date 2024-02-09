n = int(input())
phone_book = {}
for _ in range(n):
    name_and_phone = input().split()
    name = name_and_phone[0]
    phone_number = name_and_phone[1]
    phone_book[name] = phone_number

while True:
    try: 
        query_name = input()
        if query_name in phone_book:
            print(f"{query_name}={phone_book[query_name]}")
        else:
            print("Not found")
    except EOFError:
        break
    