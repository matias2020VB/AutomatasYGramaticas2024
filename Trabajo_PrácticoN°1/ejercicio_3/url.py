import re
url = re.compile("^(https?://)?(www\.)?([a-zA-Z0-9/.-])+[a-zA-Z0-9]\.(com|ar|net|org|edu\.ar|edu\.com|edu\.org)+([/a-zA-Z0-9/])*$")
url_op2 = re.compile("^(www\.)?([a-zA-Z0-9/.-])+[a-zA-Z0-9]\.(com|es|ar|net|org|um\.edu\.ar|edu\.ar|edu\.com|edu\.org|cl|co|cn|ae|au|br|ca|nz)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es)+([/a-zA-Z0-9/])*$")
url_op3 = re.compile("^([a-zA-Z0-9/.-])+[a-zA-Z0-9]\.(com|es|co|ar|net|org|um|edu)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es|edu)+\.(ar|cl|co|cn|ae|au|br|ca|nz|es|edu)+([/a-zA-Z0-9/])*$")

print("VALIDACION DE URL, PUNTO B")
agregarurl = [input("INGRESE LA URL: " u'')]

for pagina in agregarurl:
    match_one = url.search(pagina)
    match_two = url_op2.search(pagina)
    match_tree = url_op3.search(pagina)
    if match_one or match_two or match_tree:
        print('{:<30}  {}'.format(pagina, 'URL INGRESADA CORRECTAMENTE'))
    else: 
        print('{:<30}  {}'.format(pagina, 'URL INVALIDA'))