# -*- coding: utf-8 -*-


class DataBase:
    def __init__(self):
        """
        init for the database
        dictionary kind
        """
        self.dic = {}

    def set_value(self, key, val):
        """
        set value in the dictionary
        ;key: a key
        ;val: the value
        """
        if self.is_key(key):
            self.dic[key] = val
            return True
        else:
            return False

    def get_obj(self, key):
        """
        returns the value in the dictionary
        that its key is key
        ;key: the value`s key
        """
        if self.is_key(key):
            return self.dic[key]
        return "invalid key"

    def delete_value(self, key):
        """
        delete a key and value from the
        dictionary
        ;ket: hte key
        """
        if key in self.dic:
            self.dic.pop(key)
            return "delete"
        return "invalid key"

    def is_key(self, key):
        """
        check if the given key in an
        integer
        ;key: the given key
        """
        if type(key) == int:
            return True
        return False

def main():
    pass

if __name__ == '__main__':
    a = DataBase()
    assert a.set_value(1, 11)
    assert a.set_value(2, 22)
    assert a.get_obj(1) == 11
    assert a.get_obj(2) == 22
    assert a.delete_value(1) == "delete"
    assert a.is_key(2)
