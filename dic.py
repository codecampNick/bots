proj = []
projects = {}
print(type(proj))
print(type(projects))

projects['a'] = [('Outbound Feed','Used c sharp and sql to integrate with a SOAP webservice')]
projects['a'].append(('Inbound Feed','did some stuff'))
print(len(projects['a']))
print(projects['a'][1][0])

one = 'three'
two = 'four'
five = 'seven'
six = 'eight'
nine = 'ten'

projects['a'].append((one,two))
projects['a'].append((five,six,nine))

a = (one,two)
print(type(a))
print(a[0])
print(a[1])

print(len(projects['a']))

print(projects['a'][3][2])


