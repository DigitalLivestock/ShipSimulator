class Database:
    def __init__(self, filename, options="a+"):
        self.filename = filename
        self.filestream = open(filename, options)

    def append(self, line):
        self.filestream.write(line + "\n")

    def get_all_data(self):
        return self.filestream.readlines()

    def close(self):
        self.filestream.close()


if "__main__" == __name__:
    print("--Test: database_simple--")
    print("[*]Executing constructor...")
    db = Database("test_db_file.txt")
    print("...done!")
    print("[*]Testing self.append(): ")
    db.append("line 1")
    db.append("line 2")
    db.append("line 3")
    print("[*]Testing get_all_data():")
    print(db.get_all_data())
    db.close()
