"""
color=['red', 'orange', 'yellow', 'green','blue','viole']
flower={"red":"Rose","orange":"Poppise","yellow":"Sunflower","green":"arass","blue":"Bluebells","viole":"violets"}
n=input().strip().lower()#.lower可以不加
if n in color:
    flower_=flower[n]
    print("{}({})".format(flower_,n))
else:
    print("I don't konw about the color {}.".format(n))
"""

"""color=['red','orange','yellow','green','blue','viole']
flower={"red":"Rose","orange":"Poppise","yellow":"Sunflower","green":"arass"
        ,"blue":"Bluebells","violet":"violes"}
n=input()
if n in color:
    flower_=flower[n]
    print(f'{flower_}({n})')
else:
    print(f'I don\'t konw about the color {n}.')"""

color=['red','orange','yellow','green','blue','viole']
flower={"red":"Rose","qrange":"Poppise","yellow":"Sunflower",
        "green":"arass","viole":"violets","blue":"BlueBells"}
n=input()
if n in color:
    flower_=flower[n]
    print(f'{flower_}({n})')
else:
    print(f'I don\'t konw about the color {n}.')



