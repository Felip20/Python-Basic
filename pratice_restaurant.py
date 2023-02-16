class Restaurant:
    menus={
        'pizza' : 5000,
        'cola' : 500,
        'buger' : 1000
    }

    def __init__(self):
        self.total = 0 
        self.orders = []
    
    def addOrder(self,order):
        self.orders.append(order);
        self.total+=self.menus[order]
    
    def printBill(self):
        for order in self.orders:
            print(f'{order} : {self.menus[order]}');
        print(f'Total is :{self.total}')

def StartProgram():
    table = Restaurant();
    while True:
        order = input('order :');
        table.addOrder(order);

        another = input('another one : y/n');
        if another == 'y':
            continue;
        if another == 'n':
            table.printBill();
            break;

StartProgram();