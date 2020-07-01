import subprocess
import os
import time
import datetime
import csv


class UserInterface(object):

    def __init__(self):
        super(UserInterface, self).__init__()

    def get_username2(self):
        print('Enter your ID: ', end='')
        return input()

    def request_question2(self):
        print('Enter Your Message: ', end='')
        return input()

    def send_answer2(self, answer, execution_time):
        print(answer + ' (response time: {:.2f}s)'.format(execution_time))

    # def exception_message1(self, string):
        # return


class DialogManager(object):

    def __init__(self):
        super(DialogManager, self).__init__()
        self.username = None
        self.request_time = None
        self.log_dir = None
        self.user_interface = UserInterface()
        self.blender_interface = BlenderInterface()

    def run(self):
        self.get_username1()
        self.make_csv()
        while True:
            question = self.request_question1()
            q_time = time.time()
            answer = self.request_answer1(question)
            if question == '[EXIT]':
                break  # shutdown
            a_time = time.time()
            execution_time = a_time - q_time
            # if 'error'
            # self.error
            self.send_answer1(answer, execution_time)
            self.add_log(question, answer, q_time, a_time)

    def get_username1(self):
        self.username = self.user_interface.get_username2()

    def make_csv(self):
        self.log_dir = os.path.expanduser('~/simsimE/log')
        os.makedirs(self.log_dir, exist_ok=True)
        f = open(os.path.join(self.log_dir, '{}.csv'.format(self.username)), 'w', encoding='utf-8')
        self.wr = csv.writer(f)
        self.wr.writerow(['Source', 'Data', 'Time'])


    def request_question1(self):
        return self.user_interface.request_question2()

    def request_answer1(self, question):
        return self.blender_interface.request_answer2(question)

    def send_answer1(self, answer, execution_time):
        self.user_interface.send_answer2(answer, execution_time)

    # def exception_message1(self, string):
        # return

    def add_log(self, question, answer, q_time, a_time):
        a_time = datetime.datetime.fromtimestamp(a_time)
        q_time = datetime.datetime.fromtimestamp(q_time)
        self.wr.writerow([self.username, question, q_time])
        self.wr.writerow(['simsimE', answer[11:], a_time])

class BlenderInterface(object):

    def __init__(self):
        super(BlenderInterface, self).__init__()
        self.start_blender()

    def start_blender(self):
        os.chdir(os.path.expanduser('~/ParlAI'))
        command = 'python parlai/scripts/interactive.py -t blended_skill_talk -mf zoo:blender/blender_90M/model --include-personas False'
        self.blender = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("!!!!!!!!!!!! welcome to SimSimE world !!!!!!!!!!!!\n")
        time.sleep(6)

    def request_answer2(self, question):
        # a = f"{input()}\n".encode("utf-8")
        a = f"{question}\n".encode("utf-8")
        self.blender.stdin.write(a)
        self.blender.stdin.flush()
        while True:
            answer = self.blender.stdout.readline()#.decode("utf-8").strip()
            answer = answer.decode("utf-8")
            if 'Enter Your Message' in answer:
                break
        if 'TransformerGenerator' in answer:
            answer = answer.replace('TransformerGenerator', 'SimSimE')
        answer = answer[20:-1]
        return answer

if __name__ == '__main__':
    dialog_manager = DialogManager()
    dialog_manager.run()
