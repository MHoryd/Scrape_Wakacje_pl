import os

class file_manager:


    def reports_files_presence_check(self):
        list = os.listdir('./Reports')
        if len(list) > 0:
            return True
        else:
            return False

    def delete_report_files(self):
        list = os.listdir('./Reports')
        for file in list:
            os.remove('./Reports/' + file)