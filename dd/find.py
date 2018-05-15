result = []


def find_all(str_test1, query_content, index=0):
    find_index = str_test1.find(query_content, index)
    if find_index >= 0:
        result.append(find_index)
        find_all(str_test1, query_content, (find_index + len(query_content)))
    else:
        return result
    return result


str_test = "faijfkljflajfjfa"
# str_test = "fa"
result1 = find_all(str_test, "f")
print(result1)
