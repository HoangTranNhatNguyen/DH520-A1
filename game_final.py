import numpy as np
#set up key classes to set scenes (home, store, items)
class Home:
    def __init__(self, name='your house'):
        self.name = name
        self.distance = 0

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return '{} - ${}'.format(self.name, self.price)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if type(other).__name__ == 'Item':
            return self.name == other.name
        elif type(other).__name__ == 'str':
            return self.name == other
        else:
            raise ValueError('Unsupported Datatype')

class Store:
    def __init__(self, name, items, distance):
        self.name = name
        self.items = items
        self.distance = distance
    
    def display_items(self):
        print('Here is a list of items in {}'.format(self.name))
        for item in self.items:
            print('Item: {} - Price: ${}'.format(item.name, item.price))

class Person:
    def __init__(self, name):
        self.name = name
        self.hello_sentences = ['Hello!', 'Hi!', 'How\'s your day', 'How are you?', 'Nice to meet you!', 'Good morning.', 'Hey man.', 'Hey.', 'How is it going?', 'How are you doing?', 'What\'s up!']
        self.goodbye_sentences = ['Goodbye.', 'Bye bye.', 'See you again.']
    def say_hello(self):
        choice = np.random.choice(len(self.hello_sentences))
        print('Person - {}: {}'.format(self.name, self.hello_sentences[choice]))
    def say_goodbye(self):
        choice = np.random.choice(len(self.goodbye_sentences))
        print('Person - {}: {}'.format(self.name, self.goodbye_sentences[choice]))

class Seller(Person):
    def __init__(self, name):
        super().__init__(name)
        self.goodbye_sentences = ['Thank you for shopping today.', 'Thank you and have a good day.', 'Thank you.', 'Have a good day.']
    
    def sell_items(self, items):
        total_price = 0
        for item in items:
            total_price += item.price
        return total_price
    
    def say_hello(self):
        choice = np.random.choice(len(self.hello_sentences))
        print('Seller - {}: {}'.format(self.name, self.hello_sentences[choice]))
    
    def say_goodbye(self):
        choice = np.random.choice(len(self.goodbye_sentences))
        print('Seller - {}: {}'.format(self.name, self.goodbye_sentences[choice]))

class Security(Person):
    def __init__(self, name):
        super().__init__(name)
        self.goodbye_sentences = ['Thank you for shopping today.', 'Thank you and have a good day', 'Thank you']

    def check_face_mask(self, player):
        mask = None
        while True:
            print('Security person - {}: Do you have your face mask with you?'.format(self.name))
            answer = player.response()
            if 'yes' in answer.lower():
                if 'mask' in player.inventory:
                    mask = True
                    print('Security person - {}: Thanks for keeping us safe! Welcome to our store.'.format(self.name))
                    break
                else:
                    print('>>> You did not bring your face mask with you! You lied to the clerk, and they replied:')
                    mask = False
                    print('Security person - {}: I don\'t see your face mask. You need a face mask.'.format(self.name))
                    break
            elif 'no' in answer.lower():
                mask = False
                print('Security person - {}: I cannot allow you in the store without a face mask. Please wear a mask.'.format(self.name))
                break
            else:
                print('Pardon?')
        return mask

    def catch_player(self, success_rate=0.7):
        print('{}: All units alert, a suspect is running on the street!'.format(self.name))
        success = np.random.choice([0,1], p=[1-success_rate, success_rate])
        if success == 0:
            print('{}: We lost him :-('.format(self.name))
        else:
            print('{}: Gotcha! You are arrested.'.format(self.name))
        return success
    
    def say_hello(self):
        choice = np.random.choice(len(self.hello_sentences))
        print('Security person - {}: {}'.format(self.name, self.hello_sentences[choice]))
    
    def say_goodbye(self):
        choice = np.random.choice(len(self.goodbye_sentences))
        print('Security person - {}: {}'.format(self.name, self.goodbye_sentences[choice]))

class Driver(Person):
    def __init__(self, name):
        super().__init__(name)
        self.fee_per_km = 2 # 2 dollars per km
        self.arrival_sentences = ['We have arrived.', 'This is our destination.', 'Here we are.']
    
    def drive_to(self, src, des):
        print('>>> Driving from {} to {} ...'.format(src.name, des.name))
        total_distance = des.distance
        src.distance += total_distance
        des.distance -= total_distance
        return total_distance, total_distance * self.fee_per_km
    
    def say_arrive(self):
        choice = np.random.choice(len(self.arrival_sentences))
        print('>>> {} minutes later'.format(np.random.randint(60)))
        print('Driver - {}: {}'.format(self.name, self.arrival_sentences[choice]))

