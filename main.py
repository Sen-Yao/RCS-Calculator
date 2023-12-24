import os

from fileio import load_E_field
def main():
    print("Hello, World!")
    path = 'data'
    path = os.path.join(path, 'E-field.txt')
    if not os.path.isfile(path):
        print("Can't find E-field.txt")
        exit(1)

    E_field_table = load_E_field(path)

if __name__ == "__main__":
    # 确保脚本在被导入时不会立即执行
    main()
