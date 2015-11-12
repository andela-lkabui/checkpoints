from random import random

from spaces.living import Living
from spaces.office import Office
from custom import utilities
from amity import Amity
from people.fellow import Fellow
from people.staff import Staff

campus = Amity()
campus.prePopulate()

# useful vars
rangeError = 'Range error: *** Please select a number that is within the range'
valueError = 'Value error: *** Please enter a number in digit form ***\n'

file_path = utilities.getPath('data/')

while (True):
    utilities.mainMenu()
    answer = raw_input('Enter a number between 0 - 5 to select a menu.\n')
    try:
        # catch non integer input from the user
        answer = int(answer)
        # catch int that are outside the range in the menu
        if ((answer < 0) or (answer > 5)):
            utilities.clearScreen()
            print rangeError, ' 0 - 5 ***\n'
            continue
    except ValueError:
        utilities.clearScreen()
        print valueError
    else:
        if (answer == 0):
            utilities.clearScreen()
            print 'Thank you for using this product. Goodbye. \n\n'
            break
        else:
            if (answer == 1):
                # Allocate people to rooms
                utilities.clearScreen()
                while (True):
                    # Choose either staff or fellow
                    utilities.choosePersonMenu()
                    chosen = raw_input('Enter a number between 0 - 2 to select a menu.\n')
                    try:
                        # catch non integer input from the user
                        chosen = int(chosen)
                        # catch int that are outside the range in the menu
                        if ((chosen < 0) or (chosen > 2)):
                            utilities.clearScreen()
                            print rangeError, ' 0 - 5 ***\n'
                            continue
                    except ValueError:
                        utilities.clearScreen()
                        print valueError
                    else:
                        if (chosen == 0):

                            utilities.clearScreen()
                            # quit this menu
                            break
                        elif (chosen == 1):
                            # Allocating staff (offices only)
                            utilities.clearScreen()
                            # Select app or text file data entry option
                            utilities.appOrTextFileMenu()
                            how = raw_input('Enter a number between 0 - 2 to select a menu \n')
                            try:
                                how = int(how)
                                if ((how < 0) or (how > 2)):
                                    utilities.clearScreen()
                                    print rangeError, ' 0 - 2 *** \n'
                                    continue
                            except ValueError:
                                utilities.clearScreen()
                                print valueError
                            else:
                                if (how == 0):
                                    utilities.clearScreen()
                                    # Quit this menu
                                    break
                                elif (how == 1):
                                    utilities.clearScreen()
                                    while (True):
                                        staffName = raw_input('Enter the name of the staff member. \n')
                                        if staffName:
                                            worker = Staff(staffName)
                                            campus.allocate(worker, 'Office')
                                            break
                                elif (how == 2):
                                    utilities.clearScreen()

                                    # read from unallocated list file
                                    uStaff = open(file_path + 'input.txt')
                                    uStaffList = []
                                    edits = ''
                                    for line in uStaff.readlines():
                                        if line[0] == '>':
                                            staff = Staff(line[1::])
                                            uStaffList.append(staff)
                                        elif line[0] != '>':
                                            edits += line

                                    # re-write file and exclude unallocated
                                    # staff (retrieved above)
                                    uStaff = open(file_path + 'input.txt', 'w')
                                    uStaff.write(edits)
                                    uStaff.close()

                                    # Allocate as long as there are office
                                    # spaces and unallocated staff
                                    while (len(uStaffList) > 0):
                                        randStaff = int(random() * len(uStaffList))
                                        campus.allocate(uStaffList[randStaff], 'Office')
                                        uStaffList.pop(randStaff)

                                    # Save unallocated people back to file
                                    if (len(uStaffList) > 0):
                                        uStaff = open(file_path + 'input.txt', 'a+')
                                        for staff in uStaffList:
                                            uStaff.write('>' + staff.name)

                        elif (chosen == 2):
                            # Allocating fellows
                            utilities.clearScreen()
                            # Select the method for data input
                            utilities.appOrTextFileMenu()
                            how = raw_input('Enter a number between 0 - 2 to select a menu \n')
                            try:
                                how = int(how)
                                if ((how < 0) or (how > 2)):
                                    utilities.clearScreen()
                                    print rangeError, ' 0 - 2 *** \n'
                                    continue
                            except ValueError:
                                utilities.clearScreen()
                                print valueError
                            else:
                                if (how == 0):

                                    utilities.clearScreen()
                                    # Quit this menu
                                    break
                                elif (how == 1):
                                    # Allocate via app
                                    utilities.clearScreen()
                                    # select between office and living space
                                    utilities.chooseOfficeOrLivingMenu()
                                    space = raw_input('Enter a number between 0 - 2 to select a menu \n')
                                    try:
                                        space = int(space)
                                        if ((space < 0) or (space > 2)):
                                            utilities.clearScreen()
                                            print rangeError, ' 0 - 2 *** \n'
                                            continue
                                    except ValueError:
                                        utilities.clearScreen()
                                        print valueError
                                    else:
                                        if (space == 0):
                                            utilities.clearScreen()
                                            break
                                        elif (space == 1):
                                            utilities.clearScreen()
                                            # Office space selected
                                            while (True):
                                                fellowName = raw_input('Enter the name of the fellow. \n')
                                                if fellowName:
                                                    fellow = Fellow(fellowName)
                                                    campus.allocate(fellow, 'Office')
                                                    break
                                        elif (space == 2):

                                            utilities.clearScreen()
                                            # Living space selected
                                            while (True):
                                                fellowName = raw_input('Enter the name of the fellow. \n')
                                                if fellowName:
                                                    fellow = Staff(fellowName)
                                                    campus.allocate(fellow, 'Living')
                                                    break
                                elif (how == 2):
                                    # Allocate via text file
                                    utilities.clearScreen()
                                    # select between office and living space
                                    utilities.chooseOfficeOrLivingMenu()
                                    space = raw_input('Enter a number between 0 - 2 to select a menu \n')
                                    try:
                                        space = int(space)
                                        if ((space < 0) or (space > 2)):
                                            utilities.clearScreen()
                                            print rangeError, ' 0 - 2 *** \n'
                                            continue
                                    except ValueError:
                                        utilities.clearScreen()
                                        print valueError
                                    else:
                                        if (space == 0):
                                            utilities.clearScreen()
                                            break
                                        elif (space == 1):
                                            utilities.clearScreen()

                                            # Office space selected
                                            # read from unallocated list file
                                            uFellowFile = open(file_path + 'input.txt')
                                            uFellowList = []
                                            edits = ''
                                            for line in uFellowFile.readlines():
                                                if line[0] == '#' and line[1] == '#':
                                                    fellow = Fellow(line[2::])
                                                    uFellowList.append(fellow)
                                                elif line[1] != '#':
                                                    edits += line

                                            # re-write file and exclude
                                            # unallocated staff (retrieved
                                            # above)
                                            uFellowFile = open(file_path + 'input.txt', 'w')
                                            uFellowFile.write(edits)
                                            uFellowFile.close()

                                            # Allocate as long as there are
                                            # office spaces and unallocated
                                            # staff
                                            while (len(uFellowList) > 0):
                                                randFellow = int(random() * len(uFellowList))
                                                campus.allocate(uFellowList[randFellow], 'Office')
                                                uFellowList.pop(randFellow)

                                            # Save unallocated people back to file
                                            if (len(uFellowList) > 0):
                                                uFellowFile = open(file_path + 'input.txt', 'a+')
                                                for fellw in uFellowFile:
                                                    uFellowFile.write('##' + fellw.name)
                                        elif (space == 2):
                                            utilities.clearScreen()

                                            # Living space selected
                                            # read from unallocated list file
                                            uFellowFile = open(file_path + 'input.txt')
                                            uFellowList = []
                                            edits = ''
                                            for line in uFellowFile.readlines():
                                                if line[0] == '#' and line[1] != '#':
                                                    fellow = Fellow(line[1::])
                                                    uFellowList.append(fellow)
                                                else:
                                                    edits += line

                                            # re-write file and exclude
                                            # unallocated staff (retrieved
                                            # above)
                                            uFellowFile = open(file_path + 'input.txt', 'w')
                                            uFellowFile.write(edits)
                                            uFellowFile.close()

                                            # Allocate as long as there are
                                            # office spaces and unallocated
                                            # staff
                                            while (len(uFellowList) > 0):
                                                randFellow = int(random() * len(uFellowList))
                                                campus.allocate(uFellowList[randFellow], 'Living')
                                                uFellowList.pop(randFellow)

                                            # Save unallocated people back to
                                            # file
                                            if (len(uFellowList) > 0):
                                                uFellowFile = open(file + 'input.txt', 'a+')
                                                for fellw in uFellowFile:
                                                    uFellowFile.write('#' + fellw.name)

            elif (answer == 2):
                # get list of allocations
                pass
            elif (answer == 3):
                # print allocation list
                utilities.clearScreen()

                allocations = open(file_path + 'allocated.txt')

                for lines in allocations.readlines():
                    if lines[0:-1] == 'Living':
                        # A header (visual separator)
                        print 'Living Spaces (Fellows Only) \n', '-' * 80, '\n'
                    elif lines[0] == '+':
                        # The name of a living space
                        print lines[1::]
                        print '-' * 40
                    elif lines[0] == '\t' and lines[1] != '>' and lines[1] != '#':
                        # if it starts with a tab and it's not an office allocation
                        print '\t', lines[1::]
                    elif lines[0:-1] == 'Office':
                        print '\n\n', 'Office Spaces \n', '-' * 80, '\n'
                    elif lines[0] == '-':
                        # The name of an office space
                        print lines[1::], '\n', '-' * 40
                    elif lines[0] == '\t' and lines[1] == '>':
                        # Staff members in offices
                        print '\t (S): ', lines[2::]
                    elif lines[0] == '\t' and lines[1] == '#':
                        # Fellows in offices
                        print '\t (F): ', lines[2::]
            elif (answer == 4):
                # list unallocated people
                utilities.clearScreen()
                unallocated = open(file_path + 'input.txt')
                fellowOfficeList = []
                fellowLivingList = []
                staffList = []
                
                while True:
                    line = unallocated.readline()
                    if line:
                        if (line[0] == '>'):
                           staffList.append(line[1::])
                        elif (line[0] == '#' and line[1] == '#'):
                            fellowOfficeList.append(line[2::])
                        elif (line[0] == '#' and line[1] != '#'):
                            fellowLivingList.append(line[1::])
                    else:
                        break  
    
                # print the unallocated staff
                print '\n\n\n', '-' * 40, ' Unallocated Staff List ', '-' * 40
                for staff in staffList:
                    print staff

                # print the unallocated fellows (Offices)
                print '-' * 40, ' Unallocated Fellow List (Offices)', '-' * 40
                for fellow in fellowOfficeList:
                    print fellow

                # print the unallocated fellows (Living)
                print '-' * 40, ' Unallocated Fellow List (Living)', '-' * 40
                for fellow in fellowLivingList:
                    print fellow


            elif (answer == 5):
                utilities.clearScreen()

                while True:
                    utilities.listRooms()
                    room = raw_input('Enter a number between 0 - 2 to select a menu.\n')
                    try:
                        room = int(room)
                        if ((room < 0) or (room > 2)):
                            utilities.clearScreen()
                            print rangeError, ' 0 - 2 *** \n'
                            continue
                    except ValueError:
                        utilities.clearScreen()
                        print valueError
                    else:
                        if room == 0:

                            utilities.clearScreen()
                            break
                        elif room == 1:
                            utilities.clearScreen()

                            # List the offices
                            offices = campus.officeRooms
                            print '-' * 40, ' Office List ', '-' * 40
                            counter = 1
                            for office in offices:
                                print('{0}. {1}'.format(counter, office.name[:-1]))
                                counter += 1
                            print '\n0. Exit sub-menu \n'

                            selected = raw_input('Enter a number between 0 - ' + str(counter - 1) + ' to select a menu.\n')
                            try:
                                selected = int(selected)
                                if ((selected < 0) or (selected > counter)):
                                    utilities.clearScreen()
                                    print rangeError, ' 0 - ', counter, ' *** \n'
                                    continue
                            except ValueError:
                                utilities.clearScreen()
                                print valueError
                            else:
                                if (selected == 0):

                                    utilities.clearScreen()
                                    break
                                else:
                                    utilities.clearScreen()
                                    occupants = offices[selected - 1].occupants
                                    print '\n\n', 'List of Occupants in ', offices[selected - 1].name, '\n'
                                    print '-' * 40, '\n'
                                    counter = 1
                                    for person in occupants:
                                        print counter, '.', person.name
                                        counter += 1
                        elif room == 2:
                            utilities.clearScreen()

                            # List the living spaces
                            lSpaces = campus.livingRooms
                            print '-' * 40, ' Living Spaces List ', '-' * 40
                            counter = 1
                            for space in lSpaces:
                                print('{0}. {1}'.format(counter, space.name[:-1]))
                                counter += 1
                            print '\n0. Exit sub-menu \n'
                            selected = raw_input('Enter a number between 0 - ' + str(counter - 1) + ' to select a menu.\n')
                            try:
                                selected = int(selected)
                                if ((selected < 0) or (selected > counter)):
                                    utilities.clearScreen()
                                    print rangeError, ' 0 - ', counter, ' *** \n'
                                    continue
                            except ValueError:
                                utilities.clearScreen()
                                print valueError
                            else:
                                if (selected == 0):
                                    utilities.clearScreen()
                                    break
                                else:
                                    utilities.clearScreen()
                                    occupants = lSpaces[selected - 1].occupants
                                    print 'List of Occupants in ', lSpaces[selected - 1].name, '\n'
                                    print '-' * 40, '\n'
                                    counter = 1
                                    for person in occupants:
                                        print counter, '. ', person.name
                                        counter += 1

