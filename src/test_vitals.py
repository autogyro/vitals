import unittest
import vitals
import os
import datetime

TEST_FILE = "../test.csv"

class VitalsTest(unittest.TestCase):

    def test_create_file(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        ret = vitals.log_vitals(TEST_FILE, 120, 70, 80, datetime.datetime(2019, 1, 12, 16, 50, 0))

        self.assertEqual(True, os.path.exists(TEST_FILE))
        self.assertEqual(0, ret)

        f = open(TEST_FILE, 'r')
        contents = f.read()
        f.close()

        self.assertEqual('date,time,systolic,diastolic,pulse\n2019-01-12,16:50:00,120,70,80\n', contents)

        os.remove(TEST_FILE)

    def test_append_file(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        vitals.log_vitals(TEST_FILE, 120, 70, 80, datetime.datetime(2019, 1, 12, 16, 50, 0))
        ret = vitals.log_vitals(TEST_FILE, 125, 75, 85, datetime.datetime(2019, 1, 13, 6, 20, 10))

        self.assertEqual(0, ret)

        f = open(TEST_FILE, 'r')
        contents = f.read()
        f.close()

        self.assertEqual('date,time,systolic,diastolic,pulse\n2019-01-12,16:50:00,120,70,80\n2019-01-13,06:20:10,125,75,85\n', contents)

        os.remove(TEST_FILE)

    def test_empty_file(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        f = open(TEST_FILE, 'w')
        f.close()

        ret = vitals.log_vitals(TEST_FILE, 120, 70, 80, datetime.datetime(2019, 1, 12, 16, 50, 0))

        self.assertEqual(True, os.path.exists(TEST_FILE))
        self.assertEqual(0, ret)

        f = open(TEST_FILE, 'r')
        contents = f.read()
        f.close()

        self.assertEqual('date,time,systolic,diastolic,pulse\n2019-01-12,16:50:00,120,70,80\n', contents)

        os.remove(TEST_FILE)

    def test_log_invalid(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        f = open(TEST_FILE, 'w')
        f.write('test')
        f.close()

        ret = vitals.log_vitals(TEST_FILE, 120, 70, 80, datetime.datetime(2019, 1, 12, 16, 50, 0))

        self.assertEqual(-1, ret)

        f = open(TEST_FILE, 'r')
        contents = f.read()
        f.close()

        self.assertEqual('test', contents)

        os.remove(TEST_FILE)

    def test_generates_proper_csv(self):
        # It can format all strings
        self.assertEqual('date,time,systolic,diastolic,pulse', vitals.to_csv_format('date', 'time', 'systolic', 'diastolic', 'pulse'))

        # It can format all numbers
        self.assertEqual('1,2,3,4', vitals.to_csv_format(1, 2, 3, 4))

        # It can format mixed values (strings and numbers)
        self.assertEqual('1-12-2019,16:15,120,70,80', vitals.to_csv_format('1-12-2019', '16:15', 120, 70, 80))

    def test_detects_improper_format(self):
        # It can detect a single line of csv
        self.assertEqual(True, vitals.is_proper_csv('date,time,systolic'))

        # It can detect multiple lines of proper csv
        self.assertEqual(True, vitals.is_proper_csv('one,two,three\n1,2,3\n4,5,6'))

        # It doesn't care about ending newlines
        self.assertEqual(True, vitals.is_proper_csv('one,two,three\n1,2,3\n4,5,6\n\n'))

        # It detects uneven columns
        self.assertEqual(False, vitals.is_proper_csv('one,two,three\n1,2,3\n4,5'))

        # It passes an empty string
        self.assertEqual(True, vitals.is_proper_csv(''))

        # It uses the number of cols
        self.assertEqual(True, vitals.is_proper_csv('one,two,three\n1,2,3\n4,5,6', 3))
        self.assertEqual(False, vitals.is_proper_csv('one,two,three\n1,2,3\n4,5,6', 4))

        # It doesn't care about empty columns
        self.assertEqual(True, vitals.is_proper_csv('one,two,three\n1,,3\n,,'))



if __name__ == '__main__':
    unittest.main()
