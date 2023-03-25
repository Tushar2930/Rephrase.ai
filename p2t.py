import convertapi

convertapi.api_secret = 'vb2hublcjS14TSpt'

result = convertapi.convert('pdf', {'File': '1.pdf'})

# save to file
print(result.file.url)
result.file.save('1.txt')
