import argparse

from google_driver_server import GoogleDriveAutomation


class SimpleTestRunner:

    def __init__(self, google_drive_auto: GoogleDriveAutomation):
        self.__gda = google_drive_auto

    def test_get_file_list(self):
        assert self.__gda.get_file_list()

    def test_print_file_list_no_cache(self):
        assert self.__gda.print_each_element(True)

    def test_print_file_list_cache(self):
        assert self.__gda.print_each_element()

    def test_no_print_file_list_no_cache(self):
        assert self.__gda.print_each_element(False)

    def test_print_file_amount_no_cache(self):
        assert self.__gda.print_total_number_of_files(True)

    def test_print_file_amount_cache(self):
        assert self.__gda.print_total_number_of_files()

    def test_no_print_file_amount_no_cache(self):
        assert self.__gda.print_total_number_of_files(False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', default=None)
    parser.add_argument('--password', default=None)
    args = parser.parse_args()

    gda = GoogleDriveAutomation(args)
    test_runner = SimpleTestRunner(gda)

    test_runner.test_no_print_file_amount_no_cache()

    # more tests
