class UserDict:
    contact_dict = {}


class Record(UserDict):
    def input_error(self):
        def wrapper(self, quest):
            self.lst = ['add', 'change']
            for i in self.quest:
                if i in self.lst:
                    self.quest.remove(i)
            try:
                self.contact_dict[self.quest[0].title()] = self.quest[1]
            except IndexError:
                print('Give me name and phone please')
            except KeyError:
                print("...")

            self.set_questions()
        return wrapper


    @input_error
    def quest_1(self, quest):
        self.set_questions()
        
    @input_error    
    def quest_2(self, quest):
        self.set_questions()
            
            
    def quest_3(self, quest):        
        if self.quest[1].casefold().title() in self.contact_dict:
            for k, v in self.contact_dict.items():
                if k.casefold() == self.quest[1].casefold():
                    print(v)
                    self.set_questions()
                else:
                    continue
        else:
            print('Enter user name')
            self.set_questions()


class AddressBook(Record):
    def set_questions(self):
        while True:
            self.quest = input().casefold()
            if self.quest == 'hello':
                print('How can i help you?')
            elif 'add' in self.quest:
                self.quest = self.quest.split()
                return self.quest_1(self.quest)
            elif 'change' in self.quest:
                self.quest = self.quest.split()
                return self.quest_2(self.quest)
            elif 'phone' in self.quest:
                self.quest = self.quest.split()
                return self.quest_3(self.quest)
            elif self.quest == 'show all':
                print(self.contact_dict)
            elif self.quest == 'good bye' or self.quest == 'close' or self.quest == 'exit':
                print('Good bye!')
                break
            elif self.quest == '.':
                break
            else:
                print('Give me name and phone please')
        
c = AddressBook()
c.set_questions()