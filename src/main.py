from src.data.load_data import load_data

def main():
    test = load_data('data/test')
    train =  load_data('data/train')
    ideal = load_data('data/ideal')

    #save data as pictures

    for column in ideal.columns():
        




if __name__ == '__main__':
    main():
