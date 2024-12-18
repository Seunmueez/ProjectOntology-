from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QTextEdit
from owlready2 import get_ontology
import sys

class ChemistryITS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemistry Intelligent Tutoring System")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()
        
        # Load Chemistry Ontology
        self.ontology_path = "chemistry.owl"  # Replace with the actual OWL file path
        self.ontology = get_ontology(self.ontology_path).load()

    def initUI(self):
        layout = QVBoxLayout()

        # Search Field
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search Chemistry Concept...")
        layout.addWidget(self.search_bar)

        # Search Button
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.search_concept)
        layout.addWidget(self.search_button)

        # Results Display
        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def search_concept(self):
        query = self.search_bar.text()
        if not query:
            self.result_display.setText("Please enter a concept to search.")
            return

        # Search ontology classes
        matched_concepts = [cls for cls in self.ontology.classes() if query.lower() in cls.name.lower()]

        # Display Results
        if matched_concepts:
            result = "Chemistry Concept Results:\n"
            for concept in matched_concepts:
                result += f"Concept: {concept.name}\n"
                if hasattr(concept, 'comment'):
                    result += f"Description: {concept.comment[0]}\n"
                result += "-" * 40 + "\n"
            self.result_display.setText(result)
        else:
            self.result_display.setText("No matching concepts found in Chemistry Ontology.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChemistryITS()
    window.show()
    sys.exit(app.exec_())
