import random

cuisine_list = ["Italian","Mexican","Burgers","Fancy","Tacos","Vegetarian","BBQ","Mediterranean","South Asian","East Asian","Dessert","Brunch"]

italian_list = ["Coltivare in The Heights","Paulie's in Montrose","D'Amico's in Rice Village","Luigi's Pizza in 3rd Ward","Romano's Pizza in Montrose","Grazia Italian Kitchen in Pearland","Gino's East in Spring; call ahead","Mandola's Deli in EaDo","Enoteca Rossa in Bellaire","Frank's Pizza in Downtown"]
mexican_list = ["Ninfa's on Navigation in East Side","El Real Tex-Mex in Montrose","Teotihuacan in The Heights","Xochi in Downtown","Anejo in Galleria","Cyclone Anaya's in Woodlands/Heights","Abuelo's in Katy","fajita's A Go Go in Rice Village","Saltillo in Bellaire","Pico's in Upper Kirby"]
burgers_list = ["Hopdoddy in Rice Village","Hubcap Grill in The Heights","Bernie's Burger Bus in Bellaire","Bubba's Burger Shack under 59 South/610","Buffburger in Montrose","Shake Shack in Galleria","Sam's Burgers in Memorial","Rodeo Goat in EaDo","Lankford Grocery in Midtown; cash only","BurgerChan in Greenway"]
fancy_list = ["B&B Butchers in Wash. Ave","Brennan's in Midtown","Jasper's in The Woodlands","Uchi in Montrose","Steak 48 in the Galleria","Vic and Anthony's in Downtown","Cureight in the Woodlands","Peli Peli in Katy/Galleria","Avenida Brazil in League City","Antica Osteria in Rice Village"]
tacos_list = ["Tierra Caliente next to West Alabama Ice House","Tacos A Go Go in Mid-Main","Libery Taco in Galleria","Torchy's in Rice Village/Heights","Eight Row Flint in The Heights","Tacodeli in Wash Ave","Velvet Taco in Rice Military","Brothers Taco House in EaDo","Tacos Mayra near Alief","What A Taco in Montrose"]
vegetarian_list = ["Green Vegetarian in Bellaire","Wisdom's Cafe in The Woodlands","Green Seed Vegan in 3rd Ward","Flower Child in Galleria","Mellow Mushroom Pizza in The Heights","Baba Yega in Montrose","Local Foods in Downtown","The Traveling Carrot in Katy","Pepper Tree in Greenway","Southern Style Vegan in Southside"      ]
bbq_list = ["Killen's in Pearland","The Pit Room in South Midtown","Gatlin's in Independence Heights","Tejas Chocolate BBQ in Tomball","Corkscrew BBQ in Spring","Pinkerton's in The Heights","Truth BBQ in Wash. Ave","Burns BBQ near Acres Homes","Brett's Barbecue in Katy","Tin Roof BBQ in Atascocita"]
mediterranean_list = ["Niko Niko's in Montrose","Fadi's in Bellaire","Aladdin in Montrose","Mary'z in Rice Military","Istanbul Grill in Rice Village","Shawarma Stop near Hermann Park", "Zoe's Kitchen in The Heights", "Dimasi's in Katy","Zara's Kitchen in The Woodlands","Mazaj in The Galleria"]
southasian_list = ["Simply Pho in Midtown","Khyber in Upper Kirby","Thai Spice in The Heights","Huynh in EaDo","Thai Cottage in Bellaire","Mai's in Midtown","Bombay Pizza Co. in Downtown","Aga's Restaurant in Missouri City","Pondecheri in Upper Kirby","Crawfish and Noodles in Chinatown"]
#indian, thai,vietnamese
eastasian_list = ["Osaka in Montrose","Oishii in Greenway","China Garden near EaDo","Uni Sushi in The Woodlands","Spicy Girl in Midtown","Qin Dynasty in Upper Kirby","Blackbird Izakaya in The Heights","Yoshi in Bellaire","Kura Revolving Sushi in Mid-Main","Atami in Katy"]
#chinese, japanese, sushi
Dessert_list = ["Amy's Ice Cream on Shepherd","Chocolate Bar in Rice Village","House of Pies near Galleria","Tout Suite in EaDo","Sprinkles Cupcake ATM in Highland Village","Chill Milkshake Bar in The Woodlands","Stacked Ice Cream in Katy","Milk+Sugar in Montrose","Michael's Cookie Jar in Downtown","Fat Cat Creamery in The Heights"]
Brunch_List = ["Eloise Nichols in Uptown","Benjy's in Rice Village","Whiskey Cake in League City","Barnaby's Cafe in Montrose","Snooze Eatery in Katy and The Heights","District 7 Grill in EaDo","True Food Kitchen in The Woodlands","A'Bouzy in Upper Kirby","Lucille's near Hermann Park","The Union Kitchen on Bellaire Blvd"]

answer = "Yes" #input("So you wanna go out to eat?")

if answer == "Yes":
    print("Type one cuisine from this list, and I'll pick a random restaurant of that cuisine!")
    print(" ")
    print(cuisine_list)
    print(" ")
    NextQuestion = input("So what kind of food are you thinking of?")
#    print (NextQuestion)
elif answer == "yes":
    print("Type one cuisine from this list, and I'll pick a random restaurant of that cuisine!")
    print(" ")
    print(cuisine_list)
    print(" ")
    NextQuestion = input("So what kind of food are you thinking of?")
#    print (NextQuestion)
else:
    print("Then learn to cook!")

if NextQuestion == "Italian":
    Response = random.choice(italian_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(italian_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(italian_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Mexican":
    Response = random.choice(mexican_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(mexican_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(mexican_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Burgers":
    Response = random.choice(burgers_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(burgers_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(burgers_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Fancy":
    Response = random.choice(fancy_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(fancy_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(fancy_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Tacos":
    Response = random.choice(tacos_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(tacos_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(tacos_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Vegetarian":
    Response = random.choice(vegetarian_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(vegetarian_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(vegetarian_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "BBQ":
    Response = random.choice(bbq_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(bbq_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(bbq_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Mediterranean":
    Response = random.choice(mediterranean_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(mediterranean_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(mediterranean_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "South Asian":
    Response = random.choice(southasian_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(southasian_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(southasian_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "East Asian":
    Response = random.choice(eastasian_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(eastasian_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(eastasian_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Dessert":
    Response = random.choice(dessert_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(dessert_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(dessert_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
elif NextQuestion == "Brunch":
    Response = random.choice(brunch_list)
    Reply = input("Does "+Response+" work?")
    if Reply == "No":
        Response2 = random.choice(brunch_list)
        Reply2 = input("Does "+Response2+" work?")
        if Reply2 == "No":
            Response3 = random.choice(brunch_list)
            Reply3 = input("Does "+Response3+" work?")
            if Reply3 == "No":
                print("Ugh. I give up!")
            else:
                print("Found your next dinner!")
        else:
            print("Found your next dinner!")
    else:
        print("Found your next dinner!")
else:
    print("You done goofed! Restart, and pick something from the list!")


#print(foodtype)