class Player(Person):
    def __init__(self, name, money, energy):
        super().__init__(name)
        self.money = money
        self.energy = energy
        self.inventory = []
    
    def call_taxi(self, src, des):
        print('>>> You decided to take a taxi to the {}, which is {} km away'.format(des.name, des.distance))
        driver = Driver('Taxi Driver')
        driver.say_hello()
        self.response()
        distance, amount = driver.drive_to(src, des)
        driver.say_arrive()
        self.response()
        paid = self.spend_money(amount)
        if paid:
            driver.say_goodbye()

    def walk(self, src, des):
        print('>>> You decided to walk to the {}, which is {} km away'.format(des.name, des.distance))
        print('>>> {} minutes later'.format(np.random.randint(30,120)))
        remained_energy = self.energy - des.distance
        if remained_energy < 0:
            print('>>> You are now exhausted. You lose.')
            exit(-1)

        total_distance = des.distance
        src.distance += total_distance
        des.distance -= total_distance
        self.energy = max(0, remained_energy)
        print('>>> Your remaining energy is {} and you are {} km away from {}.'.format(self.energy, des.distance, des.name))
    
    def spend_money(self, money):
        print('You will have to pay ${}'.format(money))
        
        if self.money - money < 0:
            answer = input('You run out of money. The only option you have is to run away. Do you want to try this risky move? ')
            if 'yes' in answer.lower():
                being_caught = Security('Police officer').catch_player()
                if being_caught:
                    print('>>> You are now in jail. You lose.')
                    exit(-1)
                else:
                    print('>>> You successfully run away. Your pocket still has ${}'.format(self.money))
                    return 0 # Not paid
            else:
                print('You lose.')
                exit(-1)
        else:
            self.money -= money
        
        print('>>> The remaining amount is ${}'.format(self.money))
        return 1 # Paid

    def add_item(self, item):
        self.inventory.append(item)
    
    def make_travel_dicisions(self, src, des):
        print('>>> You have the following options:')
        if self.money:
            print('- Call taxi')
        if self.energy:
            print('- Walk')
        travel_options = ['call taxi', 'walk']
        while True:
            answer = input('>>> Enter your decison here: ').lower()
            if answer in travel_options[0] and self.money:
                self.call_taxi(src,des)
                break
            elif answer in travel_options[1] and self.energy:
                self.walk(src,des)
                break
            elif self.energy == 0 and self.money == 0 and place.distance != 0:
                print('>>> You ran out of money and energy. You lose!')
                exit(-1)
            else:
                print('Please enter again')
    
    def response(self):
        answer = input('Your response: ')
        print('{}: {}'.format(self.name, answer))
        return answer

class Scene:
    def __init__(self):
        pass
    
    def player_info(self, player):
        print('>>> Hello {}, you have ${} in your pocket, and your energy is {}'.format(player.name, player.money, player.energy))
    
    def bring_items(self, player):
        print('>>> Which of the following personal items are you going to bring before going shopping?')
        print('- Keys')
        print('- Face Masks')
        print('- Silly String')
        print('- Hand Sanitizer')
        print('- Bags')
        personal_items = ['key', 'mask', 'silly string', 'hand sanitizer', 'bag']
        answer = input('Please enter your choices by entering the item names: ')
        for item in personal_items:
            if item in answer:
                player.add_item(item)
        print('>>> Okay, {}, you brought {} with you'.format(player.name, player.inventory))
    
    def at_the_entrance(self, player, security_person, home, store):
        print('>>> You have arrived at the store entrance.')
        print('>>> There is a person at the front checking to see if customers are wearing face masks.')
        while not security_person.check_face_mask(player):
            print('>>> You have to go home to get your face mask. Otherwise, you cannot get what you want.')
            self.go_back_home_for_the_mask(player, home, store)
        print('>>> You are wearing your face mask, you can go in the store.')
    
    def at_the_checkout(self, player, cart):
        seller = Seller('Anna')
        seller.say_hello()
        player.response()
        total = seller.sell_items(cart)
        paid = player.spend_money(total)
        if paid:
            seller.say_goodbye()
        for item in cart:
            player.add_item(item)
    
    def in_the_store(self, player, store):
        store.display_items()
        answer = input('>>> Which items do you want to buy? ')
        cart = []
        for item in store.items:
            if item.name in answer:
                cart.append(item)
        self.at_the_checkout(player, cart)
    
    def on_the_way_to_store(self, player, home, store):
        player.make_travel_dicisions(home,store)
    
    def on_the_way_to_home(self, player, home, store):
        player.make_travel_dicisions(store,home)
    
    def go_back_home_for_the_mask(self, player, home, store):
        self.player_info(player)
        player.make_travel_dicisions(store,home)
        self.bring_items(player)
        player.make_travel_dicisions(home,store)
    
    def go_home(self, player, requested_items):
        # Back to home scene
        print('>>> You find your keys ...')
        if 'key' in player.inventory:
            print('Congrats! You got home successfully.')
            print('You have {} in your inventory'.format(player.inventory))

            forgot_items = []
            for item in requested_items:
                if item not in player.inventory:
                    forgot_items.append(item)
            if len(forgot_items):
                print('However, you forgot to buy {}. You still lose.'.format(item))
            else:
                print('You win! Yayy!')
        else:
            print('You locked your keys in the house. You lose.')
if __name__ == "__main__":
    print('This game is simple: Your partner asked you to go grocery shopping.')
    print('You have a limited amount of money and energy, and you don\'t have a car.')
    print('===> Try to get home safely with the required items.')
    print('--------------------------------------------------------------------------------------')
    
    name = input("What's your name: ")
    money = np.random.randint(50, 100) # Minimum 50 dollars, Maximum 100 dollars.
    energy = np.random.randint(50, 100)
    player = Player(name, money, energy)

    home = Home()
    walmart_items = [Item('chicken', 10), Item('ground beef', 15), Item('flowers', 5), Item('wine', 10)]
    walmart = Store(name='Walmart', items=walmart_items, distance=np.random.randint(1,50))
    security_man = Security('John')
    requested_items = np.random.choice(len(walmart_items), size=np.random.randint(1,len(walmart_items)), replace=False)
    requested_items = [walmart_items[idx].name for idx in requested_items]
    
    print('>>> You were asked to buy: {}'.format(requested_items))
    print('>>> The nearest store is {} km away'.format(walmart.distance))
    print('>>> For every km walking, you lose 1 energy point')
    print('>>> For every km using taxi, you lose $2.')
    print('>>> The game has started!')

    scene = Scene()
    scene.player_info(player)
    scene.bring_items(player)
    scene.on_the_way_to_store(player, home, walmart)
    scene.at_the_entrance(player, security_man, home, walmart)
    scene.in_the_store(player, walmart)
    scene.on_the_way_to_home(player, home, walmart)
    scene.go_home(player, requested_items)