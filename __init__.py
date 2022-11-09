from App import App

def main():
    app = App()
    option = greet()
    while(option != 3):
        if(option == 1):
            app.review()
        if(option == 2):
            app.test()        
        option = greet()

    print(app.df)
    app.exit()   

def greet() -> str:
    print('*' * 30)
    print('Studying German Words...')
    print('1: Review my cards.')
    print('2: Test my knowledge.')
    print('3: Save & Quit')
    option = input('Choose an option (1, 2, or 3): ')
    return int(option)



if __name__ == '__main__':
    main()
    