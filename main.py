import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from controller.vote_controller import VoteController
from utils.errors import PersistenceError

class VoteWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        uic.loadUi("ui/vote_window.ui", self)
        self.controller = controller


        self.btnVote.clicked.connect(self.cast_vote)
        self.btnResults.clicked.connect(self.show_results)

        self.lblError.setText("")
        self.update_counts()

    def cast_vote(self):
        voter_id = self.txtVoterID.text()
        try:
            msg = self.controller.cast_vote(
                selected_john=self.radioJohn.isChecked(),
                selected_jane=self.radioJane.isChecked(),
                voter_id=voter_id
            )
            if msg == "Already voted":
                self.lblError.setText("Already voted")
            else:
                self.lblError.setText("")  # clear error if valid
            self.statusbar.showMessage(msg, 3000)
            self.update_counts()
        except PersistenceError as e:
            self.lblError.setText("Error saving votes")

    def show_results(self):
        counts = self.controller.get_results()
        total = self.controller.get_total()
        text = f"John - {counts['John']}, Jane - {counts['Jane']}, Total - {total}"
        QMessageBox.information(self, "Results", text)

    def update_counts(self):
        counts = self.controller.get_results()
        self.lblJohnCount.setText(str(counts["John"]))
        self.lblJaneCount.setText(str(counts["Jane"]))

def main():
    app = QApplication(sys.argv)
    data_file = Path("storage/votes.csv")
    controller = VoteController(data_file)
    window = VoteWindow(controller)
    window.setWindowTitle("Voting App")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
