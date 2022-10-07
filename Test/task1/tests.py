from hstest import SQLTest, dynamic_test, correct, wrong


class Test(SQLTest):
    queries = {
        'create_book_table': None
    }

    @dynamic_test
    def test_create_table(self):
        self.execute('create_book_table')
        result_book = self.execute_and_fetch_all("PRAGMA table_info(book);")
        if not result_book:
            return wrong("Book table is missing!")

        return correct()


if __name__ == '__main__':
    Test().run_tests()
