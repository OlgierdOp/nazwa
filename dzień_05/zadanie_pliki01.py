with open("email.txt", 'r') as f:
    result = ''
    result1 = ''
    for line in f:
        if line.count('@') == 1:
            result= result + line
            
with open("cleaned_email.txt", 'w') as f:
    f.write(result)