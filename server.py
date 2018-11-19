import sys

import time



def read_data():

    server = open("users.txt", "a+")

    organization = open("organizations.txt", "a+")

    server_data = server.read()

    organization_data = organization.read()

    server.close()

    organization.close()

    server_data = str(server_data)

    organization_data = str(organization_data)

    server_data  = server_data.split('\n')

    organization_data = organization_data.split('\n')

    User_length = len(server_data)

    Organization_length = len(organization_data)

    ###########################

    names = []

    passwords = []

    for x in range(0,User_length):

        name, password = server_data[x].split()

        names.append(name)

        passwords.append(password)

    ############################

    organization_names = []

    domains = []

    IP = []

    Minutes =[]

    for x in range(0, Organization_length):

        if organization_data[x] != '':

            name, domain ,Ip , minute = organization_data[x].split('\t')

            organization_names.append(name)

            domains.append(domain)

            IP.append(Ip)

            Minutes.append(int(minute))

###########################################
    return names, passwords, organization_names, domains, IP , Minutes

def opt2(minutes):

############## Max ################

    max = 0

    min = 0

    mean = 0

    for maximum in minutes:

        if max < maximum:

            max = maximum

            min = max

    ################################

    for minimum in minutes:

        if min > minimum:

            min = minimum

    ################################


    for num in minutes:

        mean = mean + num

        mean = float(mean)

    mean = mean / len(minutes)


    return max , min , mean

def opt3(Organizations,Domains,IP_address,Minutes):

    option = raw_input("Press 1 to sort by Organzination name in ascending order or Press 2 to sort by Minutes "
                       "in Descending order \n")

    try :

        option = int(option)

        if option == 1:

            Organizations, Domains, IP_address, Minutes = zip(*sorted(zip(Organizations, Domains, IP_address, Minutes)))

        elif option == 2:

            Minutes, IP_address, Domains, Organizations = zip(
            *sorted(zip(Minutes, IP_address, Domains, Organizations), reverse=True))

        return Organizations, Domains, IP_address, Minutes

    except:

        sys.exit("Wrong Input ")

def opt4(Organizations,Domains,IP_address,Minutes):

    tries = 0

    tried = False

    data_entered = False

    while tries < 3 and data_entered == False:

        tried = False

        organization = raw_input("Enter organization name \n")

        tries = tries + 1

        print ('\n')

        domain = raw_input("Enter domain (www.example.com) \n")

        print ('\n')

        ip = raw_input("Enter IP of organization \n")

        print ('\n')

        minute = raw_input("Enter minutes \n")

        minute = int(minute)

        print ('\n')


        ######## organization check #####

        for organization_name in Organizations:

            organization_name = str(organization_name)

            if organization.upper() == organization_name.upper():

                print ("Organization is already in the server. \n ")

                tried = True

                break

        if tried == False:

            Organizations.append(str(organization))

            Domains.append(str(domain))

            IP_address.append(str(ip))

            Minutes.append(str(minute))

            data_entered = True

    return Organizations,Domains,IP_address,Minutes

def opt5(Organizations,Domains,IP_address,Minutes):

    tries = 0

    tried = False

    data_del = False

    while tries < 3 and data_del == False:

        tried = False

        organization = raw_input("Enter organization name \n")

        tries = tries + 1

        ######## organization check #####

        for x in range(0,len(Organizations)):

            organization_name = str(Organizations[x])

            if organization.upper() == organization_name.upper():

                print ("Organization Found \n ")

                del Organizations[x]

                del Domains[x]

                del IP_address[x]

                del Minutes[x]

                tried = True

                data_del = True

                break

        if tried == False:

            print ("Organization Not Found. \n ")

    if tries >= 3:

        print "Limit Exceeded."

    return Organizations, Domains, IP_address, Minutes

def opt6():

     sys.exit("Thank you very much for using the server.")

def print_console(Organizations,Domains,IP_address,Minutes):

    for x in range(0, len(Organizations)):

        print(Organizations[x], Domains[x], IP_address[x], Minutes[x])

def write_data(Organizations,Domains,IP_address,Minutes):

    organization = open("organizations.txt", "w")

    for x in range(0, len(Organizations)):

        write = Organizations[x]+'\t'+Domains[x]+'\t'+IP_address[x]+'\t'+str(Minutes[x])+'\n'

        organization.write(write)

    organization.close()

    print ("Data Written \n")

def menu():


    options = [2,3,4,5,6]

    terminate = False

    maximum_try = 0

    while terminate == False and maximum_try < 3:

        input = raw_input("\n \nWelcome to the server.\nPlease Select following options from the menu \n " \
                          "1. Press 2 for finding the maximum , minimum and mean of minutes \n " \
                          "2. Press 3 for Sorting the data \n" \
                          " 3. Press 4 for adding new organization to the server \n" \
                          " 4. Press 5 for deleting the organization from the server \n" \
                          " 5. Press 6 for terminating the program \n")

        if int(input)in options:

            return int(input)

        else:

            print " Wrong Input. Please enter the option again \n"

            maximum_try = maximum_try + 1

    sys.exit("Invalid Options. Thank you for using the server. \n")



if __name__ == '__main__':

    start = True

    while start == True:

        Users = []

        Passwords = []

        Organizations = []

        Domains = []

        IP_address = []

        Minutes = []

        Users, Passwords, Organizations, Domains, IP_address, Minutes = read_data()

        input = menu()

        if input in [2,3,4,5,6]:

            if input == 2:

                max,min,mean = opt2(Minutes)

                print "Maximum minutes = " + str(max) + "\n" \
                      "Minimum minutes = " + str(min) + "\n" \
                      "Average minutes = " + str(mean) + "\n"

                time.sleep(3)


            if input == 3:

                Organizations, Domains, IP_address, Minutes = opt3(Organizations, Domains, IP_address, Minutes)

                print_console(Organizations, Domains, IP_address, Minutes)

                time.sleep(3)

            if input == 4:

                Organizations, Domains, IP_address, Minutes = opt4(Organizations, Domains, IP_address, Minutes)

                write_data(Organizations, Domains, IP_address, Minutes)

                print_console(Organizations, Domains, IP_address, Minutes)

                time.sleep(3)

            if input == 5:

                Organizations, Domains, IP_address, Minutes = opt5(Organizations, Domains, IP_address, Minutes)

                write_data(Organizations, Domains, IP_address, Minutes)

                print_console(Organizations, Domains, IP_address, Minutes)

                time.sleep(3)

            if input == 6:

                opt6()



