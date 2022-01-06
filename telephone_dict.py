from os import name,system
import datetime

def clear():
    if name == 'nt':
        _ = system('clear')
    else:
        _ = system('cls')

class Phone:

    # Constructor of Class
    # name is clue of direcotoy name
    # name_list is used for store person name in list ..
    # add_phone_number is used for store number and name dictionary 


    def __init__(self,name,name_list):
        self.name=name
        self.name_list=name_list
        self.add_phone_number={}  

    # data_file FUNCTION is used for parsed data in file and store in add_phone_number {}

    def data_file(self,file1):
        with open(file1) as f:
            lines=f.readlines()
            if lines==[] :
                pass
            else:
                for line in lines:
                    parsed=line.split(',')
                    self.add_phone_number.update({int(parsed[0].strip()) : parsed[1].strip()})
                    self.name_list.append(parsed[1].strip())

    # data_store_file  FUNCTION is used for store data in file 
     
    def data_store_file(self,number,name):
        with open('telephone.txt','a')as fw:
            fw.write(f"{number},{name}\n")


    # delete_data_in_file FUNCTION is used for delete data in file

    def delete_data_in_file(self,number):                                     
        import os
        new_file_store_data={}
        with open('telephone.txt','r') as fd:
            lines=fd.readlines()
            for line in lines:
                line1=line.split(',')
                # print(line)
                # if line1[0]!=str(number):
                if str(number) not in line1:
                    new_file_store_data.update({line1[0]:line1[1]})
                else:
                    # print('wHAT hAPPENS WITH mE ?')
                    pass

        os.remove('telephone.txt')
        with open('telephone.txt','a') as fw:
            for num,name in new_file_store_data.items():
                fw.write(f"{num},{name}")

          
            
    # display_phone_numbers FUNCTION is used for display all contact in phone directory

    def display_phone_numbers(self):
        if self.add_phone_number=={}:
            print('\t\tEMPTY')
        print('\n\t','-'*59)
        print('\t\t\tPerson Name\t  |  \tPhone Number')
        j=1
        for key,value in self.add_phone_number.items():
            print('\t','-'*59)
            print(f"\t{j} | \t\t{value}\t  |  \t0{key}\t    |")
            j+=1
        print('\t','-'*59)

    # addition_number FUNCTION  is used for save number add_phone_number and data_store_file

    def addition_number(self,number,name):
        if number not in self.add_phone_number.keys():
            self.name_list.append(name)
            self.add_phone_number.update({number : name})
            self.data_store_file(number,name)
            print('\t\tNumber store in database successfully .')
        else:
            print(f'\t\tThis {number} already exits by {self.add_phone_number[number]}')

    # remove_number FUNCTION is used for delete contact from file and add_phone_number    

    def remove_number(self,number):
        if number in self.add_phone_number.keys():
            self.name_list.remove(self.add_phone_number[number])
            self.add_phone_number.pop(number)
            self.delete_data_in_file(number)
            print('\t\tThe number deleted successfully .')
        else:
            print(f"\t\tThis number not in phone directory . Please chech your number..")

    # search_number is used for search number in phone directory 

    def search_number(self,number):
        if self.add_phone_number=={}:
            print('\t\tEMPTY')

        elif number in self.add_phone_number.keys():
            print(f"\t\tThis number exit in phone directory with name {self.add_phone_number[number]}")
        else:
            print('\t\tThis phone number not exit in phone directory . please check your number..')

    # search_name is used for search name in phone directory 

    def search_name(self,name):
        if self.add_phone_number=={}:
            print('\t\tEMPTY')

        elif name in self.name_list:
            # print('\t\tThis name exit in phone directory .')
            j=1
            for key,value in self.add_phone_number.items():
                if name==value:
                    print(f"\t\t{j} . {value}   ------  0{key}")
                    j+=1
        else:
            print('\t\tThis name not exit in phone directory .')


    # display_name is used for display all name in phone directory 

    def display_name(self):
        if self.name_list==[]:
            print('\t\tEMPTY')
        j=1
        for name in self.name_list:
            print(f"\t\t{j} . {name}")
            j+=1
       

