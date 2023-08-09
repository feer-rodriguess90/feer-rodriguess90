return_code = 200
match return_code:
    case NOT_FOUND:
        print("return code not found")

print(f"{NOT_FOUND = }")