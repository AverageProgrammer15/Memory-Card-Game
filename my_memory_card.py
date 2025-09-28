from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
)
from random import shuffle

app = QApplication([])

# Main window
window = QWidget()
window.setWindowTitle('Memo Card')

# Question and Answer
lb_Question = QLabel('The Most Difficult Question in the World')
btn_OK = QPushButton('Answer')

# GroupBox for radio buttons
RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

# Grouping buttons
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]  # list of buttons for shuffling

# Layout for answer options
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# GroupBox for test result
AnsGroupBox = QGroupBox("Test Result")
lb_Result = QLabel("Are you correct or not?")
lb_Correct = QLabel("The correct answer will be shown here")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# Layouts
layout_line1 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2 = QHBoxLayout()
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

# Function Definitions
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False)
    for answer in answers:
        answer.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(f"Correct answer: {right_answer}")
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if btn_OK.text() == 'Answer':
        if answers[0].isChecked():
            show_correct('Correct!')
        elif any(ans.isChecked() for ans in answers[1:]):
            show_correct('Incorrect!')
    else:
        ask('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')

btn_OK.clicked.connect(check_answer)

# Final setup
window.setLayout(layout_card)
ask('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')
window.show()
app.exec()
