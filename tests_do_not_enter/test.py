
import ast



def main():
    dot = "[100,200,300,400,500]"
    lis = ast.literal_eval(dot)
    print lis

if __name__ == '__main__':
    main()