if __name__ == "__main__":
    phone_obj=Phone("Welcome To Haider's Phone Directory",[])
    phone_obj.data_file('telephone.txt')


    print(f'\n\n\n\t\t\t\t\t\t\t{phone_obj.name}\n\n')
    print('\t1 . Display All Contacts In Directory\t\t2 . Add Contact In Directory\t\t3 . Remove Number In Contact\n\n\t4 . Search Number In Directory By Number\t5 . Search Contact In Directory By Name\t 6 .Display All Contact In Directory\n\n\t\t\t\t\t\t\t7 . For Exit The Programme')
    print('\n\n\n')


    # print('\n\n\t\t\t\t\tPHONE DIRECTORY ...\n\n')
    # print('\t\t\t\t1 . Display all Contacts in Directory .')
    # print('\t\t\t\t2 . Add Contact in Directory .')
    # print('\t\t\t\t3 . Remove Contact from Directory .')
    # print('\t\t\t\t4 . Search Contact in Directory by number .')
    # print('\t\t\t\t5 . Search Contact in Directory by name .')
    # print('\t\t\t\t6 . Display all name in Directory .')
    # print('\t\t\t\t7 . For exit the programe .\n\n')



    while True:
        # print(f'\n\n\n\t\t\t\t\t\t\t{phone_obj.name}\n\n')
        # print('\t1 . Display All Contacts In Directory\t\t2 . Add Contact In Directory\t\t3 . Remove Number In Contact\n\n\t4 . Search Number In Directory By Number\t5 . Search Contact In Directory By Name\t 6 .Display All Contact In Directory\n\n\t\t\t\t\t\t\t7 . For Exit The Programme\n\n\n\n')
        choice=input('Enter Command For Phone Directory : ').strip()
        if choice=='1':
            phone_obj.display_phone_numbers()
        elif choice=='2':
            number=input('Please enter a number :').strip().title()
            name=input('Plese enter your name :').strip().title()
            try:
                number1=int(number)
            except Exception as e:
                print('\t\tYour number is not defined please enter in digits....')
            else:
                if name.isnumeric() or name.isspace() or name=='':
                    print('\t\tNumbers are not allowed in name ....')
                else:
                    total=''
                    for i in name:
                        if i.isalpha() or i.isspace():
                            total+=i
                        else:
                            break
                    if len(name)==len(total):
                        phone_obj.addition_number(number1,name)
                    else:
                        print('\t\tNumbers are not allowed in name ...')

        elif choice=='3':
            number=input('Enter a number that you want delete : ').strip()
            try:
                number1=int(number)
            except Exception as e:
                print('\t\tYour number is not defined in digits .....')
            else:
                phone_obj.remove_number(number1)
        
        elif choice=='4':
            number=input('Please enter a number for search ...').strip()
            try:
                number1=int(number)
                phone_obj.search_number(number1)
            except Exception as e:
                print('\t\tYour number is not defined in alphabets .....')
        elif choice=='5':
            name=input('Please enter name for search :').strip().title()
            try:
                name = str(name)
            except Exception as e:
                print('\t\tOnly alphabets are allowed in name ...')
            else:
                if name.isnumeric() or name.isspace() or name=='':
                    print('\t\tYour name is not defined please check it ....')
                else:
                    total=''
                    for i in name:
                        if i.isalpha() or i.isspace():
                            total+=i
                        else:
                            break
                    if len(name)==len(total):
                        phone_obj.search_name(name)
                    else:
                        print('\t\tNumbers are not allowed in name ...')
        elif choice=='6':
            phone_obj.display_name()
        elif choice=='7'or choice=='q':
            exit()
        else:
            print("Some Thing Went Wrong In Your Choice Please Give Me Right Options In Given Below !")

            