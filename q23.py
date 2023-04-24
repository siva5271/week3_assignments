def sum(*values):
    result=0;
    for x in values:
        result=result+x
    return result

print(sum(1.1, 2.2, 5.5))