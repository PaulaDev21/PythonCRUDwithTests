import unittest as ut

from Card import BasicCard


class CardTests(ut.TestCase):
    def setUp(self):
        self.card1 = BasicCard('card title', 'content for testing')
        self.card2 = BasicCard('second card title', 'content for testing')
        print(self.card1, self.card2)
        # return super().setUp()

    def test_card_creation(self):
        self.assertIs(type(self.card1), BasicCard)

    def test_adding_related_when_one(self):
        related_before = len(self.card1.related)
        self.card1.add_related(self.card2)
        self.assertEqual(len(self.card1.related), related_before + 1)

    def test_adding_related_when_list(self):
        related_before = len(self.card1.related)
        card_list = [self.card2]
        self.card1.add_related(card_list)
        self.assertEqual(len(self.card1.related),
                         related_before + len(card_list))

    def tearDown(self):
        del self.card1
        del self.card2
        # return super().tearDown()


if __name__ == '__main__':
    ut.main()
