import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MacroEstimator import Person, Diet

class Ui(QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('user_interface.ui', self)

        self.diet = None

        # Locate Exit button and link close method to it
        self.exit_button = self.findChild(QPushButton, 'exit_button')
        self.exit_button.clicked.connect(lambda:self.close())

        # Calculate button to compute results
        self.calculate_button = self.findChild(QPushButton, 'calculate_button')
        self.calculate_button.clicked.connect(self.print_results)

        # Reset button to reset text field entries
        self.reset_button = self.findChild(QPushButton, 'reset_button')
        self.reset_button.clicked.connect(self.clear_inputs)

        # Radio button for gender
        self.radio_male = self.findChild(QRadioButton, 'radio_male')
        self.radio_male.toggled.connect(self.select_male)
        self.radio_female = self.findChild(QRadioButton, 'radio_female')
        self.radio_female.toggled.connect(self.select_female)

        # Checkbox for active job and approximate body fat %
        self.check_job = self.findChild(QCheckBox, 'active_job')
        self.check_job.stateChanged.connect(self.change_active_job_state)
        self.check_bodyfat = self.findChild(QCheckBox, 'approx_bodyfat')
        self.check_bodyfat.stateChanged.connect(self.change_approx_bodyfat_state)

        # Set original values which will be changed based on the selection
        self.active_job = False
        self.approx_bodyfat = False
        self.gender = None

        # Set values based on text entry
        self.height = self.findChild(QLineEdit, 'height_input')
        self.weight = self.findChild(QLineEdit, 'weight_input')
        self.age = self.findChild(QLineEdit, 'age_input')
        self.bodyfat = self.findChild(QLineEdit, 'bodyfat_input')

        # Set values based on dropdown selection
        self.exercise = self.findChild(QComboBox, 'exercise_freq')
        self.goal = self.findChild(QComboBox, 'goal')

        # Text box for to print output
        self.tmb_display = self.findChild(QTextBrowser, 'lbm_display')
        self.tdee_display = self.findChild(QTextBrowser, 'tdee_display')
        self.macros_display = self.findChild(QTextBrowser, 'macros_display')

        self.show()

    def change_active_job_state(self, state):
        if state == Qt.Checked:
            self.active_job = True
        else:
            self.active_job = False
    
    def change_approx_bodyfat_state(self, state):
        if state == Qt.Checked:
            self.approx_bodyfat = True
        else:
            self.approx_bodyfat = False

    def select_male(self, selected):
        if selected: self.gender = 'male'

    def select_female(self, selected):
        if selected: self.gender = 'female'

    def create_diet(self):
        person = Person(float(self.weight.text()), float(self.height.text()), int(self.age.text()), self.gender, float(self.bodyfat.text()))
        self.diet = Diet(person, self.exercise, self.active_job, self.approx_bodyfat)
        self.diet.set_macros()

    def create_macros_plan(self):
        if self.goal == 'gain':
            return self.diet.calculate_macros_gain()
        elif self.goal == 'lose':
            return self.diet.calculate_macros_lose()
        elif self.goal == 'maintain':
            return self.diet.calculate_macros_lose()

    def create_tdee(self):
        return self.diet.total_daily_energy_expenditure()

    def create_lbm(self):
        return self.diet.person.lean_body_mass()

    def print_results(self):
        self.create_diet()
        lbm = self.create_lbm()
        tdee = self.create_tdee()
        self.lbm_display.setText(str(lbm))
        self.tdee_display.setText(str(tdee))
        self.macros_display.setText("hehe")

    # @pyqtSlot()
    # def on_click(self):
    #     QMessageBox.information(self, 'Results', "TDEE: " + 'textbox_value' + "\n" \
    #                         + 'TDEE: ' + "good\n" \
    #                         + 'Daily: ',
    #                         QMessageBox.Ok)

    def clear_inputs(self):
        self.height.clear()
        self.weight.clear()
        self.age.clear()
        self.bodyfat.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    app.exec_()